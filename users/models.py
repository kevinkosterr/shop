import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254, verbose_name="Email address")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
