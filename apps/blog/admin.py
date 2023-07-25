from django.contrib import admin
from . import models

admin.site.site_header = 'Administración del Blog'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Blog'

# Register your models here.

#ACERCA
class AcercaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('descripcion', 'creacion')

admin.site.register(models.Acerca, AcercaAdmin)

#REDES SOCIALES

class RedAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'url', 'icono')

admin.site.register(models.Red, RedAdmin)

#CATEGORIA
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')
    prepopulated_fields = {'slug': ('nombre', )}

admin.site.register(models.Categoria, CategoriaAdmin)


#ETIQUETA
class EtiquetaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')

admin.site.register(models.Etiqueta, EtiquetaAdmin)


#COMENTARIO
class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('autor', 'contenido', 'articulo', 'publicado')

admin.site.register(models.Comentario, ComentarioAdmin)


#ARTICULO
class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('titulo', 'categoria', 'publicado', 'autor', 'creacion', 'articuloEtiquetas')
    prepopulated_fields = {'slug': ('titulo', )}
    ordering = ('autor', '-creacion')
    search_fields = ('titulo', 'contenido', 'autor__username', 'categoria__nombre')
    list_filter = ('autor', 'categoria', 'etiquetas')

    def articuloEtiquetas(self, obj):
        return ' - '.join([etiqueta.nombre for etiqueta in obj.etiquetas.all().order_by('nombre')])
    
    articuloEtiquetas.short_description = 'Etiquetas'

admin.site.register(models.Articulo, ArticuloAdmin)