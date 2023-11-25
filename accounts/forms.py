from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'shadow-none border-dark'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'shadow-none border-dark'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'shadow-none border-dark'}))
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']
        
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
        
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'shadow-none border-dark'}))
    class Meta:
        model = CustomUser
        fields = ['email']