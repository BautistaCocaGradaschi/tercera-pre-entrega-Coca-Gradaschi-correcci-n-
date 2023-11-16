"""
URL configuration for rev_peliculas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from rev_peliculas.view import prueba_con_html
from rev_peliculas.view import crear_peli, lista_peli, buscar_peli, lista_act, crear_act, buscar_act, lista_serie, crear_serie, buscar_serie


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('prueba/', prueba_con_html),
    path("crear-peli/", crear_peli, name="crear_peli"),
    path("lista-peli/", lista_peli, name="lista_peli"),
    path("app-peli/", include("app_peli.urls")),
    path("buscar-peli/", buscar_peli, name="buscar_peli"),
    path("lista-act/", lista_act, name="lista_act"),
    path("crear-act/", crear_act, name="crear_act"),
    path("app-act/", include("app_peli.urls")),
    path("buscar-act/", buscar_act, name ="buscar_act"),
    path("app-serie/", include("app_peli.urls")),
    path("lista-serie/", lista_serie, name="lista_serie"),
    path("crear-serie/", crear_serie, name="crear_serie"),
    path("buscar-serie/", buscar_serie, name ="buscar_serie"),
]
