from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"

    def __str__(self):
        return f'{self.username}'