from rest_framework import viewsets, permissions
from .models import Contacts
from .serializers import ContactsSerializer

class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticated]