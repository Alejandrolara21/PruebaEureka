from django.contrib import admin

# Modelos
from apps.categorias.models import Categoria

# Register your models here.
@admin.register(Categoria)
class PerfilCategoria(admin.ModelAdmin):
    #Categoria
    list_display = ('pk','nombre','registrado')