from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UserRegistrationTestCase(APITestCase):
    def test_registration_success(self):
        """
        Тест на успешную регистрацию пользователя.
        """
        url = reverse('user-registration')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'somepassword123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_cannot_use_the_same_email(self):
        """
        Тест на успешную регистрацию пользователя.
        """
        url = reverse('user-registration')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'somepassword123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        response = self.client.post(url, data)
        # попробуем сново
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
