from django.urls import path
from .views import project_create_view, project_detail_view, project_list_view, project_delete_view, project_update_view
app_name = 'projects'

urlpatterns = [
    path('', project_list_view, name='list'),
    path('<int:pk>/', project_detail_view, name='detail'),
    path('<int:pk>/delete/', project_delete_view, name='delete'),
    path('<int:pk>/update/', project_update_view, name='update'),
    path('create/', project_create_view, name='create'),
]
