from django.conf.urls import url
from stockapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'productos', views.productos, name='index'),
    url(r'variantes', views.variantes, name='index'),
    ]
