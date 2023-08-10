from django import forms
from .models import Event

class Edit_event(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'dec')