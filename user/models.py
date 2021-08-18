from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='user/avatars/')
    score = models.PositiveSmallIntegerField(default=0)

    def get_date_of_birth(self):
        return self.date_of_birth
