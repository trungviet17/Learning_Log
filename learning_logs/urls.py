""" Define URL patterns for learning_logs"""

from django.urls import path # import path function
from . import views # import view module from the same direction

app_name = 'learning_logs' # distinguish this file from file the same name in other app within the project


urlpatterns = [
    # Home page 
    # first argument in path is string that help Django route the current request properly
    # Django recieve the request URL and its find in URL pattern one that match the current request

    # second argument in path is specifies which function to call in views.py (its call index function)

    # third argument in path provide the name that we use instead of writing out a URL
    path('', views.index, name='index'),

    # Page show all topic 
    path('topics/', views.topics, name = 'topics')
]
