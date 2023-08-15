from rest_framework import viewsets
from .models import AddTask
from .serializers import AddTaskSerializer

class AddTaskViewSet(viewsets.ModelViewSet):
    queryset = AddTask.objects.all()
    serializer_class = AddTaskSerializer
