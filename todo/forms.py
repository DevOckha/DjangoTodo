from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

    class Meta:
        model = Todo
        fields = '__all__'