'''
- Model tells Django how to work that will be stored in the app 

'''
"""
A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data you’re storing. 
Generally, each model maps to a single database table.

"""


from django.db import models

# Create your models here.

class Topic(models.Model): 
    """A topic the user is learning about."""
    text = models.CharField(max_length=200) # Allow
    # record date and time add 
    date_added = models.DateTimeField(auto_now_add = True)

    # display a simple representation of a model
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    

class Entry(models.Model): 
    """An entry on a specific topic"""
    # the on_delete argument tells django that when a topic is deleted, all entries associated with this topic should be deleted too
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)

    # Text field doesn't need a size limit 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True) 

    # allows us to set a special att telling Django to use Entries when it needs to multiple entries
    class Meta: 
        verbose_name_plural = 'entries'
    # which infor to show when refers to individual entries
    def __str__(self):
        if len(self.text < 50) : return self.text
        return f"{self.text[:50]}..."