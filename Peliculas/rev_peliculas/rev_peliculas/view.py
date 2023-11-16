from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from app_peli.models import Peliculas, Actores, Series

#def prueba_con_html(request):
    #contexto = {}
    #http_response = render(
        #request=request,
       # template_name='base.html',
       # context=contexto,
   # )
 #   return http_response

#def crear_peli(request):
  # http_response = render(
    #   request=request,
    #   template_name='base.html',
    #)
   #return http_response

def crear_peli(request):
   if request.method == "POST":
       data = request.POST
       peli = Peliculas(nombre=data['nombre'], puntaje=data['puntaje'])
       peli.save()
       url_exitosa = reverse('lista_peli')
       return redirect(url_exitosa)
   else:  
       return render(
           request=request,
           template_name='base.html',
       )

def lista_peli(request):
   contexto = {
       "rev_peliculas": Peliculas.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='app_peli.html',
       context=contexto,
   )
   return http_response

def buscar_peli(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       pelicula = Peliculas.objects.filter(Q(nombre__icontains=busqueda)|Q(puntaje__icontains=busqueda))
       contexto = {
           "rev_peliculas": pelicula,
       }
       http_response = render(
           request=request,
           template_name='app_peli.html',
           context=contexto,
       )
       return http_response

def lista_act(request):
   contexto = {
       "rev_peliculas": Actores.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='lista_act.html',
       context=contexto,
   )
   return http_response

def crear_act(request):
   if request.method == "POST":
       data = request.POST
       act = Actores(nombre=data['nombre'], puntaje=data['puntaje'])
       act.save()
       url_exitosa = reverse('lista_act')
       return redirect(url_exitosa)
   else:  
       return render(
           request=request,
           template_name='creacion_act.html',
       )

def buscar_act(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       actor = Actores.objects.filter(Q(nombre__icontains=busqueda)|Q(puntaje__icontains=busqueda))
       contexto = {
           "rev_peliculas": actor,
       }
       http_response = render(
           request=request,
           template_name='lista_act.html',
           context=contexto,
       )
       return http_response
   
def lista_serie(request):
   contexto = {
       "rev_peliculas": Series.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='lista_serie.html',
       context=contexto,
   )
   return http_response

def crear_serie(request):
   if request.method == "POST":
       data = request.POST
       serie = Series(nombre=data['nombre'], puntaje=data['puntaje'])
       serie.save()
       url_exitosa = reverse('lista_serie')
       return redirect(url_exitosa)
   else:  
       return render(
           request=request,
           template_name='creacion_serie.html',
       )

def buscar_serie(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       serie = Series.objects.filter(Q(nombre__icontains=busqueda)|Q(puntaje__icontains=busqueda))
       contexto = {
           "rev_peliculas": serie,
       }
       http_response = render(
           request=request,
           template_name='lista_serie.html',
           context=contexto,
       )
       return http_response