from django.contrib import admin
from django.urls import path
from djangohttp.views import bienvenida, bienvenidaRojo
from djangohttp.views import categoriaEdad, obtenerMomentoActual, contenidoHTML


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('bienvenida123/', bienvenidaRojo),
    path('categoriaEdad/<int:edad>', categoriaEdad),
    path('obtenerMomentoActual/', obtenerMomentoActual),
    path('contenidoHTML/<nombre>/<int:edad>', contenidoHTML)
]
