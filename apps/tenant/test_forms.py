from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Tenant


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

    def test_create_tenant(self):
        self.client.login(username='dejuata', password='America27')
        self.assertEqual(Tenant.objects.count(), 0)
        data = {
            'nit': 123456,
            # 'logo',
            'razon_social': 'Tranzapata',
            # 'nombre_comercial',
            'telefono': 5573847,
            'correo': 'dejuata@hotmail.com',
            'ciudad': 'Cali',
            'direccion': 'TR 8 # 18 - 21'
        }
        self.client.post('/registrar-empresa/', data)
        self.assertEqual(Tenant.objects.count(), 1)
