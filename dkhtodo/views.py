from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from dkhtodo.models import Task
from dkhtodo.serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [permissions.IsAuthenticated()]  # You can modify this permission class as needed for PATCH requests
        return super().get_permissions()
