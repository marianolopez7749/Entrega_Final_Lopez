from django.contrib import admin
from django.urls import path, include
from Mercaderias.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('productos/', productos, name="productos"),
    path('proveedores/', proveedores, name="proveedores"),
    path('compras/', compras, name="compras"),
    path('stock/', stock, name="stock"),
    path('altaProveedor/', altaProveedor, name="altaProveedor"),
    path('altaProducto/', altaProducto, name="altaProducto"),
    path('altaCompra/', altaCompra, name="altaCompra"),
    path('busquedaProducto/', busquedaProducto, name="busquedaProducto"),
    path('buscar/', buscar, name="buscar"),
    path('busquedaProveedor/', busquedaProveedor, name="busquedaProveedor"),
    path('buscarProveedor/', buscarProveedor, name="buscarProveedor"),
]
 
    
