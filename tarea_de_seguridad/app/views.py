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
def reservas(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    if user is None:
        exist=False
    return render_to_response("reservas.html",locals(), context_instance=RequestContext(request))
def contacto(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    if user is None:
        exist=False
    return render_to_response("contacto.html",locals(), context_instance=RequestContext(request))
def moteles(request):
    user=request.session.get('username')
    exist=request.session.get('user_exist')
    if user is None:
        exist=False
    return render_to_response("moteles.html",locals(), context_instance=RequestContext(request))