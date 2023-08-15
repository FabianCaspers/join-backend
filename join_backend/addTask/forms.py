from django import forms
from .models import AddTask

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = ['title', 'description', 'category', 'assigned', 'dueDate', 'prio', 'status']
