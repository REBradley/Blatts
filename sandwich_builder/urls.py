from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sandwich_index, name='sandwich_index'),
    
    url(r'^(?P<base>\w+)/$', views.burger_constructor, name='burger_constructor'),
    
    url(r'^add_sandwich/(?P<base>\w+)/$', views.add_sandwich, name='add_sandwich'),
]