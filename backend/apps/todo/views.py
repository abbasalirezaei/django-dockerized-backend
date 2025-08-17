from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoForm


class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        import time
        time.sleep(2)  # just for testing cache
        return Todo.objects.filter(user=self.request.user).only('title', 'completed')
    # per-view caching for 2 minutes :Cache the entire output of a view for a set duration.

    @method_decorator(cache_page(60 * 5, key_prefix="todo_list"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    # form_class = TodoForm
    fields = ['title', 'description', 'completed']
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:todo-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'
    context_object_name = 'todo'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm  # Use your custom form if needed
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:todo-list')

    def get_queryset(self):
        # Only allow updating user's own todos
        return Todo.objects.filter(user=self.request.user)


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:todo-list')

    def get_queryset(self):
        # Only allow deleting user's own todos
        return Todo.objects.filter(user=self.request.user)
