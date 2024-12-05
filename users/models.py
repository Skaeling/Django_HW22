from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text='Введите только цифры')
    avatar = models.ImageField(upload_to='user_avatars/', default='user_avatars/default_avatar.png', blank=True,
                               null=True, help_text='Изображение размером не более 5 мб')
    country = models.CharField(max_length=15, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email
