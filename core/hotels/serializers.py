from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import Hotel, Room, Booking, Service, Amenity, HotelImage, RoomImage


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['image']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['image']


class RoomSerializer(serializers.ModelSerializer):
    room_type_display = serializers.CharField(source='get_room_type_display')  # Выводит полное название типа комнаты
    images = RoomImageSerializer(many=True)

    class Meta:
        model = Room
        fields = ('room_number', 'room_type_display', 'images',)


class RoomDetailSerializer(RoomSerializer):
    class Meta:
        model = Room
        fields = ('room_number', 'hotel', 'price', 'amenities', 'room_type', 'room_type_display', 'images',)


class HotelSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    def get_price(self, hotel: Hotel):
        return hotel.price

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'location', 'description', 'image', 'rating', 'price',)


class HotelDetailSerializer(HotelSerializer):
    amenities = AmenitySerializer(many=True, read_only=True)
    rooms = RoomSerializer(many=True, source='room_set')

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'location', 'description', 'image', 'rating', 'price', 'amenities', 'rooms')


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


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
