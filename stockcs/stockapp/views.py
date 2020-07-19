from django.shortcuts import render, redirect
from stockapp.models import Name, Producto, Variante
from stockapp.forms import NameForm, VarianteForm, ProductoForm

# Create your views here.
def index(request):
    names_from_db = Name.objects.all()

    form = NameForm()

    context_dict = {'names_from_context': names_from_db, 'form': form}

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'index.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'index.html', context_dict)


def productos(request):
    productos_from_db = Producto.objects.all()

    form = ProductoForm()

    context_dict = {'productos_from_context': productos_from_db, 'form': form}

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

    form = VarianteForm()

    context_dict = {'variantes_from_context': variantes_from_db, 'form': form}

    if request.method == 'POST':
        form = VarianteForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'variantes.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'variantes.html', context_dict)
