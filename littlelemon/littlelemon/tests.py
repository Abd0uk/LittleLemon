from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 80")
        

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pasta", price=10.50, inventory=100)
        self.menu2 = Menu.objects.create(title="Pizza", price=12.00, inventory=100)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)