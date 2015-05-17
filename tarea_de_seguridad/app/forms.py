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
    fecha = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    hora = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))

