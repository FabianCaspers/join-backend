from django.contrib import admin
from .models import Contacts

# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'number', 'company']
    search_fields = ['name', 'email']

admin.site.register(Contacts, ContactsAdmin)