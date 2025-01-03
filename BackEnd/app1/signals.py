from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Logs
import requests


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        response = requests.get("https://7yuwxm6esrrhvrwnmxvm2id74a0rtdzg.lambda-url.eu-north-1.on.aws/", params={"user_input": instance.id})
        fibo_number = response.json()
        UserProfile.objects.create(competitor=instance, fibo_number=fibo_number)
        Logs.objects.create(user=instance, action="USER_REGISTERED")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
