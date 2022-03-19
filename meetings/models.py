from django.db import models
from projects.models import User
from employees.models import Employee

# Create your models here.
class Meeting(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    note = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    meet_url = models.CharField(max_length=150)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} with {self.employee} at {self.date}'