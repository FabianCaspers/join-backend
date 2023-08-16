from rest_framework import viewsets
from .models import AddTask
from .serializers import AddTaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class AddTaskViewSet(viewsets.ModelViewSet):
    queryset = AddTask.objects.all()
    serializer_class = AddTaskSerializer


@api_view(['DELETE'])
def delete_all_tasks(request):
    tasks = AddTask.objects.all()
    tasks.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)