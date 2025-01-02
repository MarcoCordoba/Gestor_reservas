from django.db import models

# Create your models here.
class properties(models.Model):
    
    nombre = models.CharField(max_length=30) #nombre identificativo para la propiedad
    calle = models.CharField(max_length=30) #calle donde se ubica la propiedad 
    numero = models.IntegerField() #numero de la propiedad
    barrio = models.CharField(max_length=30) #barrio dende se encuentra lo propiedad
    localidad = models.CharField(max_length=20) #localidad donde se encuentra la propiedad
    codigo_postal = models.IntegerField() #codigo postal en donde se encuentra la propiedad
    provincia = models.CharField(max_length=20) #provincia en donde se encuantra la propiedad
    pais = models.CharField(max_length=20) #pais en donde se encuantra la propiedad 
    piso = models.IntegerField() #piso en el que se ubica la propiedad
    codigo_depto = models.CharField(max_length=4) #numero, letra o ambos que identifica a un departamento de otros en el mismo domicilio
    capacidad_maxima = models.IntegerField() #capacidad de personas maximas que pueden alojarse en la propiedad 
    precio_por_persona = models.IntegerField() #monto de dinero que se cobra por dia a cada persona que se aloje en la propiedad




