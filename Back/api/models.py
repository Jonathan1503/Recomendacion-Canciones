from unittest.util import _MAX_LENGTH
from django.db import models

class Usuario(models.Model):
    nombre= models.CharField(max_length=100)
    edad= models.SmallIntegerField()
    genero= models.CharField(max_length=20)
    correo= models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    
    
