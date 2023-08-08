# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('send-email/', views.send_email_active_campaign, name='send_email'),
    path('send-email-test/', views.create_contact_automation_send_email, name='send_email'),
]
