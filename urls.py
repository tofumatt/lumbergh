from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.shortcuts import render


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import pdb; pdb.set_trace()

urlpatterns = patterns('',
    (r'', include('careers.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
    import pdb; pdb.set_trace()
