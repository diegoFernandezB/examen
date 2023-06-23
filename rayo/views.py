from django.shortcuts import render, redirect
from . models import cliente, administrador, mecanico
from django.contrib.auth import authenticate, login 
from django.views.decorators.csrf import csrf_exempt 
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

@csrf_exempt
def loguin(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            return redirect('subirArchivo')
        else:
            error_message = 'Credenciales invalidas. Por favor ingrese nuevamente.'
            return render(request, 'loguin.html',{'error_message': error_message})
    return render (request, 'rayo/loguin.html')

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
      
   return render(request, 'rayo/registro.html', context )

def reserva(request):
    context = {}
    return render (request, 'rayo/reserva.html', context)

def subirArchivo(request):
    context = {}
    if request.method != 'POST':
        return render (request, 'rayo/subirArchivo.html', context)
    else:
        
        return redirect(index)

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






    
    
