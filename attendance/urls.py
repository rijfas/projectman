from django.urls import path 
from .views import create_attendance, delete_attendance, list_attendance
app_name = 'attendance'

urlpatterns = [
    path('', list_attendance, name='list'),
    path('create/', create_attendance, name='create'),
    path('<int:pk>/delete/', delete_attendance, name='delete'),
]