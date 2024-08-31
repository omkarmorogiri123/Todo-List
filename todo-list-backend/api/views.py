from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=True, methods=['post'])
    def set_completed(self, request, pk=None):
        todo = self.get_object()
        todo.completed = not todo.completed
        todo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
