from django.http import response
from django.shortcuts import render , get_object_or_404,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .forms import IniciarSesion,Register,Agregar
from .models import *

# Create your views here.
def cerrarsesion(request):
	do_logout(request)
	Carrito.objects.all().delete()
	return render(request, 'productos.html',obtener_contexto())


def productos(request):
	return render(request, 'productos.html',obtener_contexto())

def agregar(request):

	if request.method == 'POST':
		nombre = request.POST['nombre']
		marca = request.POST['marca']
		precio = request.POST['precio']
		descripcion = request.POST['descripcion']
		stock = request.POST['stock']
		categoria = request.POST['categoria']

		imagen = request.FILES['imagen']
		producto = Productos(nombre=nombre,marca=marca,precio=precio,descripcion=descripcion,stock=stock,categoria=categoria,imagen=imagen)

		producto.save()
		return render(request, 'enviado.html',obtener_contexto())

	return render(request, 'agregar.html')

def login(request):
	if request.method == 'POST':
		login_form = IniciarSesion(request.POST)
		if login_form.is_valid():
			user = login_form.cleaned_data['user']
			password = login_form.cleaned_data['password']
			user = authenticate(username=user, password=password)
			if user is not None:
				do_login(request, user)
				return render(request, 'productos.html',obtener_contexto())
		register_form = Register(request.POST)
		if register_form.is_valid():
			email = register_form.cleaned_data['email']
			username = register_form.cleaned_data['username']
			#fecha = register_form.cleaned_data['fecha']
			password = register_form.cleaned_data['password']
			#genero = register_form.cleaned_data['exampleRadios']
			try:
				user = User.objects.create_user(username=email, email=email, first_name=username, password=password)
			except:
				return render(request, 'signup.html')

			user.save()
			if user is not None:
				do_login(request, user)
				return render(request, 'enviado.html')
	return render(request, 'signup.html')

def contact(request):
	return render(request,'contact.html')

def enviado(request):
	return render(request,'enviado.html')

def ficha(request,name,id_producto):
	if request.method=='POST':
		print("funciono")
		descr=request.POST['descripcion']
		punt=request.POST.get('rating')
		us=User.objects.get(first_name=name)
		prod=Productos.objects.get(id=id_producto)
		res=Reseña(usuario=us,producto=prod,descripcion=descr,puntuacion=punt)
		res.save()
		return render(request,'enviado.html')
	producto = get_object_or_404(Productos, id=id_producto)
	print("nofunciono")
	return render(request,'ficha.html',{'producto':producto})

def carrito(request):
	return render(request,'carrito.html',obtener_contexto())

def producto_detalle(request, id_producto):
	producto= get_object_or_404(Productos,id=id_producto)
	resenias=Reseña.objects.filter(producto_id=id_producto)
	contexto={}
	contexto['producto']=producto
	contexto['resenias']=resenias
	contexto['cantres']=len(resenias)
	return render(request,'ficha.html',contexto)

def agrega_carrito(request,name,id_producto):
	us=User.objects.get(first_name=name)
	prod=Productos.objects.get(id=id_producto)
	carro=Carrito(usua=us,prod=prod)
	carro.save()
	return render(request,'productos.html',obtener_contexto())


def obtener_contexto():
	productos=Productos.objects.all()
	contexto={}
	contexto['productos']=productos
	categorias=Productos.objects.values('categoria').distinct()
	contexto['categoria']=categorias
	marcas = Productos.objects.values('marca').distinct()
	contexto['marca'] = marcas
	carro=Carrito.objects.all()
	contexto['carro']=carro
	cantcarro=carro.count()
	contexto['cantcarro']=cantcarro
	return contexto
