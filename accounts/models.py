from django.db import models
from django.contrib.auth.models import AbstractUser

# CustomUser
# just like Django default User, but with
# unique email wich is used as username
# is_active set to False by default until email is confirmed
# confirmation_token for email confirmation and password reset

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    confirmation_token = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email