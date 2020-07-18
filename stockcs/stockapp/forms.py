from django import forms
from stockapp.models import Name, Producto, Variante

class NameForm(forms.ModelForm):
    name_value = forms.CharField(max_length=100, help_text = "Enter a name")

    class Meta:
        model = Name
        fields = ('name_value',)


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, help_text = "Nombre")

    class Meta:
        model = Producto
        fields = ('nombre',)


class VarianteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, help_text = "Nombre")

    class Meta:
        model = Variante
        fields = ('nombre',)
