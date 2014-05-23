from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'libro.views.home'),
    url(r'^ejemplo/variables/$', 'libro.views.ejemplo'),
    url(r'^form/contacto/mas/$', 'libro.views.form'),

    url(r'^index/$', 'libro.views.index'),
    
    #USUARIOS
    url(r'^usuario/new/$', 'usuarios.views.nuevo_usuario'),
    url(r'^usuario/login/$', 'usuarios.views.iniciar_sesion'),
    url(r'^usuario/salir/$', 'usuarios.views.cerrar_sesion'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
