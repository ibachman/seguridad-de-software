from django.contrib import admin

# Register your models here.
from .models import *

class usuarioAdmin(admin.ModelAdmin):
    class Meta:
        model=usuario

admin.site.register(usuario, usuarioAdmin)

class motelAdmin(admin.ModelAdmin):
    class Meta:
        model= motel

admin.site.register(motel, motelAdmin)

class piezaAdmin(admin.ModelAdmin):
    class Meta:
        model=pieza

admin.site.register(pieza, piezaAdmin)

class reservaAdmin(admin.ModelAdmin):
    class Meta:
        model=reservas

admin.site.register(reservas, reservaAdmin)

class amistadAdmin(admin.ModelAdmin):
    class Meta:
        model=amistad

admin.site.register(amistad, amistadAdmin)

class solicitudAmistadAdmin(admin.ModelAdmin):
    class Meta:
        model=solicitudesDeAmistad

admin.site.register(solicitudesDeAmistad,solicitudAmistadAdmin)

class usuariosMotelesAdmin(admin.ModelAdmin):
    class Meta:
        model=usuarios_moteles

admin.site.register(usuarios_moteles,usuariosMotelesAdmin)

class comentariosAdmin(admin.ModelAdmin):
    class Meta:
        model=comentarios

admin.site.register(comentarios,comentariosAdmin)