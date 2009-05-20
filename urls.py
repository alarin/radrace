from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Serve static media
    (r'^(?P<path>.*\.(js|gm4ie|css|xls|ico|png|gif|jpg|doc))$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^(?P<path>.*writable/.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Example:
    # (r'^radrace_django/', include('radrace_django.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
