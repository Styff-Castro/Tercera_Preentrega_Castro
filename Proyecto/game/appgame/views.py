from django.shortcuts import render
from .models import *

from .forms import *
# Create your views here.
def home(request):
    return render(request, "appgame/index.html")

def consolas(request):
    contexto = {"consolas": Consolas.objects.all()}
    return render(request, "appgame/consolas.html", contexto)

def accesorios(request):
    contexto = {"accesorios": Accsesorios.objects.all()}
    return render(request, "appgame/accesorios.html", contexto)

def juegos(request):
    contexto = {"juegos": Juegos.objects.all()}
    return render(request, "appgame/juegos.html", contexto)

def acerca(request):
    return render(request, "appgame/acerca.html")

##---Formulario---##
def consolaForm(request):
    if request.method == "POST":
        miForm = ConsolaForm(request.POST)
        if miForm.is_valid():
            consola_nombre = miForm.cleaned_data.get("nombre")
            consola_empresa = miForm.cleaned_data.get("empresa")
            consola_modelo = miForm.cleaned_data.get("modelo")
            consola_precio = miForm.cleaned_data.get("precio")
            consola = Consolas(nombre=consola_nombre, empresa=consola_empresa, modelo=consola_modelo, precio=consola_precio) 
            consola.save()
            contexto = {"consolas": Consolas.objects.all() }
            return render(request, "appgame/consolas.html", contexto)
        
    else:
        miForm =ConsolaForm()

    return render(request, "appgame/consolaForm.html", {"form":miForm})


def accesorioForm(request):
    if request.method == "POST":
        miForm = AccesorioForm(request.POST)
        if miForm.is_valid():
            accesesorio_nombre = miForm.cleaned_data.get("nombre")
            accesorio_empresa = miForm.cleaned_data.get("empresa")
            accesorio_modelo = miForm.cleaned_data.get("modelo")
            accesorio_precio = miForm.cleaned_data.get("precio")
            accesorio = Accsesorios(nombre=accesesorio_nombre, empresa=accesorio_empresa, modelo=accesorio_modelo, precio=accesorio_precio) 
            accesorio.save()
            contexto = {"accesorios": Accsesorios.objects.all() }
            return render(request, "appgame/accesorios.html", contexto)
        
    else:
        miForm =AccesorioForm()

    return render(request, "appgame/accesorioForm.html", {"form":miForm})


def juegoForm(request):
    if request.method == "POST":
        miForm = JuegoForm(request.POST)
        if miForm.is_valid():
            juego_nombre = miForm.cleaned_data.get("nombre")
            juego_empresa = miForm.cleaned_data.get("empresa")
            juego_categoria = miForm.cleaned_data.get("categoria")
            juego_precio = miForm.cleaned_data.get("precio")
            juego = Juegos(nombre=juego_nombre, empresa=juego_empresa, categoria=juego_categoria, precio=juego_precio) 
            juego.save()
            contexto = {"juegos": Juegos.objects.all() }
            return render(request, "appgame/juegos.html", contexto)
        
    else:
        miForm =JuegoForm()

    return render(request, "appgame/juegoForm.html", {"form":miForm})

#___ Buscarconsola
def buscarConsolas(request):
    return render(request, "appgame/buscarconsola.html")

def encontrarConsolas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        consolas = Consolas.objects.filter(nombre__icontains=patron)
        contexto = {'consolas': consolas}    
    else:
        contexto = {'consolas': Consolas.objects.all()}
        
    return render(request, "appgame/consolas.html", contexto)

##___BuscarAccesorio

def buscarAccesorios(request):
    return render(request, "appgame/buscaraccesorios.html")

def encontrarAccesorios(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        accesorios = Accsesorios.objects.filter(nombre__icontains=patron)
        contexto = {'accesorios': accesorios}    
    else:
        contexto = {'accesorio': Accsesorios.objects.all()}
        
    return render(request, "appgame/accesorios.html", contexto)

#___BuscarJuego

def buscarJuegos(request):
    return render(request, "appgame/buscarjuego.html")

def encontrarJuegos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        juegos = Juegos.objects.filter(nombre__icontains=patron)
        contexto = {'juegos': juegos}    
    else:
        contexto = {'juegos': Juegos.objects.all()}
        
    return render(request, "appgame/juegos.html", contexto)

##--Encontrar Cursos--#

def encontrarConsolas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        consolas = Consolas.objects.filter(nombre__icontains=patron)
        contexto = {'consolas': consolas}    
    else:
        contexto = {'consolas': Consolas.objects.all()}
        
    return render(request, "appgame/consolas.html", contexto)

def encontrarAccesorios(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        accesorios = Accsesorios.objects.filter(nombre__icontains=patron)
        contexto = {'accesorios': accesorios}    
    else:
        contexto = {'accesorios': Accsesorios.objects.all()}
        
    return render(request, "appgame/accesorios.html", contexto)

def encontrarJuegos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        juegos = Juegos.objects.filter(nombre__icontains=patron)
        contexto = {'juegos': juegos}    
    else:
        contexto = {'juegos': Juegos.objects.all()}
        
    return render(request, "appgame/juegos.html", contexto)


    