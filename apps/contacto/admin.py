from django.contrib import admin
from . import models


# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'fecha')
    list_display = ('nombre_apellido', 'email', 'asunto', 'mensaje')

admin.site.register(models.Contacto, ContactoAdmin)