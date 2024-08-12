from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('muestras', views.muestras, name = 'muestras'),
    path('agregar-muestra', views.agregar, name = 'agregar-muestra')

]