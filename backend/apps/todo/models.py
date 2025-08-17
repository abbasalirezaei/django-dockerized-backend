from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Todo(models.Model):
    """"Model representing a todo item in the application."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Todo Item'
        verbose_name_plural = 'Todo Items'
        indexes = [
            models.Index(fields=['completed']),
            models.Index(fields=['created_at']),
        ]
    def mark_as_completed(self):
        self.completed = True
        self.save()