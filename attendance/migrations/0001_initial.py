# Generated by Django 4.0.1 on 2022-03-03 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('marked', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_model', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager_model', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
