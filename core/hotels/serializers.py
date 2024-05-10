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


class HotelSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    def get_price(self, hotel: Hotel):
        return hotel.price

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'location', 'description', 'image', 'rating', 'price',)


class RoomSerializer(serializers.ModelSerializer):
    room_type_display = serializers.CharField(source='get_room_type_display')  # Выводит полное название типа комнаты
    images = RoomImageSerializer(many=True)
    amenities = AmenitySerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'room_number', 'room_type_display', 'images', 'amenities',)


class RoomDetailSerializer(RoomSerializer):
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'room_number', 'hotel', 'price', 'amenities', 'room_type', 'room_type_display', 'images',)


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
        fields = ('room', 'check_in', 'check_out', 'user', 'guest_surname', 'guest_name', 'guest_number', 'guest_email')

    def create(self, validated_data):
        """Переопределяем метод создания для обработки исключений."""
        try:
            price = validated_data['room'].price
            validated_data['price'] = price
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
    room = RoomDetailSerializer()

    class Meta:
        model = Booking
        fields = '__all__'


class BookingDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('check_in', 'check_out')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
