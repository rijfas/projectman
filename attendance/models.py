from django.db import models
from django.contrib.auth import get_user_model

from employees.models import Employee

User = get_user_model()

# Create your models here.
class Attendance(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField()
    marked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.employee} {self.date} {self.marked}'