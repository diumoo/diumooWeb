from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.simple import redirect_to
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from diumooWeb.frontpage.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diumooWeb.views.home', name='home'),
    # url(r'^diumooWeb/', include('diumooWeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^/?$',index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sparkle/',include('diumooWeb.sparkle.urls')),
    url(r'^sponsors/$',sponsors),
    url(r'^donate/?$',donate),
    url(r'^qa/?$',qa),
    url(r'^.*$',redirect_to,{'url':'/'}),
)

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
