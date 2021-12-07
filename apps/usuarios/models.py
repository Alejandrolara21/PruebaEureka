from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    #Usuario
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    registrado = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.usuario.username