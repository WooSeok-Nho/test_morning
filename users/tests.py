from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.
class UserReigsterTestCase(APITestCase):
    def test_registration(self):
        url =reverse("user_view")
        user_data = {
            "username":"testuser",
            "fullname":"테스터",
            "email":"test@naver.com",
            "password":"password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response,response)
        
