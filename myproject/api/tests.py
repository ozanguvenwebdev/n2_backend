from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import *


class UserViewSetTests(APITestCase):

    def setUp(self):
        # Create related objects
        geo = Geo.objects.create(lat=39.950289, lng=32.7732722)
        address = Address.objects.create(street="Çamlıca Mahallesi", suite="Apt. 556", city="Ankara", zipcode="06200", geo=geo)
        company = Company.objects.create(name="N2Mobil Araç Takip Sistemleri A.Ş.")
        
        # Create a user
        self.user = User.objects.create(
            name="Müslüm Türk",
            username="muslum.turk",
            email="muslum.turk@n2mobil.com.tr",
            address=address,
            phone="+90 555 555 55 55",
            website="www.n2mobil.com.tr",
            company=company
        )
        
        self.user_url = reverse('user-detail', kwargs={"pk": self.user.pk})
        self.user_list_url = reverse('user-list')

    def test_list_users(self):
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["username"], self.user.username)

    def test_retrieve_user(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)

    def test_create_user(self):
        geo = Geo.objects.create(lat=34.56, lng=78.90)
        address = Address.objects.create(street="New Street", suite="Apt 2", city="New City", zipcode="67890", geo=geo)
        company = Company.objects.create(name="New Company")
        
        payload = {
            "name": "Jane Doe",
            "username": "janedoe",
            "email": "janedoe@example.com",
            "address": {
                "street": address.street,
                "suite": address.suite,
                "city": address.city,
                "zipcode": address.zipcode,
                "geo": {"lat": str(geo.lat), "lng": str(geo.lng)},
            },
            "phone": "987-654-3210",
            "website": "https://janedoe.com",
            "company": {"name": company.name},
        }
        response = self.client.post(self.user_list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "janedoe")

    def test_update_user(self):
        payload = {
            "name": "John Updated",
            "username": "johnupdated",
            "email": "updated@example.com",
            "address": {
                "street": "Updated Street",
                "suite": "Apt Updated",
                "city": "Updated City",
                "zipcode": "00000",
                "geo": {"lat": "12.12", "lng": "34.34"},
            },
            "phone": "111-222-3333",
            "website": "https://updated.com",
            "company": {"name": "Updated Company"},
        }
        response = self.client.put(self.user_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "johnupdated")

    def test_delete_user(self):
        response = self.client.delete(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
