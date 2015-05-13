from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PythonWorkSpace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')