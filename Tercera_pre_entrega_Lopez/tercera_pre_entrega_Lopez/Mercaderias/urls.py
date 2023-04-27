from django.urls import path
from django.contrib.auth.views import LogoutView
from Mercaderias.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos, name="productos"),
    path('proveedores/', proveedores, name="proveedores"),
    path('compras/', compras, name="compras"),
    path('stock/', stock, name="stock"),
    path('altaCompra/', altaCompra, name="altaCompra"),
    path('proveedorlist/', ProveedorList.as_view(), name="proveedorlist"),
    path('eliminaproveedor/<pk>/', ProveedorDelete.as_view(), name="eliminaproveedor"),
    path('modificaproveedor/<pk>/', ProveedorUpdate.as_view(), name="modificaproveedor"),
    path('creaproveedor/', ProveedorCreate.as_view(), name="creaproveedor"),
    path('consultaproveedor/<pk>/', ProveedorDetail.as_view(), name="consultaproveedor"),
    path('compraslist/', ComprasList.as_view(), name="compraslist"),
    path('eliminacompras/<pk>/', ComprasDelete.as_view(), name="eliminacompras"),
    path('modificacompras/<pk>/', ComprasUpdate.as_view(), name="modificacompras"),
    path('consultacompras/<pk>/', ComprasDetail.as_view(), name="consultacompras"),
    path('productoslist/', ProductosList.as_view(), name="productoslist"),
    path('eliminaproductos/<pk>/', ProductosDelete.as_view(), name="eliminaproductos"),
    path('modificaproductos/<pk>/', ProductosUpdate.as_view(), name="modificaproductos"),
    path('creaproductos/', ProductosCreate.as_view(), name="creaproductos"),
    path('consultaproductos/<pk>/', ProductosDetail.as_view(), name="consultaproductos"),
    path('stocklist/', StockList.as_view(), name="stocklist"),
    path('eliminastock/<pk>/', StockDelete.as_view(), name="eliminastock"),
    path('modificastock/<pk>/', StockUpdate.as_view(), name="modificastock"),
    path('consultastock/<pk>/', StockDetail.as_view(), name="consultastock"),
    path('login/', loginView, name="login"),
    path('registro/', registro_usuario, name="registro"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('editarperfil/', editar_perfil, name="editarperfil"),
    path('agregaravatar/', agregar_avatar, name="agregaravatar"),
    path('cargaimagen/', agregar_imagen_producto , name="cargaimagen"),
    path('acerca/', acerca , name="acerca"),
]

 
    
