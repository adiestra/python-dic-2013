from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hola/(?P<nombre>\w+)/?$', 'demo01.views.saludar', name='saludar'),
    url(r'^catalogo/(?P<cod_categoria>\d+)/producto/(?P<cod_producto>\d+)/?$', 'demo01.views.detalle_catalogo', name='detalle_catalogo'),
    url(r'^tienda2/catalogo/(?P<cod_categoria>\d+)/producto/(?P<cod_producto>\d+)/?$', 'demo01.views.detalle_catalogo', name='detalle_catalogo_02', kwargs={'plantilla': 'detalle_catalogo_02.html'}),
    url(r'^tienda3/catalogo/(?P<cod_categoria>\d+)/producto/(?P<cod_producto>\d+)/?$', 'demo01.views.detalle_catalogo_03', name='detalle_catalogo_02', kwargs={'plantilla': 'detalle_catalogo_03.html'}),
    url(r'^google/?', 'demo01.views.redirigir_a_google', name='google'),
    url(r'^catalogo/?', 'demo01.views.catalogo', name='catalogo'),
    url(r'^$', 'demo01.views.home', name='home'),
)
