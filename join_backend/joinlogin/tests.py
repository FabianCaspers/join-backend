from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
import unittest

# Create your tests here.

class LoginTest(TestCase):
    def test_testhomepage(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')
        self.client.login(username='test_user', password='test_user')
        
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)
        
        
    