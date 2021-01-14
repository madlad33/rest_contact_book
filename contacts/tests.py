from django.test import TestCase
from .models import contacts
from .serializers import ContactSerializer
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory


# Create your tests here.
from . import views
CREATE_URL = reverse('create')

class ContactsAPITest(TestCase):
    def setUp(self):
        """Basic setup"""
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test1@test.com',
            password='testpass'

        )
        self.client.force_authenticate((self.user))
    def test_create_contact(self):
        """Test creating contacts"""
        payload = {
            'name': 'gg',
            'email': 'test@test.com',
            'mobile_no': '+919999999999',
            'address': 'Test address'

        }
        response = self.client.post(CREATE_URL,payload)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


    def test_create_invalid(self):
        """Test creating invalid fails"""
        payload = {
            'name':' ',
            'email': 'test@test.com',
            'mobile_no': '9999999999',
            'address': 'Test address'

        }
        response =self.client.post(CREATE_URL,payload)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_retrieve_data(self):
        """Test retrieving data"""
        payload = {
            'name': 'test',
            'email': 'test@test.com',
            'mobile_no': '+919999999999',
            'address': 'Test address'

        }
        contacts.objects.create(**payload)
        contact = contacts.objects.all()
        response = self.client.get(reverse('get_all'))
        serializer = ContactSerializer(contact,many=True)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['results'],serializer.data)


    def test_delete_contact(self):
        """Test deleting contacts"""
        payload = {
                'name': 'gg',
                'email': 'test@test.com',
                'mobile_no': '+919999999999',
                'address': 'Test address'

            }
        data = contacts.objects.create(**payload)
        response = self.client.delete(reverse('update',kwargs={'pk':data.pk}))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
