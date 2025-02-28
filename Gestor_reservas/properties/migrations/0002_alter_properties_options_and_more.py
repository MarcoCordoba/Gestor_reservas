# Generated by Django 5.1.4 on 2025-01-08 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='properties',
            options={'verbose_name': 'propertie', 'verbose_name_plural': 'properties'},
        ),
        migrations.AlterField(
            model_name='properties',
            name='capacidad_maxima',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='properties',
            name='codigo_postal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='properties',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='properties',
            name='piso',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='properties',
            name='precio_por_persona',
            field=models.IntegerField(),
        ),
    ]
