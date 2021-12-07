from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre = models.CharField(max_length=100)
    registrado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre