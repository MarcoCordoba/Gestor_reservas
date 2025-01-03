from django.db import models

# Create your models here.

class tenants(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30)

    tipo_documento_opciones = [
        ('DNI', 'DNI'),
        ('PASAPORTE', 'PASAPORTE'), 
        ('LIBRETA ENROLAMIENTO', 'LIBRETA ENROLAMIENTO'),
        ('LIBRETA CIVICA', 'LIBRETA CIVICA'),
    ]

    tipo_documeto = models.CharField(
        max_length=20,
        choices = tipo_documento_opciones,
        default='DNI',
    )

    numero_documento = models.CharField(max_length=20)
    telefono = models.IntegerField()   

    class Meta: #es para que el nombre en el panel de admin este bien escrito
        verbose_name = "tenant"
        verbose_name_plural = "tenants"

    def __str__(self):
        return self.apellido + '' + self.nombre