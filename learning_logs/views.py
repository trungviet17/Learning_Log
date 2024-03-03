from django.shortcuts import render

# import topic trong model 
from .models import Topic 

# Create your views here.

def index(request): 
    """The home page for learning logs"""
    return render(request, 'learning_logs/index.html')

# request object Django received from the server and all associated entries from  the database 
def topics(request): 
    """Show all the topics."""
    # query the database 
    topics = Topic.objects.order_by('date_added')
    # define the context that we'll send to the template 
    context = {'topics' : topics}

    return render(request, 'learning_logs/topics.html', context)

# request object for specific page 
def topic(request, topic_id): 
    # retrieve the topic
    topic = Topic.objects.get(id = topic_id ) 
    # get entry objects associated with this
    entries = topic.entry_set.order_by('-date_added') # get all Entry objects related with this topic

    # create a list of dictionaries containing each entry and its author
    context = {'topic' : topic, 'entries' : entries}

    return render(request, 'learning_logs/topic.html', context) 