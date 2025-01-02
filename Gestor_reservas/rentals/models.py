from django.db import models

# Create your models here.

class rentals(models.Model):

    fecha_ingreso = models.DateField() #fecha de ingreso a la propiedad
    fecha_egreso = models.DateField() #fecha de egreso de la propiedad
    hora_ingreso = models.TimeField() #hora de ingreso a la propiedad
    hora_egreso = models.TimeField() #hora de egreso de la propiedad
    cantidad_personas = models.IntegerField(max_length=2) #cantidad de personas que se alojaran en la propiedad


    estado_alquiler_opciones = [
        ('PENDIENTE', 'PENDIENTE'),
        ('ACTIVO', 'ACTIVO'),
        ('CANCELADO', 'CANCELADO'),
        ('FINALIZADO', 'FINALIZADO'),
    ]
    
    estado_alquiler = models.CharField(
        max_length=20,
        choices = estado_alquiler_opciones,
        default='PENDIENTE',
    )

    observaciones = models.TextField(max_length=100) #observaciones que se quieran agregar al alquiler
