from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Name(models.Model):
    name_value = models.CharField(max_length=100)

    def __str__(self): # if Python 2 use __unicode__
        return self.name_value


class ProductoTipo(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.nombre


class ProductoSubTipo(models.Model):
    tipo = models.ForeignKey(ProductoTipo, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.nombre


class Producto(models.Model):
    tipo = models.ForeignKey(ProductoSubTipo, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.nombre


class EtiquetaTipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self): 
        return self.nombre


class Etiqueta(models.Model):

    tipo = models.ForeignKey(EtiquetaTipo, on_delete=models.CASCADE) 
    valor = models.CharField(max_length=100)

    def __str__(self): 
        return tipo.nombre + ":" + self.valor

class Variante(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    etiquetas = models.ManyToManyField(Etiqueta)

    def __str__(self): 
        return producto.nombre

