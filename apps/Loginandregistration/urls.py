from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^wish_item/(?P<id>\d+)$', views.show, name='show'),
    url(r'^wish_item/createw', views.createw, name='createw'),
    url(r'^wish_item/add', views.add, name='add'),
    url(r'^(?P<id>\d+)/remove', views.remove, name='remove'),
    url(r'^(?P<id>\d+)/addfrom', views.addfrom, name='addfrom')





]