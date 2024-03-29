"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Which page to build in response to browser  requests

# import module và function để quản lý URLS cho admin site 
from django.contrib import admin
from django.urls import path, include

# define the urlpatterns variable, includes sets of URLS from the apps in the project.
urlpatterns = [
    path('admin/', admin.site.urls), # defines all the urls that can be requested from the admin site
    path('', include('learning_logs.urls')), # add line to include the module learning_logs.urls 
    path('users/', include('users.urls'))
]
