# Generated by Django 5.1.4 on 2025-01-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tenants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=30)),
                ('tipo_documeto', models.CharField(choices=[('DNI', 'DNI'), ('PASAPORTE', 'PASAPORTE'), ('LIBRETA ENROLAMIENTO', 'LIBRETA ENROLAMIENTO'), ('LIBRETA CIVICA', 'LIBRETA CIVICA')], default='DNI', max_length=20)),
                ('numero_documento', models.CharField(max_length=20)),
                ('telefono', models.IntegerField(max_length=20)),
            ],
        ),
    ]
