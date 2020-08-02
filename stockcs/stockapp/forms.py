from django import forms
from django.db import models
from stockapp.models import (Name, Producto, ProductoSubTipo, ProductoTipo, 
Variante, Etiqueta, EtiquetaTipo, ProductoUnidad, ProductoStock, Deposito)

class NameForm(forms.ModelForm):
    name_value = forms.CharField(max_length=100)

    class Meta:
        model = Name
        fields = ('name_value',)


class EtiquetaTipoForm(forms.ModelForm):

    class Meta:
        model = EtiquetaTipo
        fields = ('nombre',)


class EtiquetaForm(forms.ModelForm):
    etiquetaTipos_from_db = EtiquetaTipo.objects.all()
    tipo_padre = forms.ModelChoiceField(queryset=etiquetaTipos_from_db)

    class Meta:
        model = Etiqueta
        fields = ('tipo_padre','valor')


class ProductoTipoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)

    class Meta:
        model = ProductoTipo
        fields = ('nombre',)


class ProductoSubTipoForm(forms.ModelForm):
    productoTipos_from_db = ProductoTipo.objects.all()
    tipo_padre = forms.ModelChoiceField(queryset=productoTipos_from_db)
    nombre = forms.CharField(max_length=100)

    class Meta:
        model = ProductoSubTipo
        fields = ('nombre','tipo_padre')


class ProductoForm(forms.ModelForm):
    productoSubTipos_from_db = ProductoSubTipo.objects.all()
    productoSubTipo = forms.ModelChoiceField(queryset=productoSubTipos_from_db)
    nombre = forms.CharField(max_length=100)

    class Meta:
        model = Producto
        fields = ('nombre','productoSubTipo')


class VarianteForm(forms.ModelForm):
    productos_from_db = Producto.objects.all()
    producto = forms.ModelChoiceField(queryset=productos_from_db)

    class Meta:
        model = Variante
        fields = ('producto','etiquetas','unidad')


class DepositoForm(forms.ModelForm):

    class Meta:
        model = Deposito
        fields = ('nombre','ubicacion')


class ProductoStockForm(forms.ModelForm):

    class Meta:
        model = ProductoStock
        fields = ('variante','cantidad')
