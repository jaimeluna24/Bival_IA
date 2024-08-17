from django.urls import path
from . import views


urlpatterns = [
    path('', views.muestras),
    path('muestras', views.muestras, name = 'muestras'),
    path('agregar-muestra', views.agregar, name = 'agregar-muestra'),
    path('muestras/detalles/<codigomuestra>', views.detalles, name = 'detalles-muestra'),
    path('muestras/detalles/editar/<codigomuestra>', views.editar_caracteristicas, name = 'editar-caracteristicas-muestra'),
    path('logout/', views.exit, name = 'exit'),
    path('register/', views.register, name = 'register')
]