from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from constants import API_DESCRIPTION, ENDPOINTS, MY_NAME, MY_EMAIL

# Homepage

def home(request):
    return render(request, 'home.html', {'api_description':API_DESCRIPTION, 'my_name':MY_NAME,'my_email':MY_EMAIL})

# Docs

def docs(request):
    return render(request, 'docs.html', {'endpoints':ENDPOINTS})

# Checks if authenticated user is staff

def is_admin(user):
    return user.is_authenticated and user.is_staff

class AdminRequiredMixin:
    @method_decorator(user_passes_test(is_admin))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)