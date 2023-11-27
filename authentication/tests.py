from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from .models import CustomUser

# Test cases for authentication views
class AuthenticationTests(TestCase):
    """
    Test cases for user authentication views.
    """

    def setUp(self):
        """
        Set up test data and client.
        """
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        # User data for registration and login
        self.user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword',
            'confirm_password': 'testpassword',
        }

    def test_user_registration(self):
        """
        Test user registration.
        """
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        """
        Test user login after registration.
        """
        # Register a user first
        self.client.post(self.register_url, self.user_data)

        # Attempt login with registered credentials
        login_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        response = self.client.post(self.login_url, login_data)

        # Check if login is successful and JWT tokens are returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

