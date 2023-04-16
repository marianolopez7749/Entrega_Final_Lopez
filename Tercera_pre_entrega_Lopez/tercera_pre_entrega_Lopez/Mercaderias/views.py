from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from Mercaderias.models import *
from Mercaderias.form import *




# Create your views here.

def inicio(self):
    return render(self, "mercaderias.html")

def productos(self):
    return render(self, "productos.html")

def proveedores(self):
    return render(self, "proveedores.html")

def compras(self):
    return render(self, "compras.html")

def stock(self):
    return render(self, "stock.html")


def altaProveedor(request):
    
    if request.method == 'POST':
      altaFormulario = AltaProveedor(request.POST)
      print(altaFormulario)

      if altaFormulario.is_valid():
          data = altaFormulario.cleaned_data
          proveedores = Proveedores(razon_social=data['razon_social'], titular=data['titular'], Cuit=data['Cuit'], domicilio=data['domicilio'], email=data['email'])
          proveedores.save()
          return render(request, "mercaderias.html")
      else:
          return render(request, "mercaderias.html", {"mensaje": "Formulario invalido"})
    else:
      altaFormulario = AltaProveedor()
      return render(request, "altaProveedor.html", {"altaFormulario": altaFormulario})
        

def altaProducto(request):
    
    if request.method == 'POST':
      altaFormulario = AltaProductos(request.POST)
      print(altaFormulario)

      if altaFormulario.is_valid():
          data = altaFormulario.cleaned_data
          productos = Productos(nombre=data['nombre'], descripcion=data['descripcion'], codigo=data['codigo'], Cuit=data['Cuit'])
          productos.save()
          return render(request, "mercaderias.html")
      else:
          return render(request, "mercaderias.html", {"mensaje": "Formulario invalido"})
    else:
      altaFormulario = AltaProductos()
      return render(request, "altaProducto.html", {"altaFormulario": altaFormulario})
        

def altaCompra(request):
    
    if request.method == 'POST':
      altaFormulario = AltaCompras(request.POST)
      print(altaFormulario)

      if altaFormulario.is_valid():
          data = altaFormulario.cleaned_data
          compra = Compras(orden_compra=data['orden_compra'],
                      factura_compra=data['factura_compra'], Cuit=data['Cuit'], 
                      codigo=data['codigo'],cantidad=data['cantidad'])
          compra.save()
          return render(request, "mercaderias.html")
      else:
          return render(request, "mercaderias.html", {"mensaje": "Formulario invalido"})
    else:
      altaFormulario = AltaCompras()
      return render(request, "altaCompra.html", {"altaFormulario": altaFormulario})
    
def busquedaProducto(request):

    return render(request, "busquedaProducto.html")  

def buscar(request):
    
    if request.GET["codigo"]:
        codigo = request.GET["codigo"]
        productos = Productos.objects.filter(codigo=codigo)
        return render(request, "resultadoBusquedaProducto.html", {"codigo": productos})
    else:
        return HttpResponse(f'No enviaste info')
         


def busquedaCompra(request):

    return render(request, "busquedaCompra.html")  

def buscarCompra(request):
    
    if request.GET["orden_compra"]:
        orden_compra = request.GET["orden_compra"]
        compra = Compras.objects.filter(orden_compra=orden_compra)
        return render(request, "resultadoBusquedaCompra.html", {"orden_compra": compra})
    else:
        return HttpResponse(f'No enviaste info')
         
def busquedaProveedor(request):

    return render(request, "busquedaProveedor.html")  

def buscarProveedor(request):
    
    if request.GET["cuit"]:
        cuit = request.GET["cuit"]
        proveedor = Proveedores.objects.filter(Cuit=cuit)
        return render(request, "resultadoBusquedaProveedor.html", {"cuit": proveedor})
    else:
        return HttpResponse(f'No enviaste info')

