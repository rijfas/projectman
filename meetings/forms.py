from django.forms import ModelForm
from .models import Meeting

class CreateMeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = (
            'title', 
            'date', 
            'meet_url', 
            'employee', 
            'note'
            )