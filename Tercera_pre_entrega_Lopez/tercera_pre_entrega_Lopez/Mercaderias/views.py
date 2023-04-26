from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from Mercaderias.models import *
from Mercaderias.form import *

# Create your views here.

def inicio(self):

    try:
      avatar = Avatar.objects.get(user=self.user.id)
      return render(self, 'mercaderias.html', {'url': avatar.imagen.url})
    except:
      return render(self, "mercaderias.html")

def productos(self):

    try:
      avatar = Avatar.objects.get(user=self.user.id)
      return render(self, 'productos.html', {'url': avatar.imagen.url})
    except:
      return render(self, "productos.html")
    

def proveedores(self):

    try:
      avatar = Avatar.objects.get(user=self.user.id)
      return render(self, 'proveedores.html', {'url': avatar.imagen.url})
    except:
      return render(self, "proveedores.html")
    
def compras(self):

    try:
      avatar = Avatar.objects.get(user=self.user.id)
      return render(self, 'compras.html', {'url': avatar.imagen.url})
    except:
      return render(self, "compras.html")
    

def stock(self):

    try:
      avatar = Avatar.objects.get(user=self.user.id)
      return render(self, 'stock.html', {'url': avatar.imagen.url})
    except:
      return render(self, "stock.html")
    


        
@staff_member_required(login_url='/mercaderias/')
def altaCompra(request):
    
    if request.method == 'POST':
      altaFormulario = AltaCompras(request.POST)
      
      if altaFormulario.is_valid():
          data = altaFormulario.cleaned_data
          compra = Compras(orden_compra=data['orden_compra'],
                      factura_compra=data['factura_compra'], Cuit=data['Cuit'], 
                      codigo=data['codigo'],cantidad=data['cantidad'])
          compra.save()

          codigo = data['codigo']  
          

          if Stock.objects.get(codigo=codigo):
             stock = Stock.objects.get(codigo=codigo)
             
             stock.codigo = data['codigo']
             stock.cantidad+=data['cantidad']
             stock.save()  
          else:
             stock = Stock(codigo=data['codigo'],cantidad=data['cantidad'])
             stock.save()
            

          return render(request, "mercaderias.html")
      else:
          return render(request, "mercaderias.html", {"mensaje": "Formulario invalido"})
    else:
      altaFormulario = AltaCompras()
      return render(request, "altaCompra.html", {"altaFormulario": altaFormulario})
   
class ComprasList(ListView):
   
   model = Compras
   template_name = 'compraslist.html'
   context_object_name = 'compras'

class ComprasDetail(DetailView):
   
   model = Compras
   template_name = 'comprasdetail.html'
   context_object_name = 'compras'

class ComprasUpdate(LoginRequiredMixin,UpdateView):
   
   model = Compras
   template_name = 'comprasupdate.html'
   context_object_name = 'compras'
   fields = ('__all__')
   success_url = '/mercaderias/'

class ComprasDelete(LoginRequiredMixin,DeleteView):
   
   model = Compras
   template_name = 'comprasdelete.html'
   success_url = '/mercaderias/'



class ProveedorList(ListView):
   
   model = Proveedores
   template_name = 'proveedorlist.html'
   context_object_name = 'proveedores'

class ProveedorDetail(DetailView):
   
   model = Proveedores
   template_name = 'proveedordetail.html'
   context_object_name = 'proveedores'

class ProveedorCreate(LoginRequiredMixin, CreateView):
   
   model = Proveedores
   template_name = 'proveedorcreate.html'
   fields = ['razon_social', 'titular', 'Cuit', 'domicilio', 'email']
   success_url = '/mercaderias/'

class ProveedorUpdate(LoginRequiredMixin,UpdateView):
   
   model = Proveedores
   template_name = 'proveedorupdate.html'
   context_object_name = 'proveedores'
   fields = ('__all__')
   success_url = '/mercaderias/'

class ProveedorDelete(LoginRequiredMixin,DeleteView):
   
   model = Proveedores
   template_name = 'proveedordelete.html'
   success_url = '/mercaderias/'





class ProductosList(ListView):
   
    model = Productos
    template_name = 'productoslist.html'
    context_object_name = 'productos'



class ProductosDetail(DetailView):
   
   model = Productos
   template_name = 'productosdetail.html'
   context_object_name = 'productos'
   
   


class ProductosCreate(LoginRequiredMixin,CreateView):
   
   model = Productos
   template_name = 'productoscreate.html'
   fields = ('__all__')
   success_url = '/mercaderias/'


class ProductosUpdate(LoginRequiredMixin,UpdateView):
   
   model = Productos
   template_name = 'productosupdate.html'
   context_object_name = 'productos'
   fields = ('__all__')
   success_url = '/mercaderias/'

