from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print(f"Signal executed in thread: {threading.current_thread().name}")
