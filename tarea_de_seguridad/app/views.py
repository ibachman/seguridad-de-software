# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from .forms import *
from .models import *
# Create your views here.

def register(request):
    form=registroForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        user=request.session.get('username')
        exist=request.session.get('user_exist')
        if user is None:
            exist=False
        return HttpResponseRedirect('/../')
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    if user is None:
        exist=False

    return render_to_response("registro.html",locals(), context_instance=RequestContext(request))

def home(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    if user is None:
        exist=False
    print user,exist
    return render_to_response("home.html",locals(), context_instance=RequestContext(request))

def login(request):
    form=loginForm(request.POST or None)
    user_exist=False
    if request.method == 'POST':

        if form.is_valid():
            username=form.cleaned_data['nombre_de_usuario']
            contr=form.cleaned_data['password']
            user_exist = usuario.objects.filter(nombre_de_usuario=username,password=contr) is not None
            if user_exist:
                request.session['username']=username
                request.session['user_exist']=user_exist
                exist = user_exist
                return HttpResponseRedirect('/../')
    exist=user_exist
    return render_to_response("login.html",locals(), context_instance=RequestContext(request))

def logout(request):
    try:
        del request.session['username']
        #del request.session['user_exist']
    except KeyError:
        pass
    return HttpResponseRedirect('/')

def amistades(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    if user is None:
        exist=False
    return render_to_response("amistades.html",locals(), context_instance=RequestContext(request))
def mis_reservas(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    current_user = usuario.objects.get(nombre_de_usuario=user)              
    lista_reservas=reservas.objects.filter(usuario=current_user.id)
    if user is None:
        exist=False
    return render_to_response("mis_reservas.html",locals(), context_instance=RequestContext(request))
def contacto(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    if user is None:
        exist=False
    return render_to_response("contacto.html",locals(), context_instance=RequestContext(request))
def moteles(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    lista_moteles=motel.objects.all()
    if user is None:
        exist=False
    return render_to_response("moteles.html",locals(), context_instance=RequestContext(request))
def info_motel(request, motel_id):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    motel_info=motel.objects.get(id=motel_id)
    lista_piezas=pieza.objects.filter(motel=motel_id)
    if user is None:
        exist=False
    return render_to_response("info_motel.html",locals(), context_instance=RequestContext(request))
def info_pieza(request, pieza_id):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    pieza_info=pieza.objects.get(id=pieza_id)
    if user is None:
        exist=False
    return render_to_response("info_pieza.html",locals(), context_instance=RequestContext(request))

def crear_reserva(request, pieza_id):
    if request.method == 'POST':
        form = reservaForm(request.POST)
        if form.is_valid():
            #guardamos la reserva sólo si hay disponibilidad
            pieza_reserva = pieza.objects.get(id=pieza_id)
            disponibilidad =pieza_reserva.piezas_disponibles
            if(disponibilidad > 0):
                user_name=request.session.get('username')
                user = usuario.objects.get(nombre_de_usuario=user_name)
                motel_reserva=motel.objects.get(nombre_del_motel=form.cleaned_data['motel'])
                fecha_reserva=form.cleaned_data['fecha']
                hora_reserva=form.cleaned_data['hora']
                nueva_reserva = reservas(motel=motel_reserva, usuario=user, 
                pieza = pieza_reserva, fecha=fecha_reserva, hora=hora_reserva )
                nueva_reserva.save()
                #updateamos disponibilidad
                nueva_disponibilidad = disponibilidad - 1
                pieza_reserva.piezas_disponibles = nueva_disponibilidad
                pieza_reserva.save()
                return HttpResponseRedirect('/')
        
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')    
    else:
        pieza_obj = pieza.objects.get(id=pieza_id)
        motel_obj = motel.objects.get(id=pieza_obj.motel.id)
        form = reservaForm(initial={'motel':motel_obj.nombre_del_motel, 'pieza':pieza_obj.nombre_de_la_pieza})

    return render(request, 'crear_reserva.html', {'form': form})