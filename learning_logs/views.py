from django.shortcuts import render

# import topic trong model 
from .models import Topic 

# Create your views here.

def index(request): 
    """The home page for learning logs"""
    return render(request, 'learning_logs/index.html')

# request object Django received from the server
def topics(request): 
    """Show all the topics."""
    # query the database 
    topics = Topic.objects.order_by('date_added')
    # define the context that we'll send to the template 
    context = {'topics' : topics}

    return render(request, 'learning_logs/topics.html', context)