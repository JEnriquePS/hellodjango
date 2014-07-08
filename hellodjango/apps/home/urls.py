from django.conf.urls import patterns, url

urlpatterns = patterns('hellodjango.apps.home.views',
    url(r'^$', 'jenriqueps_view', name='vista_jenriqueps'),
    url(r'^about/$', 'about_view', name='vista_about'),
    url(r'^productos/$', 'productos_view',name='vista_productos'),
    url(r'^contacto/$', 'contacto_view',name='vista_Contactos'),
    url(r'^jenriqueps/$', 'index_view',name='vista_principal'),
)
