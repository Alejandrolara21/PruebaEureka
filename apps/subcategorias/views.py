from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.http import HttpResponse
import json
import os

from apps.categorias.models import Categoria
from apps.subcategorias.models import Subcategoria
from apps.productos.models import Producto


@login_required
def crear_view(request):
    try:
        categorias = Categoria.objects.all()
        data ={
            'categorias': categorias
        }
    except:
        data={
            'categorias': {
                'nombre': "Error en la base de datos",
                'error': "12"
            }
        }

    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descr']
        idCategoria = request.POST['categoria']
        errores = []

        if(len(nombre)> 100):
            errores.append("Nombre demasiado largo")

        if(len(errores) > 0):
            data={
                'nombre':nombre,
                'descripcion': descripcion,
                'error': errores,
                'categorias': categorias
            }
            return render(request,'CRUD/subcategoria/crear-subcategoria.html',data)
        
        try:
            subcategoria = Subcategoria()
            categoria = Categoria.objects.get(pk=idCategoria)
            subcategoria.nombre = nombre
            subcategoria.descripcion = descripcion
            subcategoria.categoria = categoria
            subcategoria.save()
            return redirect('listado_subcategoria')
        except:
            data={
                'errorDB': "Error en la base de datos"
            }
    return render(request,'CRUD/subcategoria/crear-subcategoria.html',data)

@login_required
def listado_view(request):
    try:
        subcategorias=Subcategoria.objects.all()
        data = {
            'subcategorias':subcategorias
        }
    except:
        data={
            'errorDB': "Error en la base de datos"
        }
    return render(request,'CRUD/subcategoria/listado-subcategoria.html',data)

@login_required
def listadoCantProd_view(request):
    try:
        subcategorias = Subcategoria.objects.all()
        data = {}
        data['subcategorias'] = []

        for subcategoria in subcategorias:
            productos = Producto.objects.filter(subcategoria=subcategoria)
            arreglo_json = {
                'id': f'{subcategoria.id}',
                'nombre': f'{subcategoria.nombre}',
                'categoria': f'{subcategoria.categoria}',
                'productos':f'{len(productos)}'
            }

            data['subcategorias'].append(arreglo_json)
    except:
        data={
            'errorDB': "Error en la base de datos"
        }
    return render(request,'CRUD/subcategoria/listado-cantidad-productos.html',data)


@login_required
def editar_view(request,pk):
    try:
        categorias = Categoria.objects.all()
        data ={
            'subcategoria':Subcategoria.objects.get(pk=pk),
            'categorias': categorias
        }
    except:
        data={
            'categorias': {
                'nombre': "Error en la base de datos",
                'error': "12"
            }
        }

    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descr']
        idCategoria = request.POST['categoria']

        errores = []

        if(len(nombre)> 100):
            errores.append("Nombre demasiado largo")

        if(len(errores) > 0):
            try:
                categorias = Categoria.objects.all()
                data ={
                    'subcategoria':Subcategoria.objects.get(pk=pk),
                    'categorias': categorias,
                    'error':errores
                }
            except:
                data={
                    'errorDB': "Error en la base de datos"
                }
            return render(request,'CRUD/subcategoria/editar-subcategoria.html',data)

        try:
            subcategoria = Subcategoria.objects.get(pk=pk)
            categoria = Categoria.objects.get(pk=idCategoria)
            subcategoria.nombre = nombre
            subcategoria.descripcion = descripcion
            subcategoria.categoria = categoria
            subcategoria.save()
            return redirect('listado_subcategoria')
        except:
            data={
                'errorDB': "Error en la base de datos"
            }

    return render(request,'CRUD/subcategoria/editar-subcategoria.html',data)


@login_required
def eliminar_view(request,pk):
    try:
        subcategoria = Subcategoria.objects.get(pk=pk)
        productos = Producto.objects.filter(subcategoria=subcategoria)
        for producto in productos:
            if(producto.imagen):
                file_path = f'{settings.MEDIA_ROOT}/{producto.imagen}'
                if os.path.isfile(file_path):
                    os.remove(file_path)
        subcategoria.delete()
        data ={
            'status':'ok',
            'message': 'Subcategoria eliminada correctamente'
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
        subcategorias = Subcategoria.objects.all()
        jsonData = {}
        jsonData['subcategorias'] = []

        for subcategoria in subcategorias:

            arreglo_json = {
                'id': f'{subcategoria.id}',
                'nombre': f'{subcategoria.nombre}',
                'descripcion': f'{subcategoria.descripcion}',
                'categoria': f'{subcategoria.categoria}',
            }

            jsonData['subcategorias'].append(arreglo_json)

    except Exception as e:
        print(e)
        jsonData={
            'status': 'error',
            'message': 'Error en la base de datos'
        }

    
    return HttpResponse(json.dumps(jsonData),content_type='application/json')