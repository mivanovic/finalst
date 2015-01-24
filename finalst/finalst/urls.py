from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.views.generic.base import TemplateView
from finalweb.views import *
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$', 'finalweb.views.index', name='index'),
                       url(r'^references/(?P<reference>.+?)/$', 'finalweb.views.single_reference', name='references'),
                       url(r'^references/$', 'finalweb.views.references', name='references'),
                       url(r'^contact/send/$', send_email),
                       url(r'^contact/$', 'finalweb.views.contact', name='contact'),

                       url(r'^admin/', include(admin.site.urls)),
                       )


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
