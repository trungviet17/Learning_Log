'''
- Use the redirect  function to send a user back to the topics page after they submit thier topic
'''


from django.shortcuts import render, redirect

# import topic trong model 
from .models import Topic, Entry

from .forms import TopicForm, EntryForm
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


'''
- Needs to handle two different situations : 
    1. Initial request for the new_topic page 
    2. Processing of any data submitted in the form 
- How function work ? 
    1. Function below take in the request as the parameter 
    2. The user initally request this page -> browser  sends GET request to the server 
    3. When user has filled up on the request 
'''


def new_topic(request)  : 
    '''Add new topic'''
    if request.method != 'POST': 
        # no data submitted, create blank form 
        form = TopicForm()
    else : 
        # post data submitted, process data 
        form = TopicForm(data = request.POST) 
        # check all require field have been filled in
        if form.is_valid() : 
            # write data from the the form to the database 
            form.save()
            # redirect the user's browser to the topics page, where the user should see the topic they just entered in the list of topic
            return redirect('learning_logs:topics')

    # display a blank or invalid form 
    context = {'form' : form }
    return render(request, 'learning_logs/new_topic.html', context)  



def new_entry(request, topic_id): 
    """Add new entry for a particular topic"""

    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST': 
        form = EntryForm()

    else : 
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # create new entry but not save it into database
            new_entry = form.save(commit=False)
            # assign the created object to the topic
            new_entry.topic = topic
            # now we can save it into the database
            new_entry.save()

            return  redirect('learning_logs:topic',  topic_id = topic_id) 
        
    context = {"topic": topic ,'form' : form} 
    return render(request, 'learning_logs/new_entry.html', context=context)  


"""
- GET request: Return a form for editing the entry 
- POST request: saves the modifiled text into the database 
"""
def edit_entry(request, entry_id) : 
    """Edit an existing entry"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if request.method != 'POST': 
        # create a form instance based on the information associated with the existing entry object
        form = EntryForm(instance=entry)
    else : 
        # update data  in the database 
        form = EntryForm(instance= entry, data =  request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id )
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request,'learning_logs/edit_entry.html', context)

    