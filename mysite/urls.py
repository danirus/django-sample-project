from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'mysite.views.http404'
handler500 = 'mysite.views.http500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns(
        "",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
        }),
    )
