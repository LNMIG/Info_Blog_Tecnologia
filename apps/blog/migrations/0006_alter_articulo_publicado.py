# Generated by Django 4.2.3 on 2023-07-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_articulo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='publicado',
            field=models.BooleanField(default=True, verbose_name='Publicado'),
        ),
    ]
