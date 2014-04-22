#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
# importamos settings
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'hellodjango.views.home', name='home'),
                       # url(r'^hellodjango/', include('hellodjango.foo.urls')),
                       # Uncomment the admin/doc line below
                       #to enable admin documentation:
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       #o.0
                       url(r'^static/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),
                       url(r'^media/(?P<path>.*)$',
                           'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
                       #url(r'^$', 'campuskit.views.index'),
                       #url(r'^add/$', 'campuskit.views.dropbox'),
                       #incluyendo las urls de mi aplicacion home
                       url(r'^', include('hellodjango.apps.home.urls')),
                       )
