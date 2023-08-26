from django.test import TestCase
from .models import Contacts

# Create your tests here.

class ContactsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Contacts.objects.create(name='John', email='john@example.com', number='123456789', company='Bad-Company')

    def test_name_label(self):
        contact = Contacts.objects.get(id=1)
        field_label = contact._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_email_label(self):
        contact = Contacts.objects.get(id=1)
        field_label = contact._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')