from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import Hotel, Room, Booking


class HotelSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    def get_price(self, hotel: Hotel):
        return hotel.price

    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingCreationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Booking
        fields = ('room', 'check_in', 'check_out', 'guests', 'user',)

    def create(self, validated_data):
        """Переопределяем метод создания для обработки исключений."""
        try:
            return super().create(validated_data)
        except ValidationError as e:
            raise serializers.ValidationError({'non_field_errors': e.messages})

    def update(self, instance, validated_data):
        """Переопределяем метод обновления для обработки исключений."""
        try:
            return super().update(instance, validated_data)
        except ValidationError as e:
            raise serializers.ValidationError({'non_field_errors': e.messages})


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
