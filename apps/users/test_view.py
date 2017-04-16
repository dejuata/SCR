from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class SimpleTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='dejuata',
            email='dejuata@hotmail.com',
            password='America27',
            first_name='Juan',
            last_name='Pino',
        )

    # def test_profile_user(self):
    #     self.client.login(username='dejuata', password='America27')
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)

    # def test_user_login(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
