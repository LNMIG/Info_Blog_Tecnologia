from django.urls import path

from . import views


urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),

    path('articulo/<slug:articulo_slug>/',
         views.ArticuloDetailView.as_view(), name='articulo'),

    path('categoria/<slug:categoria_slug>/',
         views.ArticulosByCategoriaView.as_view(), name='categoria'),

    path('autor/<str:autor>/', views.ArticulosByAutorView.as_view(), name='autor'),

    path('archivo/<int:year>/<int:month>',
         views.ArticulosByArchivoViews.as_view(), name='archivo'),

    # path('404/', views.NotFoundView.as_view(), name='custom_404'),
]