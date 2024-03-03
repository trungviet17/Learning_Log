'''
- Allowing the user to add new topic, we add new module called forms.py which containt the form

'''

# import form module and model we will work (Topic)
from django import forms 
from .models import Topic 

# class inherits from form.ModelForm 

class TopicForm(forms.ModelForm):
    # the simplest version  of ModelForm consist of a nested  Meta class that contains the model it is based on

    #  lớp con meta trong form dùng để cấu hình hiện thị, bổ sung ràng buộc, cấu hình, hành vi truy vấn 
    class Meta: 
        # build form from the topic model include text fields, generate a label for the text field
        model = Topic 
        fields = ['text']
        labels = {'text' : ''}

