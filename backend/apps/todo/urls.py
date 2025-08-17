from django.urls import path, include

from . import views

app_name = 'todo'

urlpatterns = [
    path('api/v1/', include('apps.todo.api.v1.urls', namespace='api-v1')),
    path('create/', views.TodoCreate.as_view(), name='todo-create'),
    path('todos/', views.TodoList.as_view(), name='todo-list'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todo-delete'),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todo-update'),
    path('todos/<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
]
