from datetime import date

from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from users.models import User

from .models import Hotel, Room, Booking


class BookingAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Настройка для API теста
        cls.user = User.objects.create_user(email='testuser', password='12345')
        cls.hotel = Hotel.objects.create(name="Test Hotel", location="Test Location", description="Test Description")
        cls.room = Room.objects.create(hotel=cls.hotel, room_number="101", room_type="single", price=100.00)
        cls.url = reverse('booking-list')  # Убедитесь, что у вас есть имя 'booking-list' в urls.py для BookingViewSet

    def setUp(self):
        self.client.login(email='testuser', password='12345')

    def test_create_booking(self):
        """
        Проверяем возможность создать бронирование через API.
        """

        data = {
            "room": self.room.id,
            "user": self.user.id,
            "check_in": "2024-04-01",
            "check_out": "2024-04-05",
            "guests": 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_booking_overlap(self):
        """
        Тестируем API на предмет отклонения перекрывающихся бронирований.
        """
        Booking.objects.create(room=self.room, user=self.user, check_in=date(2024, 4, 1),
                               check_out=date(2024, 4, 5),
                               guests=2)
        overlap_data = {
            "room": self.room.id,
            "user": self.user.id,
            "check_in": "2024-04-03",
            "check_out": "2024-04-06",
            "guests": 2
        }
        response = self.client.post(self.url, overlap_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_booking_isolation(self):
        """
        Проверяем, что пользователи не могут получить доступ к бронированиям друг друга.
        """
        other_user = User.objects.create_user(email='otheruser@example.com', password='12345')
        Booking.objects.create(room=self.room, user=other_user, check_in=date(2024, 4, 1),
                               check_out=date(2024, 4, 5), guests=2)

        Booking.objects.create(room=self.room, user=self.user, check_in=date(2025, 4, 1),
                               check_out=date(2025, 4, 5), guests=2)
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 1)  # Предполагается, что первоначальный пользователь не видит чужие брони
