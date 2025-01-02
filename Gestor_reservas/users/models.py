from django.db import models

# Create your models here.

class users(models.Model):

    nombre = models.CharField(max_length=30) #nombre del usuario  
    apellido = models.CharField(max_length=30) #apellido del usuario 
    correo = models.EmailField(max_length=30)
    telefono = models.IntegerField()
    tipo_juridico = models.CharField(max_length=20)
    razon_social = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=20, unique=True)
    contraseña = models.CharField(max_length=20)

