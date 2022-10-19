from django.urls import path
from ControlStock import views

app_name = 'ControlStock'

urlpatterns = [
    path('', views.login_request, name="Login"),
    path('logout', views.logout_request, name="Logout"),
    path('registro', views.registro, name="Registro" ),

    path('inicio', views.Index, name="Index"),
    path('productos', views.ListadoProdructos, name="Productos"),
    path('productosModificar/<id_producto>/', views.ModificarProductos, name="Modificar"),
    path('productosEliminar/<id_producto>/', views.Eliminar, name="Eliminar"),
    path('productosNuevo', views.NuevoProducto, name="NuevoProducto"),
    path('productosSumar', views.SumarProducto, name="Sumar"),
    path('agregar/<id_producto>/', views.AgregarProducto, name="Agregar"),
    path('productosRestar', views.RestarProducto, name="Restar"),
    path('descontar/<id_producto>/', views.DescontarProducto, name="Descontar"),
]