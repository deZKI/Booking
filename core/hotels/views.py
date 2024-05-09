from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Hotel, Room, Booking, Service
from .serializers import HotelSerializer, RoomSerializer, BookingCreationSerializer, BookingSerializer, \
    ServiceSerializer, HotelDetailSerializer


class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return HotelSerializer
        return HotelDetailSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ['get', 'post']

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookingSerializer
        if self.request.method == 'POST':
            return BookingCreationSerializer
        return super().get_serializer_class()
