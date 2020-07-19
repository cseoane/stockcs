from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Name(models.Model):
    name_value = models.CharField(max_length=100)

    def __str__(self): # if Python 2 use __unicode__
        return self.name_value


class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.nombre

class Etiqueta(models.Model):

    nombre = models.CharField(max_length=100)

    valor = models.CharField(max_length=100)

    def __str__(self): 
        return self.nombre

class Variante(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 

    etiquetas = models.ManyToManyField(Etiqueta)

    def __str__(self): 
        return producto.nombre

