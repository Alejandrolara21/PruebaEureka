from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

import os
from django.http import HttpResponse
import json


from apps.productos.models import Producto
from apps.subcategorias.models import Subcategoria

@login_required
def crear_view(request):
    try:
        subcategorias = Subcategoria.objects.all()
        data ={
            'subcategorias': subcategorias
        }
    except:
        data={
            'subcategorias': {
                'nombre': "Error en la base de datos",
                'error': "12"
            }
        }

    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descr']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        idSubcategoria = request.POST['subcategoria']

        errores = []

        if(len(nombre)> 100):
            errores.append("Nombre demasiado largo")

        if(len(precio) > 10):
            errores.append("Numero no valido")

        if(len(errores) > 0):
            data={
                'nombre':nombre,
                'descripcion':descripcion,
                'precio':precio,
                'cantidad':cantidad,
                'subcategorias':subcategorias,
                'error': errores
            }
            return render(request,'CRUD/productos/crear-producto.html',data)

        try:
            producto = Producto()
            subcategoria = Subcategoria.objects.get(pk=idSubcategoria)
            producto.nombre = nombre
            producto.precio = precio
            producto.cantidad = cantidad
            producto.descripcion = descripcion
            if(request.FILES):
                imagen = request.FILES['imagen']
                producto.imagen = imagen
            producto.subcategoria = subcategoria

            producto.save()

            return redirect('listado_producto')
        except:
            data={
                'errorDB': "Error en la base de datos"
            }

    return render(request,'CRUD/productos/crear-producto.html',data)


@login_required
def listado_view(request):
    try:
        productos=Producto.objects.all()
        data ={
            'productos':productos
        }
    except:
        data={
            'errorDB': "Error en la base de datos"
        }
    return render(request,'CRUD/productos/listado-producto.html',data)

@login_required
def editar_view(request,pk):
    try:
        subcategorias = Subcategoria.objects.all()
        data={
            'subcategorias': subcategorias,
            'producto': Producto.objects.get(pk=pk)
        }
    except:
        data={
            'subcategorias': {
                'nombre': "Error en la base de datos",
                'error': "12"
            },
            'errorDB': "Error en la base de datos"
        }

    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descr']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        idSubcategoria = request.POST['subcategoria']

        subcategoria = Subcategoria.objects.get(pk=idSubcategoria)

        errores = []

        if(len(nombre)> 100):
            errores.append("Nombre demasiado largo")

        if(len(precio) > 10):
            errores.append("Numero no valido")

        if(len(errores) > 0):
            data={
                'nombre':nombre,
                'descripcion':descripcion,
                'precio':precio,
                'cantidad':cantidad,
                'subcategorias':subcategorias,
                'error': errores
            }
            return render(request,'CRUD/productos/crear-producto.html',data)

        try:
            producto = Producto.objects.get(pk=pk)
            if(request.FILES):
                file_path = f'{settings.MEDIA_ROOT}/{producto.imagen}'
                if os.path.isfile(file_path):
                    print("imagen encontrada")
                    os.remove(file_path)
                imagen = request.FILES['imagen']
                producto.imagen = imagen

            producto.nombre = nombre
            producto.precio = precio
            producto.cantidad = cantidad
            producto.descripcion = descripcion
            producto.subcategoria = subcategoria
            producto.save()
            return redirect('listado_producto')
        except:
            data={
                'errorDB': "Error en la base de datos"
            }

    return render(request,'CRUD/productos/editar-producto.html',data)

@login_required
def eliminar_view(request,pk):
    try:
        producto = Producto.objects.get(pk=pk)
        if(producto.imagen):
            file_path = f'{settings.MEDIA_ROOT}/{producto.imagen}'
            if os.path.isfile(file_path):
                print("imagen encontrada")
                os.remove(file_path)
        else:
            print("imagen no encontrada")
        producto.delete()
        data ={
            'status':'ok',
            'message': 'Producto eliminada correctamente'
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
        productos = Producto.objects.all()
        jsonData = {}
        jsonData['productos'] = []

        for producto in productos:

            arreglo_json = {
                'id': f'{producto.id}',
                'nombre': f'{producto.nombre}',
                'descripcion': f'{producto.descripcion}',
                'imagen': f'{producto.imagen}',
                'precio': f'{producto.precio}',
                'cantidad': f'{producto.cantidad}',
                'subcategoria': f'{producto.subcategoria}',
            }

            jsonData['productos'].append(arreglo_json)

    except Exception as e:
        print(e)
        jsonData={
            'status': 'error',
            'message': 'Error en la base de datos'
        }

    
    return HttpResponse(json.dumps(jsonData),content_type='application/json')