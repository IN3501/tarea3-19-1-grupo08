from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UsuarioRegistrado(models.Model):
    usuario = models.ForeignKey(User,models.CASCADE)
    nacimiento = models.DateField()
    genero = models.CharField(max_length=140)

class Productos(models.Model):
    nombre = models.CharField(max_length=140)
    marca = models.CharField(max_length=140)
    precio = models.CharField(max_length=140)
    descripcion = models.CharField(max_length=140)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=140,default="")
    imagen = models.ImageField(upload_to='static/imagenes',blank=True)

class Reseña(models.Model):
    usuario = models.ForeignKey(User, models.SET_NULL, null=True , blank=True)
    producto = models.ForeignKey(Productos, models.SET_NULL, null=True, blank=True)
    descripcion = models.CharField(max_length=1000)
    puntuacion = models.IntegerField(default=0)

class Carrito(models.Model):
    usua = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    prod = models.ForeignKey(Productos, models.SET_NULL, null=True, blank=True)

class Contacto(models.Model):
    nombre = models.CharField(max_length=140)
    rut = models.CharField(max_length=140)
    telefono = models.CharField(max_length=140)
    correo = models.EmailField()
    comentario = models.CharField(max_length=1000)