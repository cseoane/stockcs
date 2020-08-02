from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Name(models.Model):
    name_value = models.CharField(max_length=100)

    def __str__(self): # if Python 2 use __unicode__
        return self.name_value


class EtiquetaTipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self): 
        return self.nombre


class Etiqueta(models.Model):

    tipo_padre = models.ForeignKey(EtiquetaTipo, on_delete=models.CASCADE) 
    valor = models.CharField(max_length=100)

    def __str__(self): 
        return self.tipo_padre.nombre + ":" + self.valor


class ProductoTipo(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.nombre


class ProductoSubTipo(models.Model):
    tipo_padre = models.ForeignKey(ProductoTipo, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.nombre


class Producto(models.Model):
    productoSubTipo = models.ForeignKey(ProductoSubTipo, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.nombre

class ProductoUnidad(models.Model):

    nombre = models.CharField(max_length=100)
    def __str__(self): 
        return self.nombre


class Variante(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    etiquetas = models.ManyToManyField(Etiqueta)
    unidad = models.ForeignKey(ProductoUnidad, on_delete=models.CASCADE, default=1) 

    def joinEtiquetas(self):
        etiquetasConcatenadas = ":"
        for etiqueta in self.etiquetas.all():
            etiquetasConcatenadas = etiquetasConcatenadas + ", " + etiqueta.valor
        etiquetasConcatenadas = etiquetasConcatenadas.replace(":,",":")
        return etiquetasConcatenadas

    def __str__(self): 
        return self.producto.nombre + self.joinEtiquetas()


class Deposito(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150)
    
    def __str__(self): 
        return self.nombre


class ProductoStock(models.Model):

    fecha = models.DateField(auto_now=False, auto_now_add=True)
    variante = models.ForeignKey(Variante, on_delete=models.CASCADE) 
    cantidad = models.DecimalField(max_digits=12, decimal_places=3)

    def __str__(self): 
        return self.variante.__str__() + " : " + str(self.cantidad) + " " + self.variante.unidad.nombre

    def representacion(self):
        return (self.fecha + "|" + 
        self.variante + " - " + 
        self.cantidad.__str__ + " " + 
        self.variante.unidad.nombre)

