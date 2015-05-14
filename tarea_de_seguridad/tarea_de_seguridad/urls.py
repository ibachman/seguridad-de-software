from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tarea_de_seguridad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^registro/', 'app.views.register', name='register'),
    url(r'^login/', 'app.views.login', name='login'),
    url(r'^logout/', 'app.views.logout', name='logout'),
    url(r'^amistades/', 'app.views.amistades', name='amistades'),
    url(r'^moteles/', 'app.views.moteles', name='moteles'),
    url(r'^reservas/', 'app.views.reservas', name='reservas'),
    url(r'^contacto/', 'app.views.contacto', name='contacto'),
    url(r'^admin/', include(admin.site.urls)),
)
