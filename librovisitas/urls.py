from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'principal.views.index', name='index'),
    url(r'^libro/$', 'principal.views.libro', name='libro'),
    url(r'nuevo_comentario', 'principal.views.nuevo_comentario'),
)
