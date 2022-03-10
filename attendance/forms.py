from dataclasses import fields
from django import forms
from .models import Attendance

class CreateAttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = (
            'employee',
            'date'
        )