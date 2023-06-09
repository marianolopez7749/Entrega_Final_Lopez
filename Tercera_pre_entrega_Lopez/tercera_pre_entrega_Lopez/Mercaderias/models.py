from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proveedores(models.Model):
    razon_social=models.CharField(max_length=40)
    titular=models.CharField(max_length=40)
    Cuit=models.IntegerField()
    domicilio=models.CharField(max_length=40)
    email=models.EmailField()

    def __str__(self):
       return f'Razón Social: {self.razon_social} - Titular: {self.titular} - CUIT: {self.Cuit} - Domicilio: {self.domicilio} - Email: {self.email}'


class Productos(models.Model):
    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=40)
    codigo=models.IntegerField()
    Cuit=models.IntegerField()
    imagen = models.ImageField(upload_to='imagenproductos', null=True, blank=True)
    
    def __str__(self):
       return f'Nombre: {self.nombre} - Descripcion: {self.descripcion} - Código: {self.codigo} - Cuit: {self.Cuit} - imagen: {self.imagen}' 


class Compras(models.Model):
    orden_compra=models.IntegerField()
    factura_compra=models.CharField(max_length=40)
    Cuit=models.IntegerField()
    codigo=models.IntegerField()
    cantidad=models.IntegerField()

    def __str__(self):
       return f'Orden de compra: {self.orden_compra} - Factura nro: {self.factura_compra} - Cuit: {self.Cuit} - Código: {self.codigo} - Cantidad: {self.cantidad}'


class Stock(models.Model):
    codigo=models.IntegerField()
    cantidad=models.IntegerField()

    def __str__(self):
       return f'Código: {self.codigo} - Cantidad: {self.cantidad}'
    

class Avatar(models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

  def __str__(self):
      return  f'{self.user} - {self.imagen}'

class ImagenProducto(models.Model):

  codigo = models.ForeignKey(Productos, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='imagenproductos', null=True, blank=True)

  def __str__(self):
      return  f'{self.codigo} - {self.imagen}'