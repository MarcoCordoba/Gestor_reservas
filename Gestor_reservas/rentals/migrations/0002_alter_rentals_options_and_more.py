# Generated by Django 5.1.4 on 2025-01-08 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rentals',
            options={'verbose_name': 'rental', 'verbose_name_plural': 'rentals'},
        ),
        migrations.AlterField(
            model_name='rentals',
            name='cantidad_personas',
            field=models.IntegerField(),
        ),
    ]
