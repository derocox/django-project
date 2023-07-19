from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    identificacion = models.IntegerField(default=0)
    nombres = models.CharField(max_length=50)
    telefono = models.IntegerField(default=0)
    tipo = models.CharField(max_length=10)
    email = models.CharField(max_length=50, default='')