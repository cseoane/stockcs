from django.conf.urls import url
from stockapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'depositos', views.depositos, name='index'),
    url(r'productos', views.productos, name='index'),
    url(r'variantes', views.variantes, name='index'),
    url(r'productoSubTipos', views.productoSubTipos, name='index'),
    url(r'productoTipos', views.productoTipos, name='index'),
    url(r'etiquetas', views.etiquetas, name='index'),
    url(r'etiquetaTipos', views.etiquetaTipos, name='index'),
    url(r'productoStock', views.productoStock, name='index'),
    ]
