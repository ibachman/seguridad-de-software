# -*- encoding: utf-8 -*-
from django import forms
from .models import *

class registroForm(forms.ModelForm):
    password=forms.CharField(label="",widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : 'Contraseña'}))
    nombre_de_usuario=forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Nombre de usuario'}))
    nickname=forms.CharField(label="",widget=forms.HiddenInput(attrs={'value':" "}))
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'E-mail'}))

    class Meta:
        model=usuario
class loginForm(forms.ModelForm):
    password=forms.CharField(label="",widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : 'Contraseña'}))
    nombre_de_usuario=forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Nombre de usuario'}))
    email=forms.EmailField(label="",widget=forms.HiddenInput(attrs={'value':"dummy@mail.com"}))
    nickname=forms.CharField(label="",widget=forms.HiddenInput(attrs={'value':" "}))
    class Meta:
        model=usuario


