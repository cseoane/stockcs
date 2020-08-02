from django.contrib import admin
from stockapp.models import (Name, Producto, Variante, Etiqueta, EtiquetaTipo, 
    ProductoTipo, ProductoSubTipo, ProductoStock, Deposito)
# Register your models here.

admin.site.register(Name)
admin.site.register(Producto)
admin.site.register(Variante)
admin.site.register(Etiqueta)
admin.site.register(EtiquetaTipo)
admin.site.register(ProductoTipo)
admin.site.register(ProductoSubTipo)
admin.site.register(ProductoStock)
admin.site.register(Deposito)
