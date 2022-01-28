from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms

from employees.models import Employee

User = get_user_model()


class EmployeeCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class EmployeeAssignProjectForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("project",)
