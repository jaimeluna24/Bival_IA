from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from bivalvos.models import AuthUser  # Importa el modelo de usuario personalizado



# Create your views here.
def inicio(request):
    return HttpResponse("<h1> Hola</h1>")


@login_required
def muestras(request):
    filtro = request.GET.get('filtro', None)  # Obtener el valor de la consulta GET
    if filtro:
        muestras_list = Caracteristicasbivalvos.objects.filter(codigomuestra = filtro)
    else:
        muestras_list = Caracteristicasbivalvos.objects.all()
    # muestras_list = Caracteristicasbivalvos.objects.all()
    return render(request, 'vistas/muestras.html',{'muestras_list': muestras_list})

@login_required
@transaction.atomic
def agregar(request):
    auth_user_instance = AuthUser.objects.get(pk=request.user.pk) 
    condiciones_list = Condicionesbivalvos.objects.all()
    formas_list = Formas.objects.all()
    habitat = Habitats.objects.all()
    tipo_habitat = Tiposhabitat.objects.all()
    especies_list = Especies.objects.all()
    if request.method == 'POST':
        try:
            # Guardamos los datos de la Ubicación
            ubicacion_form = Ubicaciones(
                latitud = request.POST.get('latitud'),
                longitud = request.POST.get('longitud'),
                altitud = request.POST.get('altitud'),
                region = request.POST.get('region')
            )
            ubicacion_form.save()

            #Guardamos los datos de marea
            marea_form = Mareas(
                hora = request.POST.get('hora'),
                zonalugar = request.POST.get('zonalugar'),
                altitudmarea = request.POST.get('altitudmarea'),
                observaciones = request.POST.get('observaciones'),
            )
            marea_form.save()

            # Guardar las Variables ambientales

            # Se obtiene la instancia de Habitats
            idhabitats = request.POST.get('idhabitat')
            habitat_instance = Habitats.objects.get(id=idhabitats)

            # Se obtiene la instancia de Especies
            idespecie = request.POST.get('idespecie')
            especie_instance = Especies.objects.get(id=idespecie)

            # Se obtiene la instancia de TipoHabitat
            idtipohabitat = request.POST.get('idtipohabitat')
            tipohabitat_instance = Tiposhabitat.objects.get(id=idtipohabitat)
            
            variablesambientales_form = Variablesambientales(
                temperatura = request.POST.get('temperatura'),
                salinidad = request.POST.get('salinidad'),
                ph = request.POST.get('ph'),
                oxigeno = request.POST.get('oxigeno'),
                idubicacion = ubicacion_form,
                idhabitat = habitat_instance,
                idespecie = especie_instance,
                idmarea = marea_form,
                idtipohabitat = tipohabitat_instance,
            )
            variablesambientales_form.save()


            # Se obtiene la instancia de condiciones
            idcondicion = request.POST.get('idcondicionbivalvo')
            condicion_instance = Condicionesbivalvos.objects.get(id=idcondicion)

            # Se obtiene la instancia de formas
            idforma = request.POST.get('idforma')
            forma_instance = Formas.objects.get(id=idforma)

            # Guardamos los datos caracteristicos de los bivalvos
            caracteristicas_form = Caracteristicasbivalvos(
                codigomuestra = request.POST.get('codigomuestra'),
                altura = request.POST.get('altura'),
                ancho = request.POST.get('ancho'),
                espesor = request.POST.get('espesor'),
                color = request.POST.get('color'),
                estructuraconcha = request.POST.get('estructuraconcha'),
                pesoconcarne = request.POST.get('pesoconcarne'),
                pesosincarne = request.POST.get('pesosincarne'),
                fotodorsal = request.FILES.get('fotodorsal'),
                fotolateral = request.FILES.get('fotolateral'),
                fotoventral = request.FILES.get('fotoventral'),
                fotoanterior = request.FILES.get('fotoanterior'),
                fotoposterior = request.FILES.get('fotoposterior'),
                idcondicionbivalvo = condicion_instance,
                idforma = forma_instance,
                idvariableambiental = variablesambientales_form,
                iduser = auth_user_instance 
            )
            caracteristicas_form.save()

            return redirect('muestras')

        except Exception as e:
            transaction.set_rollback(True)
            return render(request, 'vistas/error.html', {'error': str(e)})



    return render(request, 'vistas/agregar-muestra.html', {'condiciones_list': condiciones_list, 'formas_list': formas_list,
                                                           'habitat': habitat, 'tipo_habitat': tipo_habitat, 'especies_list': especies_list})

@login_required
def detalles(request, codigomuestra):
    muestra = get_object_or_404(Caracteristicasbivalvos, codigomuestra=codigomuestra)

    return render(request, 'vistas/detalles-muestra.html', {'muestra': muestra})

@login_required
def editar_caracteristicas(request, codigomuestra):
    muestra = get_object_or_404(Caracteristicasbivalvos, codigomuestra=codigomuestra)
    condiciones_list = Condicionesbivalvos.objects.all()
    formas_list = Formas.objects.all()
    if request.method == 'POST':
        # Actualizar los campos con los datos enviados en el formulario
        muestra.codigomuestra = request.POST.get('codigomuestra')
        muestra.altura = request.POST.get('altura')
        muestra.ancho = request.POST.get('ancho')
        muestra.espesor = request.POST.get('espesor')
        muestra.color = request.POST.get('color')
        muestra.estructuraconcha = request.POST.get('estructuraconcha')
        muestra.pesoconcarne = request.POST.get('pesoconcarne')
        muestra.pesosincarne = request.POST.get('pesosincarne')
    
        muestra.save()
        return redirect('detalles-muestra', codigomuestra=muestra.codigomuestra)
    return render(request, 'vistas/forms-edit/caracteristicas-edit.html', {'muestra': muestra, 'condiciones_list': condiciones_list, 'formas_list': formas_list})









def exit(request):
    logout(request)
    return redirect('login')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            # user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            # login(request, user)
            return redirect('muestras')
        else:
            data['form'] = user_creation_form
    return render(request,'registration/register.html', data)