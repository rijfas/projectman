from django.urls import path
from .views import delete, list, create, detail
app_name = 'meetings'

urlpatterns = [
    path('', list, name='list'),
    path('<int:id>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('<int:pk>/delete/', delete, name='delete'),
]

