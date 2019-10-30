from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', productos, name='productos'),
    path('agregar/', agregar, name='agregar'),
    path('signup/', login, name='signup'),
    path('contact/', contact, name='contact'),
    path('enviado/', enviado, name='enviado'),
    path('cerrarsesion/', cerrarsesion, name='cerrarsesion'),
    path('carrito/', carrito, name='carrito'),
    url(r'productos/(?P<id_producto>\d+)$', producto_detalle, name='producto_detalle'),
    url(r'carrito/(?P<name>\w+)/(?P<id_producto>\d+)', agrega_carrito, name='agrega_carrito'),
    url(r'ficha/(?P<name>\w+)/(?P<id_producto>\d+)',ficha, name='agrega_reseña'),
]
