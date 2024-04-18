from rest_framework.serializers import ModelSerializer, FloatField

from services.permissions import BookPermissionsService
from books.models import Books, Authors, Tags


class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class AuthorsShortSerializer(ModelSerializer):
    class Meta:
        model = Authors
        fields = ('name', 'surname', 'last_name',)


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class BooksSerializer(ModelSerializer):
    authors = AuthorsShortSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    rating = FloatField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Books

    def to_representation(self, instance):
        """
        Dynamically add 'file' if user has view file permission.
        """
        representation = super().to_representation(instance)
        request = self.context.get('request')

        if request and request.user.is_authenticated:
            # Проверяем, есть ли у пользователя доступ к файлу этой книги
            has_permission_to_view_file = BookPermissionsService.has_permission(instance, request.user, 'view')

            if not has_permission_to_view_file:
                # Если у пользователя нет доступа, удаляем информацию о файле
                representation.pop('file', None)
        else:
            # Если пользователь не авторизован
            representation.pop('file', None)

        return representation
