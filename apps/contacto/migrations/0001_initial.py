# Generated by Django 4.2.3 on 2023-07-23 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(blank=True, max_length=120, verbose_name='Nombre y Apellido')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('asunto', models.CharField(blank=True, max_length=50, verbose_name='Asunto')),
                ('mensaje', models.TextField(blank=True, verbose_name='Mensaje')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
            ],
        ),
    ]
