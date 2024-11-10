from django.db import models

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.CharField(max_length=15)
