from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from utils import is_admin
from constants import *

def home(request):
    return render(request, 'home.html', {'server_url':SERVER_URL})

def api_docs(request):
    return render(request, 'api_docs.html', {'endpoints':ENDPOINTS})

def credits(request):
    return render(request, 'credits.html', {
        'data_source':DATA_SOURCE,
        'author':AUTHOR,
        })
    
@user_passes_test(is_admin)
def admin_api(request):
    return render(request, 'admin_api.html', {'endpoints':ADMIN_ENDPOINTS})
