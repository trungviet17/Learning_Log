"""Define URL patterns for users"""

from django.urls import path, include 

# add app name 
app_name = 'users'

urlpatterns = [
    # Default auth urls, tell it to send request to Django's default login view
    path('', include('django.contrib.auth.urls')), # Login and Logout views
]