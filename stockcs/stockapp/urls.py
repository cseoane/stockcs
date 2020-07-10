from django.conf.urls import url
from stockapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    ]
