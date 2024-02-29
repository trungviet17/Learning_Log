from django.contrib import admin

# Register your models here.

# the dot to tell django to look for model.py in the same directory as admin.py
from .models import Topic, Entry 

# manage our model through the admin site
admin.site.register(Topic)
admin.site.register(Entry)