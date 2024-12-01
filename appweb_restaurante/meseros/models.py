from django.db import models

# Create your models here.

class Mesero(models.Model):
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=35)
    edad = models.IntegerField(default=0)
    dni = models.CharField(max_length=8, default='00000000')