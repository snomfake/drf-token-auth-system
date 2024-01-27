from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse


class TokenAuthTestCase(APITestCase):
    """Token issuance tests"""

    def setUp(self):
        self.user = User.objects.create(
            username="Test user", password=make_password("secret")
        )
        self.signin_url = reverse("signin")
        self.signup_url = reverse("signup")

    def test_signup(self):
        data = {"username": "newusr", "password": "secret"}
        response = self.client.post(self.signup_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        data = {"username": self.user.username, "password": "secret"}
        response = self.client.post(self.signin_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_negative_login(self):
        data = {"username": self.user.username, "password": "wrongpassword"}
        response = self.client.post(self.signin_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
