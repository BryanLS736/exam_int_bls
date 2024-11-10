from django.db import models
from django.db.models import IntegerField

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length =30)
    apellido = models.CharField(max_length =30)
    dni = models.CharField(max_length = 8, default = '00000000')