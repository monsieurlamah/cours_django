from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    description = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)