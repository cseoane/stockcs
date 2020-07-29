from django.shortcuts import render, redirect
from stockapp.models import Name, Producto, Variante, Etiqueta
from stockapp.forms import NameForm, VarianteForm, ProductoForm, EtiquetaForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def productos(request):
    productos_from_db = Producto.objects.all()

    producto_form = ProductoForm()

    context_dict = {'productos_from_context': productos_from_db, 'producto_form': producto_form}

    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'productos.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'productos.html', context_dict)


def variantes(request):
    variantes_from_db = Variante.objects.all()

    variante_form = VarianteForm()

    context_dict = {'variantes_from_context': variantes_from_db, 'variante_form': variante_form}

    if request.method == 'POST':
        form = VarianteForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'variantes.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'variantes.html', context_dict)


def etiquetas(request):
    etiquetas_from_db = Etiqueta.objects.all()

    etiqueta_form = EtiquetaForm()

    context_dict = {
        'etiquetas_from_context': etiquetas_from_db, 
        'etiqueta_form': etiqueta_form
    }

    if request.method == 'POST':
        form = EtiquetaForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'etiquetas.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'etiquetas.html', context_dict)
