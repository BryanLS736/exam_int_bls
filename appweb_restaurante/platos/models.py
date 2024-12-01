from django.db import models

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=45)
    pais = models.CharField(max_length=40, default='')
    precio = models.IntegerField()
    procedencia = models.CharField(max_length=50, default='')