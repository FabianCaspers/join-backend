from django.test import TestCase, Client
from .models import Contacts
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class ContactsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass', email='testuser@example.com')
        cls.token, _ = Token.objects.get_or_create(user=cls.user)
        cls.contact = Contacts.objects.create(name='John', email='john@example.com', number='123456789', company='Bad-Company')
    
    def setUp(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
  
    def set_auth_credentials(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_name_label(self):
        contact = Contacts.objects.get(id=1)
        field_label = contact._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_email_label(self):
        contact = Contacts.objects.get(id=1)
        field_label = contact._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')
        
    def test_post_contact(self):
        self.set_auth_credentials()
        data = {
            'name': 'Jane',
            'email': 'jane@example.com',
            'number': '987654321',
            'company': 'Good-Company',
        }
        response = self.client.post('https://fabiancaspersdjango.pythonanywhere.com/contacts/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Jane')

    def test_get_contact(self):
        self.set_auth_credentials()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(f'/contacts/{self.contact.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'John')


    def test_delete_contact(self):
        self.set_auth_credentials()
        response = self.client.delete(f'https://fabiancaspersdjango.pythonanywhere.com/contacts/{self.contact.id}/')
        self.assertEqual(response.status_code, 204)
