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
    url(r'^admin/', include(admin.site.urls)),
)
