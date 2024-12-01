from django.db import models

# Create your models here.

class Comensal(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=8, default='00000000')
