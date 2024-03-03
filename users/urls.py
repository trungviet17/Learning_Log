"""Define URL patterns for users"""

from django.urls import path, include 
from . import views 
# add app name 
app_name = 'users'

urlpatterns = [
    # Default auth urls, tell it to send request to Django's default login view
    # https://docs.djangoproject.com/en/5.0/topics/auth/default/#auth-web-requests
    path('', include('django.contrib.auth.urls')), # Login and Logout views
    path('register/', views.register, name = 'register'),
]
