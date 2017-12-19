# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from SGMGU.models import *
from SGMGU.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utiles import *
from django.http import HttpResponse,Http404
from django.db.models import Q
from django.db import models


# para buscar entre las entidades
@login_required
@permission_required(['administrador', 'especialista'])
def buscar_entidades(request):
    if request.method == "POST":
        texto = request.POST['texto_entidad'].lower()

        entidades = Entidad.objects.filter(e_nombre__icontains=texto)
    else:
        entidades = []
    entidades = paginar(request, entidades)
    context = {'entidades': entidades, 'paginas': crear_lista_pages(entidades), 'busqueda': True,
               'texto': request.POST['texto_entidad']}
    return render(request, "Entidades/gestion_entidades.html", context)


# para imprimir en la tabla las entidades

@login_required
@permission_required(['administrador', 'especialista'])
def gestion_entidades(request):
    entidades = Entidad.objects.all()
    entidades = paginar(request, entidades)
    context = {'entidades': entidades, 'paginas': crear_lista_pages(entidades)}
    return render(request, "Entidades/gestion_entidades.html", context)


# aqui registro una entidad
def registrar_entidad(request):
    if request.method == 'POST':
        form=EntidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "La entidad se ha registrado con éxito.")
            return redirect('/entidades')
    else:
        form = EntidadForm()
    context = {'form':form}
    return render(request, "entidades/form_entidad.html", context)

# para modificar una entidad:

@login_required
@permission_required(['administrador','especialista'])
def modificar_entidad(request,id_entidad):
    entidad=Entidad.objects.get(id_codigo_entidad=id_entidad)
    if request.method == 'POST':
        form=EntidadForm(request.POST,instance=entidad)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "La entidad se ha modificado con éxito.")
            return redirect('/entidades')
    else:
        form = EntidadForm(instance=entidad)
    # Creamos el contexto
    context = {'form':form,'nombre_accion':'Modificar'}
    # Y mostramos los datos
    return render(request, "entidades/form_entidad.html", context)

# eliminar una entidad

@login_required
@permission_required(['administrador','especialista'])
def eliminar_entidad(request,id_entidad):
    entidad = Entidad.objects.get(id_codigo_entidad=id_entidad)
    entidad.estado = False
    entidad.save()
    messages.add_message(request, messages.SUCCESS, "La entidad ha sido desactivada con éxito.")
    return redirect('/entidades')
