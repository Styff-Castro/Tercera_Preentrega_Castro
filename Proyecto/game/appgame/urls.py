from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('consolas/', consolas, name="consolas"),
    path('accesorios/', accesorios, name="accesorios"),
    path('juegos/', juegos, name="juegos"),

    path('acerca/', acerca, name="acerca"),

    ##---Formulario---#
    path('consolaForm/', consolaForm, name="consolaForm"),
    path('accesorioForm/', accesorioForm, name="accesorioForm"), 
    path('juegoForm/', juegoForm, name="juegoForm"),

    ##---Buscar---##
    path('buscarConsolas/', buscarConsolas, name="buscarConsolas"),
    path('buscarAccesorios/', buscarAccesorios, name="buscarAccesorios"),
    path('buscarJuegos/', buscarJuegos, name="buscarJuegos"),
    path('encontrarConsolas/', encontrarConsolas, name="encontrarConsolas"),
    path('encontrarAccesorios/', encontrarAccesorios, name="encontrarAccesorios"),
    path('encontrarJuegos/', encontrarJuegos, name="encontrarJuegos"),
    

]
