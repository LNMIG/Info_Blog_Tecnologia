from django.db import models
from django.utils import timezone

# Create your models here.

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=120, null=False, blank=True, verbose_name='Nombre y Apellido')
    email = models.EmailField(null=False, blank=True, verbose_name='Email')
    asunto = models.CharField(max_length=50, null=False, blank=True, verbose_name='Asunto')
    mensaje = models.TextField(null=False, blank=True, verbose_name='Mensaje')
    fecha = models.DateTimeField(default=timezone.now, verbose_name='Fecha de creación')
    

    def __str__(self):
        return self.nombre_apellido

