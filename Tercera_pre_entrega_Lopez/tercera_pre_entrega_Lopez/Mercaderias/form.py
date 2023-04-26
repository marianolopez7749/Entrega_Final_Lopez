from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar, ImagenProducto
from django.db import models

class AltaProveedor(forms.Form):
    razon_social= forms.CharField(max_length=40)
    titular= forms.CharField(max_length=40)
    Cuit= forms.IntegerField()
    domicilio= forms.CharField(max_length=40)
    email= forms.EmailField()

   

class AltaProductos(forms.Form):
    nombre= forms.CharField(max_length=40)
    descripcion= forms.CharField(max_length=40)
    codigo= forms.IntegerField()
    Cuit= forms.IntegerField()
    imagen = forms.ImageField()

    
class AltaCompras(forms.Form):
    orden_compra = forms.IntegerField()
    factura_compra = forms.CharField(max_length=40)
    Cuit = forms.IntegerField()
    codigo = forms.IntegerField()
    cantidad = forms.IntegerField()

    

class UserEditForm(UserChangeForm):
   
    password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
      model=User
      fields=('email', 'first_name', 'last_name')

    def clean_password2(self):

      print(self.cleaned_data)

      password2 = self.cleaned_data["password2"]
      if password2 != self.cleaned_data["password1"]:
        raise forms.ValidationError("Las contraseñas no coinciden!")
      return password2
  

class AvatarFormulario(forms.ModelForm):
   class Meta:
      model=Avatar
      fields=('imagen',)  


class ImagenProductoFormulario(forms.ModelForm):
   class Meta:
      model=ImagenProducto
      fields=('imagen',) 