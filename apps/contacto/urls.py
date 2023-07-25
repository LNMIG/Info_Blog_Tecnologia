from django.urls import path
from . import views

app_name = 'apps.contacto'

urlpatterns = [
    path('contacto/', views.ContactoCreateView.as_view(), name='contacto'),
]
