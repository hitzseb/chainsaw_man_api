import secrets
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.core.mail import send_mail
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from constants import MY_EMAIL_HOST_USER, SERVER_URL
from .models import CustomUser
from .forms import *

# Register
# sets the confirmation token
# sets the username as the email
# saves the user and sends an email with a confirmation link
# as /accounts/confirm/<confirmation_token>
# user.is_active is set to False until the user clicks the link

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            token = secrets.token_urlsafe(32)
            user.username = user.email
            user.confirmation_token = f'{user.username}_{token}'
            user.save()
            subject = 'Confirm your account'
            message = f'''
            Hello,
            
            Thank you for registeringin the Chainsaw Man API.
            
            Please follow this link to activate your account: 
            {SERVER_URL}accounts/confirm/{user.confirmation_token}
            
            Chainsaw Man API
            '''
            from_email = MY_EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email,
                      recipient_list, fail_silently=False)
            message = '''
            We have sent an email to you for verification. 
            Follow the link provided to finalize the signup process. If 
            you do not see the verification email in your main inbox, 
            check your spam folder. Please contact us if you do not 
            receive the verification email within a few minutes.
            '''
            return render(request, 'message.html', {'message': message})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login
# when the user logs in, 
# it will be redirected to the page he was trying to access 
# or to homepage in case of no next parameter

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout

def logout_view(request):
    logout(request)
    return redirect('home')

# Email confirmation
# it verifies if the confirmation token is valid
# by getting the user by the token
# in that case it sets user.is_active to True

def confirm_email(request, token):
    User = get_user_model()
    try:
        user = User.objects.get(confirmation_token=token)
    except User.DoesNotExist:
        message = 'Invalid token'
        return render(request, 'message.html', {'message': message})
    user.is_active = True
    user.confirmation_token = ''
    user.save()
    message = 'Email verification success. Your account is now activated.'
    return render(request, 'message.html', {'message': message})

# Password recovery
# takes the email from the user 
# sets a new confirmation token
# and sends an email with a link that uses the confirmation token

def password_reset_request(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_object_or_404(CustomUser, username=email)
            token = secrets.token_urlsafe(32)
            user.confirmation_token = f'{user.username}_{token}'
            user.save()
            reset_url = f'{SERVER_URL}accounts/reset/{user.confirmation_token}/'
            subject = 'Change password'
            message = f'''
            Hello,
            
            We've received a request to reset the password for your account. If you didn't make this request, you can ignore this email.
            
            To reset your password, click on the following link:
            {reset_url}
            
            Chainsaw Man API
            '''
            from_email = MY_EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email,
                      recipient_list, fail_silently=False)
            message = 'We sent you an email with instructions to reset your password.'
            return render(request, 'message.html', {'message': message})
    else:
        form = CustomPasswordResetForm()
    return render(request, 'password_reset_request.html', {'form': form})

# this is the actual password reset
# it verifies if the confirmation token is valid
# by getting the user by the token
# in that case it shows the password reset form
# with two fields for the new password
# if they match and are valid, the password is changed

def password_reset(request, token):
    user = get_object_or_404(CustomUser, confirmation_token=token)

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 and password1 == password2:
            try:
                validate_password(password1, user=user)
                user.set_password(password1)
                user.confirmation_token = ''
                user.save()
                message = 'Password succesfully changed.'
                return render(request, 'message.html', {'message': message})
            except ValidationError as e:
                message = ', '.join(e.messages)
                return render(request, 'message.html', {'message': message})
        else:
            message = 'Passwords do not match.'
            return render(request, 'message.html', {'message': message})

    return render(request, 'password_reset.html', {'user': user})