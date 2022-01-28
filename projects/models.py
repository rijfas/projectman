from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_employee = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)


class Project(models.Model):
    STATUS = (
        ('Not Started', 'Not Started'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Aborted', 'Aborted'),
    )
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS)
    progress = models.SmallIntegerField()
    deadline = models.DateField()

    def __str__(self):
        return self.title
