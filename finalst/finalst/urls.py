from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'finalweb.views.index', name='index'),
    url(r'^contact/$', 'finalweb.views.contact', name='contact'),
    url(r'^news/$', 'finalweb.views.news', name='news'),
    url(r'^aboutus/$', 'finalweb.views.aboutus', name='aboutus'),
    url(r'^services/$', 'finalweb.views.services', name='services'),
    url(r'^gallery/$', 'finalweb.views.gallery', name='gallery'),
    url(r'^references/$', 'finalweb.views.references', name='references'),
    url(r'^services/(?P<page_alias>.+?)/$', 'finalweb.views.static_page'),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
							document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
							document_root = settings.MEDIA_ROOT)
