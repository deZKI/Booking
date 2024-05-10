from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Hotel, Room, Booking, Service
from .serializers import HotelSerializer, RoomSerializer, BookingCreationSerializer, BookingSerializer, \
    ServiceSerializer, HotelDetailSerializer, RoomDetailSerializer, BookingDateSerializer


class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return HotelSerializer
        return HotelDetailSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RoomSerializer
        return RoomDetailSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ['get', 'post']

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).all()

    @swagger_auto_schema(
        method='get',
        operation_description="Получает список всех дат бронирований для указанной комнаты по ID.",
        responses={200: BookingDateSerializer(many=True),
                   400: "Room ID is required"},

        manual_parameters=[
            openapi.Parameter(
                'room_id',
                openapi.IN_QUERY,
                description="ID комнаты, для которой запрашиваются даты бронирований",
                type=openapi.TYPE_INTEGER
            )
        ]
    )
    @action(detail=False, methods=['get'], url_path='booking-dates-by-room')
    def booking_dates_by_room(self, request):
        room_id = request.query_params.get('room_id')  # Получаем roomId из параметров запроса
        if not room_id:
            return Response({"error": "Room ID is required"}, status=400)

        bookings = Booking.objects.filter(room__id=room_id)

        serializer = BookingDateSerializer(bookings, many=True)

        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookingSerializer
        if self.request.method == 'POST':
            return BookingCreationSerializer
        return super().get_serializer_class()
