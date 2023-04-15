from django.contrib import admin
from .models import Productos, Proveedores, Compras, Stock

# Register your models here.
admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(Compras)
admin.site.register(Stock)
