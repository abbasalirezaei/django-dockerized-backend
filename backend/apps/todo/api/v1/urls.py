from django.urls import path
from .views import TodoListCreateAPIView,TodoDetailView
app_name = 'api-v1'
urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view()),
    path('todos/<int:id>/',TodoDetailView.as_view())
]
