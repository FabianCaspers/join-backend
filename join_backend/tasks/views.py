from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['DELETE'])
def delete_all_tasks(request):
    tasks = Task.objects.all()
    tasks.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
