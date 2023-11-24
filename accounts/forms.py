from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']
        
class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = CustomUser