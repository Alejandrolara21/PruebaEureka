from django.db import models

from apps.subcategorias.models import Subcategoria

class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(blank=True,decimal_places=2,max_digits=10)
    cantidad = models.IntegerField(blank=True)
    imagen = models.ImageField(upload_to='productos/imagenes')
    registrado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    subcategoria = models.ForeignKey(Subcategoria,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre