from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^mostrar_ip/?$', 'demo04.views.mostrar_ip', name='mostrar_ip'),
    url(r'^dashboard/?$', 'demo04.views.dashboard', name='dashboard'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/?', 'django.contrib.auth.views.login', kwargs={'template_name':'login.html'}, name='login'),
    url(r'^logout/?', 'django.contrib.auth.views.logout', kwargs={'template_name':'logout.html'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'demo04.views.hola', name='hola'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
        
    )

