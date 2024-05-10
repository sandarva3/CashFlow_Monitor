from django import forms
from .models import Event

class Eventform(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name']
        error_messages = {
                'Names should be less than 125 characters'
        }