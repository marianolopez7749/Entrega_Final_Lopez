"""tercera_pre_entrega_Lopez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('busquedaCompra/', busquedaCompra, name="busquedaCompra"),
    path('buscarCompra/', buscarCompra, name="buscarCompra"),
]
