from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('confirm/<str:token>/', confirm_email, name='confirm_email'),
    path('reset/', password_reset_request, name='password_reset_request'),
    path('reset/<str:token>/', password_reset, name='password_reset'),
]