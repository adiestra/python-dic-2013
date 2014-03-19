from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse

from django.contrib import admin
admin.autodiscover()

from contact.views import contact_page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo03.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contacto/?', contact_page, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)
