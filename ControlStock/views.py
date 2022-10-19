from django.shortcuts import render, redirect
from ControlStock.models import Productos
from ControlStock.forms import productosForm, FormularioSuma, FormularioResta
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#   REGISTRO USUARIOS
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f"Nueva cuenta creada: {nombre_usuario}")
            login(request, usuario)
            messages.info(request, f"Has sido registrado como {nombre_usuario}")
            return redirect("ControlStock:Index")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = UserCreationForm
    return render(request, 'cuentas/register.html', {'form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                messages.info(request, f"Estas logeado como {usuario}")
                return redirect('ControlStock:Index')
            else:
                messages.error(request, "Usuario o contraseña equivocada")
        else:
            messages.error(request, "Usario o contraseña equivocada")
    form = AuthenticationForm()
    return render(request, 'cuentas/login.html', {'form': form})
        

def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect("ControlStock:Login")

#   INICIO
@login_required(login_url='cuentas/login.html') 
def Index(request):
    return render (request, 'index.html')

#   LISTADO DE PRODUCTOS
@login_required(login_url='cuentas/login.html')
def ListadoProdructos(request):
    resultado = Productos.objects.all()
    return render(request, 'productosList.html',{'productos':resultado})

#   MODICICAR DATOS DE PRODUCTOS
@login_required(login_url='cuentas/login.html')
def ModificarProductos(request, id_producto):
    resultado = Productos.objects.get(id_producto=id_producto)
    data = {
        'form' : productosForm(instance = resultado)
    }

    if request.method == 'POST':
        form = productosForm (data = request.POST, instance = resultado)
        if form.is_valid():
            form.save()
            return redirect('ControlStock:Productos')

    return render (request, 'productosModificar.html', data)

#   ELIMINAR PRODUCTOS
@login_required(login_url='cuentas/login.html')
def Eliminar(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)

    if request.method == 'POST':
        producto.delete()
        return redirect('ControlStock:Productos')
    return render(request, 'productosDelete.html', {'producto':producto})

#   AGREGAR NUEVO PRODUCTO
@login_required(login_url='cuentas/login.html')
def NuevoProducto(request):
    if request.method == 'POST':
        form = productosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ControlStock:Productos')
    else:
        form = productosForm()
    return render(request, 'productosAdd.html', {'form':form})

#   SUMAR CANTIDAD
@login_required(login_url='cuentas/login.html')
def SumarProducto(request):
    resultado = Productos.objects.all()
    return render(request, 'productosSumar.html',{'productos':resultado})


@login_required(login_url='cuentas/login.html')
def AgregarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    data = {
        'form': FormularioSuma()
    }
    if request.method == 'POST':
        form = FormularioSuma(request.POST)
        if form.is_valid():
            suma = form.cleaned_data['suma']
            producto.cantidad += suma
            producto.save()
            return redirect('ControlStock:Productos')
    return render(request, 'productosAgregar.html', data)

#   RESTAR CANTIDAD
@login_required(login_url='cuentas/login.html')
def RestarProducto(request):
    resultado = Productos.objects.all()
    return render(request, 'productosRestar.html',{'productos':resultado})


@login_required(login_url='cuentas/login.html')
def DescontarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    data = {
        'form': FormularioResta()
    }
    if request.method == 'POST':
        form = FormularioResta(request.POST)
        if form.is_valid():
            resta = form.cleaned_data['resta']
            producto.cantidad -= resta
            producto.save()
            return redirect('ControlStock:Restar')
    return render(request, 'productosDescontar.html', data)

