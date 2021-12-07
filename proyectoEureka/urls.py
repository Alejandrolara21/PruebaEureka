"""proyectoEureka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from os import name
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from proyectoEureka import views as local_views
from apps.productos import views as productos_views
from apps.usuarios import views as usuarios_views
from apps.categorias import views as categorias_views
from apps.subcategorias import views as subcategorias_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/login/',usuarios_views.login_view,name="login_usuario"),
    path('usuarios/logout/',usuarios_views.logout_view,name="logout_usuario"),
    path('usuarios/signup/',usuarios_views.signup_view,name="signup_usuario"),
    path('',categorias_views.inicio_view,name="inicio"),

    #Menu Categoria
    path('categoria/crear/',categorias_views.crear_view,name="crear_categoria"),
    path('categoria/listado/',categorias_views.listado_view,name="listado_categoria"),
    path('categoria/editar/<int:pk>/',categorias_views.editar_view,name="editar_categoria"),
    path('categoria/eliminar/<int:pk>/',categorias_views.eliminar_view,name="eliminar_categoria"),
    path('categoria/listadoJson/',categorias_views.listadoJson_view,name="listadoJson_categoria"),

    #Menu Subcategoria
    path('subcategoria/crear/',subcategorias_views.crear_view,name="crear_subcategoria"),
    path('subcategoria/listado/',subcategorias_views.listado_view,name="listado_subcategoria"),
    path('subcategoria/editar/<int:pk>/',subcategorias_views.editar_view,name="editar_subcategoria"),
    path('subcategoria/eliminar/<int:pk>/',subcategorias_views.eliminar_view,name="eliminar_subcategoria"),
    path('subcategoria/listadoJson/',subcategorias_views.listadoJson_view,name="listadoJson_subcategoria"),

    #Menu Producto
    path('producto/crear/',productos_views.crear_view,name="crear_producto"),
    path('producto/listado/',productos_views.listado_view,name="listado_producto"),
    path('producto/editar/<int:pk>/',productos_views.editar_view,name="editar_producto"),
    path('producto/eliminar/<int:pk>/',productos_views.eliminar_view,name="eliminar_producto"),
    path('producto/listadoJson/',productos_views.listadoJson_view,name="listadoJson_producto"),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
