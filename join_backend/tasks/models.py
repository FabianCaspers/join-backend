from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    assigned = models.CharField(max_length=100)
    dueDate = models.DateField()
    prio = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='todo')

    def __str__(self):
        return self.title
