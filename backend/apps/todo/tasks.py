from celery import shared_task
from django.core.mail import send_mail
from .models import Todo

@shared_task
def send_todo_reminder(todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        send_mail(
            subject=f"Reminder: {todo.title}",
            message=f"Don't forget: {todo.description}",
            from_email='noreply@yourapp.com',
            recipient_list=[todo.user.email],
        )
        return f"Reminder sent for Todo ID {todo_id}"
    except Todo.DoesNotExist:
        return f"Todo ID {todo_id} not found"