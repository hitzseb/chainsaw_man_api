import secrets
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

from django.core.mail import send_mail

from .forms import RegisterForm

# Register

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.confirmation_token = secrets.token_urlsafe(32)
            user.username = user.email
            user.save()
            subject = 'Confirm your account'
            message = f'Thank you for registering in the Chainsaw Man API. Please follow this link to activate your account: http://127.0.0.1:8000/accounts/confirm/{user.confirmation_token}'
            from_email = 'hitzseb.test@gmail.com'
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return render(request, 'verification_sent.html')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
 
def logout_view(request):
    logout(request)
    return redirect('home')

# Email confirmation

def confirm_email(request, token):
    User = get_user_model()
    try:
        user = User.objects.get(confirmation_token=token)
    except User.DoesNotExist:
        return HttpResponse('Invalid token')
    user.is_active = True
    user.confirmation_token = ''
    user.save()
    return render(request, 'confirmation_success.html')