from django.shortcuts import render, redirect
from stockapp.models import (Name, Producto, Variante, Etiqueta, EtiquetaTipo, 
    ProductoTipo, ProductoSubTipo, ProductoStock, Deposito)
from stockapp.forms import (NameForm, VarianteForm, ProductoForm, EtiquetaForm,
    EtiquetaTipoForm, ProductoTipoForm, ProductoSubTipoForm, ProductoStockForm,
    DepositoForm)

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def productoTipos(request):
    productoTipos_from_db = ProductoTipo.objects.all()

    productoTipo_form = ProductoTipoForm()

    context_dict = {'productoTipos_from_context': productoTipos_from_db, 'productoTipo_form': productoTipo_form}

    if request.method == 'POST':
        form = ProductoTipoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'productoTipos.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'productoTipos.html', context_dict)


def productoSubTipos(request):
    productoSubTipos_from_db = ProductoSubTipo.objects.all()

    productoSubTipo_form = ProductoSubTipoForm()

    context_dict = {'productoSubTipos_from_context': productoSubTipos_from_db, 'productoSubTipo_form': productoSubTipo_form}

    if request.method == 'POST':
        form = ProductoSubTipoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'productoSubTipos.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'productoSubTipos.html', context_dict)


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
    print(etiquetas_from_db)

    etiqueta_form = EtiquetaForm()

    context_dict = {
        'etiquetas_from_context': etiquetas_from_db, 
        'etiqueta_form': etiqueta_form
    }
    print(request.method)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'etiquetas.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'etiquetas.html', context_dict)


def etiquetaTipos(request):
    etiquetaTipos_from_db = EtiquetaTipo.objects.all()
    print(etiquetaTipos_from_db)

    etiquetaTipo_form = EtiquetaTipoForm()

    context_dict = {
        'etiquetaTipos_from_context': etiquetaTipos_from_db, 
        'etiquetaTipo_form': etiquetaTipo_form
    }

    if request.method == 'POST':
        form = EtiquetaTipoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'etiquetaTipos.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'etiquetaTipos.html', context_dict)


def depositos(request):
    depositos_from_db = Deposito.objects.all()
    print(depositos_from_db)

    deposito_form = DepositoForm()

    context_dict = {
        'depositos_from_context': depositos_from_db, 
        'deposito_form': deposito_form
    }

    if request.method == 'POST':
        form = DepositoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'depositos.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'depositos.html', context_dict)



def productoStock(request):
    productoStock_from_db = ProductoStock.objects.all()
    print(productoStock_from_db)

    formset = []
    productoStock_form = ProductoStockForm()

    for productoStock in productoStock_from_db:
        formset.append(ProductoStockForm(productoStock))

    context_dict = {
        'productoStock_from_context': productoStock_from_db, 
        'productoStock_form': productoStock_form,
        'formset': formset
    }

    if request.method == 'POST':
        form = ProductoStockForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'productoStock.html', context_dict)
        else:
            print(form.errors)

    return render(request, 'productoStock.html', context_dict)

