# Generated by Django 4.2.3 on 2023-07-30 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_articulo_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
