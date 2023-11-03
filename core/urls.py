from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('api/', api_docs, name='api_docs'),
    path('api/admin/', admin_api, name='admin_api'),
    path('credits/', credits, name='credits'),
]