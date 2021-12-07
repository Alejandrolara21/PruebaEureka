from django.contrib import admin
from django.contrib.auth.models import User

# Modelos
from apps.subcategorias.models import Subcategoria

@admin.register(Subcategoria)
class PerfilSubcategoria(admin.ModelAdmin):

    list_display = ('pk','nombre','descripcion','categoria','registrado')

