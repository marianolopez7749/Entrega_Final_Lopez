from django import forms

class AltaProveedor(forms.Form):
    razon_social= forms.CharField(max_length=40)
    titular= forms.CharField(max_length=40)
    Cuit= forms.IntegerField()
    domicilio= forms.CharField(max_length=40)
    email= forms.EmailField()

    def __str__(self):
       return f'{self.razon_social} - {self.titular} - {self.Cuit} - {self.domicilio} - {self.email}'

class AltaProductos(forms.Form):
    nombre= forms.CharField(max_length=40)
    descripcion= forms.CharField(max_length=40)
    codigo= forms.IntegerField()
    Cuit= forms.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.descripcion} - {self.codigo} - {self.Cuit}'

class AltaCompras(forms.Form):
    orden_compra = forms.IntegerField()
    factura_compra = forms.CharField(max_length=40)
    Cuit = forms.IntegerField()
    codigo = forms.IntegerField()
    cantidad = forms.IntegerField()

    def __str__(self):
       return f'{self.orden_compra} - {self.factura_compra} - {self.Cuit} - {self.codigo} - {self.cantidad}'

