from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import fields

# Modelos
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario

@admin.register(Usuario)
class PerfilAdministrador(admin.ModelAdmin):
    #Usuario
    list_display = ('pk','usuario','registrado')
    search_fields =('usuario__email','usuario__username')
    
    fieldsets = (
        ('Perfil', {
            'fields': ('usuario',)
        }),
        ('Datos', {
            'fields': ('registrado',)
        })
    )

    readonly_fields = ('registrado',)

class PerfilInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Usuarios'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)