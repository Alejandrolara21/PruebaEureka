from django.contrib import admin

# Modelos
from apps.productos.models import Producto 

@admin.register(Producto)
class PerfilProducto(admin.ModelAdmin):

    list_display = ('pk','nombre','imagen','subcategoria','registrado')
