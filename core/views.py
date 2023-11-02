from django.shortcuts import render
from constants import SERVER_URL

def home(request):
    return render(request, 'home.html', {'server_url':SERVER_URL})
