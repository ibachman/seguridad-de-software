from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tarea_de_seguridad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^registro/', 'app.views.register', name='register'),
    url(r'^(?P<pieza_id>[0-9]+)/crear_reserva/', 'app.views.crear_reserva', name='crear_reserva'),
    url(r'^login/', 'app.views.login', name='login'),
    url(r'^logout/', 'app.views.logout', name='logout'),

    url(r'^amistades/', 'app.views.amistades', name='amistades'),
    url(r'^solicitar_amistad/', 'app.views.solicitar_amistad', name='solicitar_amistad'),

    url(r'^moteles/', 'app.views.moteles', name='moteles'),
    url(r'^(?P<motel_id>[0-9]+)/info_motel/', 'app.views.info_motel', name='infomotel'),
    url(r'^(?P<pieza_id>[0-9]+)/info_pieza/', 'app.views.info_pieza', name='infopieza'),
    url(r'^mis_reservas/', 'app.views.mis_reservas', name='reservas'),
    url(r'^contacto/', 'app.views.contacto', name='contacto'),
    url(r'^admin/', include(admin.site.urls)),
)
