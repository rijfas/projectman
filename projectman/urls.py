from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='landing_page.html'), name='landing'),
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls', namespace='projects')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('attendance/', include('attendance.urls', namespace='attendance')),
    path('meetings/', include('meetings.urls', namespace='meetings')),
]