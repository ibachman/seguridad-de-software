# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.ñññ
class usuario(models.Model):
    nombre_de_usuario=models.CharField(max_length=120,null=False, blank=False)
    nickname=models.CharField(max_length=120,null=True, blank=True)
    password=models.CharField(max_length=120,null=False, blank=False)
    email=models.EmailField(max_length=120)

    def __unicode__(self):
        return smart_unicode(self.nombre_de_usuario)

class motel(models.Model):
    nombre_del_motel=models.CharField(max_length=120,null=False, blank=False)
    ubicacion=models.CharField(max_length=200,null=False, blank=False)
    descripcion=models.TextField(max_length=1000,null=False, blank=False)
    telefono=models.CharField(max_length=120,null=False, blank=False)
    email=models.EmailField(max_length=120)
    def __unicode__(self):
        return smart_unicode(self.nombre_del_motel)

class pieza(models.Model):
    nombre_de_la_pieza=models.CharField(max_length=200,null=False, blank=False)
    motel=models.ForeignKey('motel')
    cantidad=models.IntegerField(max_length=2,null=False, blank=False)
    piezas_disponibles=models.IntegerField(max_length=2,null=False, blank=False)
    descripcion=models.TextField(max_length=1000,null=False, blank=False)
    def __unicode__(self):
        return smart_unicode(self.nombre_de_la_pieza)


class reservas(models.Model):
    motel=models.ForeignKey('motel')
    usuario=models.ForeignKey('usuario',related_name="usuario")
    invitado=models.ForeignKey('usuario',blank=True,null=True,related_name="invitado")
    pieza=models.ForeignKey('pieza')
    fecha1=models.DateField()
    hora1=models.TimeField()
    fecha2=models.DateField()
    hora2=models.TimeField()
    def __unicode__(self):
        return smart_unicode("Reserva " + str(self.pk)+": "+str(self.usuario)+" en "+str(self.motel))

class amistad(models.Model):
    usuario_1=models.ForeignKey('usuario',related_name="usuario1")
    usuario_2=models.ForeignKey('usuario',related_name="usuario2")
    visto=models.BooleanField(default=False)
    @classmethod
    def create(cls,user1, user2):
        am= cls(usuario_1=user1,usuario_2=user2)
        return am
    def __unicode__(self):
        return smart_unicode(str(self.usuario_1)+" es amigo de "+str(self.usuario_2))

class solicitudesDeAmistad(models.Model):
    solicitante=models.ForeignKey('usuario',related_name="solicitante")
    solicitado=models.ForeignKey('usuario',related_name="solicitado")
    timespamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    @classmethod
    def create(cls,user1, user2):
        solicitud = cls(solicitante=user1,solicitado=user2)
        return solicitud
    def __unicode__(self):
        return smart_unicode(str(self.solicitante)+" solicitó ser amigo de "+str(self.solicitado))

class usuarios_moteles(models.Model):
    nombre_de_usuario=models.CharField(max_length=120,null=False, blank=False)
    motel_asociado=models.ForeignKey('motel')
    password=models.CharField(max_length=120,null=False, blank=False)
    email=models.EmailField(max_length=120)

    def __unicode__(self):
        return smart_unicode(self.nombre_de_usuario+" asociado a "+str(self.motel_asociado))

class comentarios(models.Model):
    usuario=models.ForeignKey('usuario')
    motel=models.ForeignKey('motel')
    pieza=models.ForeignKey('pieza',blank=True,null=True)
    comentario=models.TextField(max_length=1000,blank=False,null=False)
    calificacion=models.IntegerField(max_length=1,blank=False,null=False)
    def __unicode__(self):
        return smart_unicode(str(self.usuario)+" calificó al motel "+str(self.motel)+" con nota "+str(self.calificacion))