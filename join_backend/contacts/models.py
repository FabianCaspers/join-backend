from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    color = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.email}"