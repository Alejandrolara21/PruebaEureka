from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.http import HttpResponse
import json
import os

from apps.categorias.models import Categoria
from apps.subcategorias.models import Subcategoria
from apps.productos.models import Producto

@login_required
def inicio_view(request):
    return render(request,'CRUD/index.html')

@login_required
def crear_view(request):
    data={}

    if request.method == 'POST':
        nombre = request.POST['nombre']
        errores = []

        if(len(nombre)> 100):
            errores.append("Nombre demasiado largo")

        if(len(errores) > 0):
            data={
                'nombre':nombre,
                'error': errores
            }
            return render(request,'CRUD/categoria/crear-categoria.html',data)
        
        try:
            categoria = Categoria()
            categoria.nombre = nombre
            categoria.save()
            return redirect('listado_categoria')
        except:
            data={
                'errorDB': "Error en la base de datos"
            }
    return render(request,'CRUD/categoria/crear-categoria.html',data)


@login_required
def listado_view(request):
    try:
        categorias=Categoria.objects.all()
        data={
            'categorias':categorias
        }
    except:
        data={
            'errorDB': "Error en la base de datos"
        }
    return render(request,'CRUD/categoria/listado-categoria.html',data)

@login_required
def editar_view(request,pk):
    try:
        data={
            'categoria':Categoria.objects.get(pk=pk),
        }
    except:
        data={
            'errorDB': "Error en la base de datos"
        }

    if request.method == 'POST':
        nombre = request.POST['nombre']
        errores = []

        if(len(nombre)> 100):
            errores.append("Nombre demasiado largo")

        if(len(errores) > 0):
            try:
                data={
                    'categoria':Categoria.objects.get(pk=pk),
                    'error': errores
                }
            except:
                data={
                    'errorDB': "Error en la base de datos"
                }
            return render(request,'CRUD/categoria/editar-categoria.html',data)

        try:
            categoria = Categoria.objects.get(pk=pk)
            categoria.nombre = nombre
            categoria.save()
            return redirect('listado_categoria')
        except:
            data={
                'errorDB': "Error en la base de datos"
            }
    return render(request,'CRUD/categoria/editar-categoria.html',data)


@login_required
def eliminar_view(request,pk):

    try:
        categoria = Categoria.objects.get(pk=pk)
        subcategorias = Subcategoria.objects.filter(categoria=categoria)
        for subcategoria in subcategorias:
            productos = Producto.objects.filter(subcategoria=subcategoria)
            for producto in productos:
                if(producto.imagen):
                    file_path = f'{settings.MEDIA_ROOT}/{producto.imagen}'
                    if os.path.isfile(file_path):
                        os.remove(file_path)
        categoria.delete()
        data ={
            'status':'ok',
            'message': 'Categoria eliminada correctamente'
        }

    except:
        data={
            'status': 'error',
            'message': 'Error en la base de datos'
        }

    
    return HttpResponse(json.dumps(data),content_type='application/json')


@login_required
def listadoJson_view(request):
    try:
        categorias = Categoria.objects.all()
        jsonData = {}
        jsonData['categorias'] = []

        for categoria in categorias:
            arreglo_json = {
                'id': f'{categoria.id}',
                'nombre': f'{categoria.nombre}',
            }

            jsonData['categorias'].append(arreglo_json)

    except:
        jsonData={
            'status': 'error',
            'message': 'Error en la base de datos'
        }

    
    return HttpResponse(json.dumps(jsonData),content_type='application/json')