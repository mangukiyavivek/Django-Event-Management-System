# event_management/urls.py

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
]
