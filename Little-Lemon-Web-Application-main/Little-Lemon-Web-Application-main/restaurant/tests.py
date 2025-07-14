from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Menu
from decimal import Decimal

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass123'
        )
        Menu.objects.create(
            title="IceCream",
            price=Decimal('80.00'),
            inventory=100
        )

    def test_get_menu(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_menu(self):
        data = {
            "title": "Pizza",
            "price": "100.00",
            "inventory": 50
        }
        response = self.client.post('/api/menu/', data)
        self.assertEqual(response.status_code, 201)