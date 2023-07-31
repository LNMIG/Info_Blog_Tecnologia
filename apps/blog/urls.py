from django.urls import path
from . import views

app_name = 'apps.blog'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),

    path('articulo/<slug:articulo_slug>/', 
         views.ArticuloDetailView.as_view(), name='articulo'),

    path('categoria/<slug:categoria_slug>/', 
         views.ArticulosByCategoriaView.as_view(), name='categoria'),

    path('autor/<str:autor>/',
         views.ArticulosByAutorView.as_view(), name='autor'),

    path('archivo/<int:year>/<int:month>', 
        views.ArticulosByArchivoView.as_view(), name='archivo'),

    path('crear_articulo/',
         views.ArticuloCreateView.as_view(), name='crear_articulo'),

    path('actualizar_articulo/<slug:articulo_slug>',
         views.ArticuloUpdateView.as_view(), name='actualizar_articulo'),

    path('eliminar_articulo/<slug:articulo_slug>',
         views.ArticuloDeleteView.as_view(), name='eliminar_articulo'),

    path('actualizar_comentario/<int:pk>', 
         views.ComentarioUpdateView.as_view(), name='actualizar_comentario'),

    path('eliminar_comentario/<int:pk>', 
         views.ComentarioDeleteView.as_view(), name='eliminar_comentario'),

    path('crear_categoria/',
         views.CategoriaCreateView.as_view(), name='crear_categoria'),

    path('listado_de_categorias/',
         views.CategoriaListView.as_view(), name='listar_categorias'),

    path('eliminar_categoria/<int:pk>',
         views.CategoriaDeleteView.as_view(), name='eliminar_categoria'),

    path('actualizar_categoria/<int:pk>',
         views.CategoriaUpdateView.as_view(), name='actualizar_categoria'),

    path('listado_de_articulos/',
         views.ArticuloListView.as_view(), name='listar_articulos'),

    path('ordenar_articulos/<str:order_by>/<str:order_type>',
         views.ArticulosOrdenadosView.as_view(), name='ordenar_articulos'),

    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('confirmacion/<str:code>/<str:user>/',
         views.ConfirmationView.as_view(), name='confirmacion')
]