from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from .models import CustomUser

# RegisterForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

# LoginForm
# Just like standard AuthenticationForm, 
# but with an email label instead of username
        
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        
# CustomPasswordResetForm
# used for requesting a password reset email

class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = CustomUser
        fields = ['email']