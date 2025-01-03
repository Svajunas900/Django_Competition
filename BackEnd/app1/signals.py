from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
import requests


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        response = requests.get("https://7yuwxm6esrrhvrwnmxvm2id74a0rtdzg.lambda-url.eu-north-1.on.aws/", params={"user_input": instance.id})
        print(response.status_code, response.json())
        fibo_number = response.json()
        print(fibo_number, type(fibo_number))
        UserProfile.objects.create(competitor=instance, fibo_number=fibo_number)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()