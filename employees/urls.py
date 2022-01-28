from django.urls import path
from .views import employee_assign_project, employee_list_view, employee_create_view,  employee_detail_view, employee_list_view, employee_delete_view

app_name = 'employees'

urlpatterns = [
    path('', employee_list_view, name='list'),
    path('<int:pk>/', employee_detail_view, name='detail'),
    path('<int:pk>/delete/', employee_delete_view, name='delete'),
    path('<int:pk>/assign-project/',
         employee_assign_project, name='assign-project'),
    path('create/', employee_create_view, name='create'),
]
