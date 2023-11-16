from django.contrib import admin
from django.urls import path, include
#from rev_peliculas.view import prueba_con_html
from rev_peliculas.view import crear_peli
from rev_peliculas.view import lista_peli, buscar_peli, lista_act, crear_act, buscar_act, lista_serie, crear_serie, buscar_serie

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('prueba/', prueba_con_html),
    path("crear-peli/", crear_peli, name="crear_pelicula"),
    path("lista-peli/", lista_peli, name="lista_peli"),
    path("buscar-peli/", buscar_peli, name="buscar_peli"),
    path("lista-act/", lista_act, name="lista_act"),
    path("crear-act/", crear_act, name="crear_act"),
    path("buscar-act/", buscar_act, name ="buscar_act"),
    path("lista-serie/", lista_serie, name="lista_serie"),
    path("crear-serie/", crear_serie, name="crear_serie"),
    path("buscar-serie/", buscar_serie, name ="buscar_serie"),
]