from django.db import models
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='manager')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
