from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from .models import CustomUser

# RegisterForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'shadow-none border-dark'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'shadow-none border-dark'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'shadow-none border-dark'}))
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

# LoginForm
# Just like standard AuthenticationForm, 
# but with an email label instead of username
        
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={'class': 'shadow-none border-dark'}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'shadow-none border-dark'}),
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        
# CustomPasswordResetForm
# used for requesting a password reset email

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'shadow-none border-dark'}))
    class Meta:
        model = CustomUser
        fields = ['email']