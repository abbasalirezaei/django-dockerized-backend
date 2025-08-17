from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


from apps.todo.models import Todo
from .serializers import TodoSerializer


class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    

class TodoDetailView(RetrieveUpdateDestroyAPIView):
    """ Detail view for a single todo item. """
    # permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
