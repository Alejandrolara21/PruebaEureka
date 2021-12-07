from django.db import models

from apps.categorias.models import Categoria
# Create your models here.
class Subcategoria(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    registrado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre