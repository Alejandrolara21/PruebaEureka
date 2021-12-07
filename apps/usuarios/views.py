from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

#MODELOS
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario

#EXCEPTION
from django.db.utils import IntegrityError

def login_view(request):
    #Vista del login
    if request.method == 'POST':
        usuario = authenticate(
                username=request.POST['correo'],
                password=request.POST['password']
        )
        if usuario is not None:
            login(request,usuario)
            return redirect('inicio')
        else:
            return render(request,'usuarios/login.html',{'error':'Correo o password incorrectos'})

    return render(request,'usuarios/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_usuario')


def signup_view(request):
    if request.method == 'POST':
        username=request.POST['correo']
        email=request.POST['correo']
        nombre= request.POST['nombre']
        apellido = request.POST['apellido']
        password = request.POST['password']

        try:
            user = User.objects.create_user(
                username=username,
                password=password             
            )

            user.first_name = nombre
            user.last_name = apellido
            user.email = email

            user.save()

            usuario = Usuario(usuario=user)
            usuario.save()

            return render(request,'usuarios/login.html')
        except IntegrityError:
            return render(request,'usuarios/signup.html',{'error': 'Usuario ya existente'})
        except:
            return render(request,'usuarios/signup.html',{'error': 'Error, vuelva intentar mas tarde'})
    return render(request,'usuarios/signup.html') 