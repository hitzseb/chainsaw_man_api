from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    confirmation_token = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email