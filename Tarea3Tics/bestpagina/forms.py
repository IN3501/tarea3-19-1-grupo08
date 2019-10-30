from django import forms


class IniciarSesion(forms.Form):
    user = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)




class Register(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=140)
    password = forms.CharField(widget=forms.PasswordInput)
    fecha = forms.DateField()
    #genero = forms.CharField(max_length=140)

class Agregar(forms.Form):
    nombre = forms.CharField(max_length=140)
    marca = forms.CharField(max_length=140)
    precio = forms.CharField(max_length=140)
    descripcion = forms.CharField(max_length=140)
    stock = forms.IntegerField()
    categoria = forms.CharField(max_length=140)
    imagen = forms.FileField()
    #imagen = forms.ImageField(upload_to='static/imagenes', blank=True)