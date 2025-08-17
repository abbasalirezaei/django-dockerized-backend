from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from django.core.cache import cache
from .models import Todo
from .tasks import send_todo_reminder

@receiver(post_save, sender=Todo)
def schedule_todo_reminder(sender, instance, created, **kwargs):
    if created:
        reminder_time = timezone.now() + timedelta(minutes=1)  # for demo
        send_todo_reminder.apply_async((instance.id,), eta=reminder_time)




@receiver([post_save,post_delete], sender=Todo)
def invalidate_hotel_cache(sender, instance, **kwargs):
    """
    Invalidate the cache for the todo list when a Todo is created, updated, or deleted.
    """
    
    cache.delete_pattern('*todo_list*')
