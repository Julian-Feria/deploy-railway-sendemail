from django.urls import path
from .views import emails_list

urlpatterns = [
    path('emails/', emails_list, name='emails_list'),
]