# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_event_api, name='create_event_api'),
    path('<int:event_id>/', views.get_event_api, name='get_event_api'),
    path('<int:event_id>/update/', views.update_event_api, name='update_event_api'),
    path('<int:event_id>/delete/', views.delete_event_api, name='delete_event_api'),
]
