from django.urls import path
from . import views


urlpatterns = [
    path('', views.muestras),
    path('muestras', views.muestras, name = 'muestras'),
    path('agregar-muestra', views.agregar, name = 'agregar-muestra'),
    path('muestras/detalles/<codigomuestra>', views.detalles, name = 'detalles-muestra'),
    path('muestras/detalles/editar/<codigomuestra>', views.editar_caracteristicas, name = 'editar-caracteristicas-muestra'),
    path('muestras/detalles/editar-variables-ambientales/<codigomuestra>/<idvariable>', views.editar_variables, name = 'editar-variables-ambientales'),
    path('muestras/detalles/editar-ubicacion/<codigomuestra>/<idubicacion>', views.editar_ubicacion, name = 'editar-ubicacion'),
    path('muestras/detalles/editar-marea/<codigomuestra>/<idmarea>', views.editar_marea, name = 'editar-marea'),
    path('logout/', views.exit, name = 'exit'),
    path('register/', views.register, name = 'register')
]