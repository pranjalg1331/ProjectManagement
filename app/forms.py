
from django import forms
 
# import GeeksModel from models.py
from .models import Tasks,Project
 
# create a ModelForm
class TaskForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Tasks
        exclude = ['project']
        
class ProjectForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Project
        fields = "__all__"