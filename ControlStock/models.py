from django.db import models

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    fecha_vencimiento = models.DateField()
    observacion = models.CharField(max_length=200)

    class Meta():
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
