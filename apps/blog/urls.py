from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('autor/', views.autor, name='autor'),
    path('archivo/', views.archivo, name='archivo'),
    path('articulo/', views.categoria, name='articulo'),
    path('categoria/', views.categoria, name='categoria'),
]