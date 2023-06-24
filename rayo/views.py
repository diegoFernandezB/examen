from django.shortcuts import render, redirect
from .models import cliente, administrador, mecanico, Archivo
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt 
from .forms import ArchivoForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    context={}
    return render(request,'rayo/index.html', context)

def fichaServ(request):
    context = {}
    return render (request, 'rayo/fichaServ.html', context)

def carritoCompras(request):
    context = {}
    return render (request, 'rayo/carritoCompras.html', context)

def CrudTrabajos(request):
    context = {}
    return render (request, 'rayo/CrudTrabajos.html', context)

def fichamecas(request):
    context = {}
    return render (request, 'rayo/fichamecas.html', context)

def login(request):
     if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request, usuario=usuario, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin/')  # Redirige al administrador de Django
            else:
                return redirect('index')  # Redirige a otra página en caso de no ser un administrador
        else:
            error_message = 'Credenciales inválidas. Por favor, ingrese nuevamente.'
            context = {'error_message': error_message}
            return render(request, 'rayo/login.html', context)
     else:
        context = {}
        return render(request, 'rayo/loguin.html', context)


@csrf_exempt
@login_required
def loguin(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            error_message = 'Credenciales invalidas. Por favor ingrese nuevamente.'
            return render(request, 'rayo/index.html',{'error_message': error_message})
    
    

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def meca1(request):
    context = {}
    return render (request, 'rayo/meca1.html', context)

def meca2(request):
    context = {}
    return render (request, 'rayo/meca2.html', context)

def meca3(request):
    context = {}
    return render (request, 'rayo/meca3.html', context)

def plantillamec(request):
    context = {}
    return render (request, 'rayo/plantillamec.html', context)

def plantillaserv(request):
    context = {}
    return render (request, 'rayo/plantillaserv.html', context)

def pll(request):
    context = {}
    return render (request, 'rayo/pll.html', context)

def registro(request):
    context = {}
    return render (request, 'rayo/registro.html', context)

def reserva(request):
    context = {}
    return render (request, 'rayo/reserva.html', context)

def subirArchivo(request):
    archivo = Archivo.objects.all()
    context = {'archivo':archivo}
    print("Enviando Datos")  
    return render (request, 'rayo/subirArchivo.html', context)

def subirArchivo_add(request):
    context = {}
    if request.method == "POST":
        form = ArchivoForm(request.POST)
        if form.is_valid:
            print("Estas en agregar, is_valid")
            form.save()

            form = ArchivoForm()

            context = {'mensaje':'OK, datos grabados...','form':form}
            return render(request, 'rayo/subirArchivo.html',context)
    else:
        form = ArchivoForm()
        context = {'form': form}
        return render (request, 'rayo/subirArchivo.html', context)

def subirArchivo_del(request, pk):
    mensajes = []
    errores = []
    archivos = Archivo.objects.all()
    try:
        archivo = Archivo.objects.get(id_archivo=pk)
        context = {}
        if archivo:
            archivo.delete()
            mensajes.append('Archivos Eliminados Correctamente...')
            context = {'archivos': archivos, 'mensajes': mensajes, 'errores':errores}
            return render (request, 'rayo/subirArchivo.html', context)
    except:
        print("Error ID no existe...")
        archivos = Archivo.objects.all()
        mensaje = "Error ID no existe..."
        context = {'mensaje': mensaje, 'archivos': archivos}
        return render(request, 'rayo/subirArchivo.html', context)

def subirArchivo_edit(request, pk):
    try:
        archivo = Archivo.objects.get(id_genero=pk)
        context = {}
        if archivo:
            print("Edit encontró el Archivo...")
            if request.method == "POST":
                print("edit, es un POST" )
                form = ArchivoForm(request.POST,instance = archivo)
                form.save()
                mensaje = "Datos Actualizados..."
                print(mensaje)
                context = {'archivo': archivo, 'form': form,'mensaje': mensaje}
                return render(request, 'rayo/subirArchivo.html', context)
            else:
                print("edit, no es un post")
                form = ArchivoForm(instance=archivo)
                mensaje = ""
                context = {'archivo': archivo, 'form': form,'mensaje': mensaje}
                return render(request, 'rayo/subirArchivo.html', context)
    except:
        print("Error, id no existe...")
        archivos = Archivo.objects.all()
        mensaje = "Error, id no existe..."
        context = {'mensaje': mensaje,'archivos': archivos}
        return render(request, 'rayo/subirArchivo.html')

def trabajo1(request):
    context = {}
    return render (request, 'rayo/trabajo1.html', context)

def trabajo2(request):
    context = {}
    return render (request, 'rayo/trabajo2.html', context)

def trabajo3(request):
    context = {}
    return render (request, 'rayo/trabajo3.html', context)

def trabajo4(request):
    context = {}
    return render (request, 'rayo/trabajo4.html', context)

def trabajo5(request):
    context = {}
    return render (request, 'rayo/trabajo5.html', context)

def base(request):
    context= {}
    return render (request, 'rayo/base.html', context)