class ProductosDelete(LoginRequiredMixin,DeleteView):
   
   model = Productos
   template_name = 'productosdelete.html'
   success_url = '/mercaderias/'

#class Agregarimagenproducto(LoginRequiredMixin,CreateView):
   
#   model = ImagenProducto
#   template_name = 'cargaimagen.html'
#   fields = ('__all__')
#   success_url = '/mercaderias/'

@staff_member_required(login_url='/mercaderias/')
def altaProducto(request):
    
    if request.method == 'POST':
      altaFormulario = AltaProductos(request.POST)
      
      if altaFormulario.is_valid():
          data = altaFormulario.cleaned_data
          producto = Productos(orden_compra=data['orden_compra'],
                      factura_compra=data['factura_compra'], Cuit=data['Cuit'], 
                      codigo=data['codigo'],cantidad=data['cantidad'],
                      imagen=data['imagen'])
          producto.save()

          return render(request, "mercaderias.html")
      else:
          return render(request, "mercaderias.html", {"mensaje": "Formulario invalido"})
    else:
      altaFormulario = AltaProductos()
      return render(request, "productoscreate.html", {"altaFormulario": altaFormulario})


def agregar_imagen_producto(request):
   
      if request.method == 'POST':
       formulario = ImagenProductoFormulario(request.POST, request.FILES)

       if formulario.is_valid():
        
          data = formulario.cleaned_data
          imagenprod = ImagenProducto(codigo=request.codigo, imagen=data["imagen"])
          imagenprod.save()

          return render(request, 'mercaderias.html')
         
       else:
          return render(request, "mercaderias.html", {"mensaje": "Carga inválida"})
  
      else:
        formulario = ImagenProductoFormulario()
        return render(request, "cargaimagen.html", {"formulario": formulario})





class StockList(ListView):
   
   model = Stock
   template_name = 'stocklist.html'
   context_object_name = 'stocks'

class StockDetail(DetailView):
   
   model = Stock
   template_name = 'stockdetail.html'
   context_object_name = 'stocks'

class StockUpdate(LoginRequiredMixin,UpdateView):
   
   model = Stock
   template_name = 'stockupdate.html'
   context_object_name = 'stocks'
   fields = ('__all__')
   success_url = '/mercaderias/'

class StockDelete(LoginRequiredMixin,DeleteView):
   
   model = Stock
   template_name = 'stockdelete.html'
   success_url = '/mercaderias/'




def registro_usuario(request):
   
  if request.method == 'POST':
     formulario = UserCreationForm(request.POST)

     if formulario.is_valid():
       data = formulario.cleaned_data
       username = data["username"]
       formulario.save()
       return render(request, 'mercaderias.html', {"mensaje": f'Usuario {username} creado!'})
     else:
       return render(request, "mercaderias.html", {"mensaje": "Formulario invalido"})
  else:
     formulario = UserCreationForm()
     return render(request, "registro.html", {"formulario": formulario}) 


def loginView(request):
   
  if request.method == 'POST':
    
    formulario = AuthenticationForm(request, data=request.POST)

    if formulario.is_valid():
       
      data = formulario.cleaned_data
      usuario = data["username"]
      psw = data["password"]

      user = authenticate(username=usuario, password=psw)

      if user:
          login(request, user)
          return render(request, 'mercaderias.html', {"mensaje": f'Bienvenido {usuario}'})
      else:
          return render(request, "mercaderias.html", {"mensaje": "Datos erróneos"})
    else:
        return render(request, "mercaderias.html", {"mensaje": "Datos erróneos"})
     
  else:
     formulario = AuthenticationForm()
     return render(request, "login.html", {"formulario": formulario})  
  
 

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':
      
      formulario = UserEditForm(request.POST, instance=request.user)

      if formulario.is_valid():
          data = formulario.cleaned_data
          
          usuario.email = data['email']
          usuario.first_name = data['first_name']
          usuario.last_name = data['last_name']
          usuario.set_password(data["password1"])
          usuario.save()
          
          return render(request, "mercaderias.html", {"mensaje": "Datos actualizados!"})
    
      else:
          return render(request, "mercaderias.html", {"formulario": formulario})
    else:
      formulario = UserEditForm(instance=request.user)
      return render(request, "editarPerfil.html", {"formulario": formulario})



@login_required
def agregar_avatar(request):
   
  if request.method == 'POST':
      formulario = AvatarFormulario(request.POST, request.FILES)

      if formulario.is_valid():

        data = formulario.cleaned_data
        avatar = Avatar(user=request.user, imagen=data["imagen"])
        avatar.save()

        return render(request, 'mercaderias.html', {"mensaje": f'Avatar agregado!'})
         
      else:
        return render(request, "mercaderias.html", {"mensaje": "Formulario invalido"})
  
  else:
      formulario = AvatarFormulario()
      return render(request, "agregaravatar.html", {"formulario": formulario})
  


