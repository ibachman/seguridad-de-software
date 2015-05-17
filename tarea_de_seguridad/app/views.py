# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
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
    return render_to_response("home.html",locals(), context_instance=RequestContext(request))

def login(request):
    form=loginForm(request.POST or None)
    user_exist=False
    user_not_registered=False
    if request.method == 'POST':

        if form.is_valid():
            username=form.cleaned_data['nombre_de_usuario']
            contr=form.cleaned_data['password']
            possible_user= usuario.objects.filter(nombre_de_usuario=username,password=contr)
            user_exist =len(possible_user) > 0

            if user_exist:
                request.session['username']=username
                request.session['user_exist']=user_exist
                exist = user_exist
                return HttpResponseRedirect('/../')
            else:
                user_not_registered= not user_exist
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
    user_info= usuario.objects.get(nombre_de_usuario=user)
    user_id=user_info.pk
    amis= amistad.objects.filter(Q(usuario_1=user_id) | Q(usuario_2=user_id))
    sol_amis=solicitudesDeAmistad.objects.filter(solicitante=user_id)
    amigos=[]
    for am in amis:
        if (am.usuario_1).nombre_de_usuario == user :
            amigos.append(str(am.usuario_2))
        else:
            amigos.append(str(am.usuario_1))
    solicitudes_de_amistad=[]
    for s_a in sol_amis:
        solicitudes_de_amistad.append(str(s_a.solicitado))

    has_friends=len(amis)>0
    has_made_frequest=len(sol_amis)>0
    if user is None:
        exist=False
    return render_to_response("amistades.html",locals(), context_instance=RequestContext(request))

def solicitar_amistad(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    form=solicitudAmistadForm(request.POST or None)

    if request.method == 'POST':
       solicitado=request.POST.get("solicitado")
       if len(usuario.objects.filter(nombre_de_usuario=solicitado))>0:
            user1_info= usuario.objects.get(nombre_de_usuario=user)
            user2_info= usuario.objects.get(nombre_de_usuario=solicitado)
            user_info= usuario.objects.get(nombre_de_usuario=user)
            user_pk=user_info.pk
            friend_request_for_user=solicitudesDeAmistad.objects.filter(solicitado=user_pk)
            for request in friend_request_for_user:
                if request.solicitante==user2_info:
                    request.delete()
                    amist=amistad.create(user1_info,user2_info)
                    amist.save()
                    return HttpResponseRedirect('/../')
            if len(amistad.objects.filter(Q(usuario_1=user1_info.pk) | Q(usuario_2=user1_info.pk),Q(usuario_1=user2_info.pk) | Q(usuario_2=user2_info.pk)))==0:
                sol=solicitudesDeAmistad.create(user1_info,user2_info)
                sol.save()
       return HttpResponseRedirect('/../')

    return render_to_response("solicitar_amistad.html",locals(), context_instance=RequestContext(request))


def mis_reservas(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    if user is None:
        exist=False
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