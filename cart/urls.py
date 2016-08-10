from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^remove/(?P<pk>[0-9]+)/$', views.remove_from_cart, name='remove_from_cart'),
    
    url(r'^show/$', views.show_cart, name='show_cart'),
]