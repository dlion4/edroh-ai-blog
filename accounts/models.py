from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user_profile")
    
    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=CustomUser)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

