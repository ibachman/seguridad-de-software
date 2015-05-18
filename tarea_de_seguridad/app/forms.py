# -*- encoding: utf-8 -*-
from django import forms
from .models import *
from django.forms.widgets import SplitDateTimeWidget
from datetimewidget.widgets import DateWidget, TimeWidget

class registroForm(forms.ModelForm):
    password=forms.CharField(label="",widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : 'Contraseña'}))
    nombre_de_usuario=forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Nombre de usuario'}))
    nickname=forms.CharField(label="",widget=forms.HiddenInput(attrs={'value':" "}))
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'E-mail'}))

    class Meta:
        model=usuario
        fields = "__all__" 

class loginForm(forms.ModelForm):
    password=forms.CharField(label="",widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : 'Contraseña'}))
    nombre_de_usuario=forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Nombre de usuario'}))
    email=forms.EmailField(label="",widget=forms.HiddenInput(attrs={'value':"dummy@mail.com"}))
    nickname=forms.CharField(label="",widget=forms.HiddenInput(attrs={'value':" "}))
    class Meta:
        model=usuario
        fields = "__all__"

class reservaForm(forms.Form):
    motel = forms.CharField(label="Motel:",widget=forms.TextInput(attrs={'class' : 'form-control'}))
    pieza = forms.CharField(label="Pieza",widget=forms.TextInput(attrs={'class' : 'form-control'}))
    fecha1 = forms.DateField(label="Fecha de Inicio:",widget=DateWidget(usel10n=True, bootstrap_version=3))
    hora1 = forms.TimeField(label="Hora de Inicio:",widget=TimeWidget(usel10n=True, bootstrap_version=3))
    fecha2 = forms.DateField(label="Fecha de Término:",widget=DateWidget(usel10n=True, bootstrap_version=3))
    hora2 = forms.TimeField(label="Hora de Término:",widget=TimeWidget(usel10n=True, bootstrap_version=3))

class solicitudAmistadForm(forms.Form):
    solicitado=forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Solicitado'}))

class conctacForm(forms.Form):
    nombre = forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Nombre'}))
    mailContacto = forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'mail'}))
    mensaje = forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'mensaje'}))