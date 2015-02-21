from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.views.generic.base import TemplateView, View
from finalweb.views import *
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view()),
                       url(r'^references/(?P<id>.+?)/$', SingleReferenceView.as_view()),
                       url(r'^references/$', ReferencesView.as_view()),
                       url(r'^contact/send/$', SendMail.as_view()),
                       url(r'^contact/$', ContactView.as_view()),

                       url(r'^admin/', include(admin.site.urls)),
                       )


if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL,
    #                       document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
