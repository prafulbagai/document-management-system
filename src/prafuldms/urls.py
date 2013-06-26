from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^', include('apps.login.urls')),
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.normpath( os.path.join( os.path.dirname(__file__),'../static/'))})
    # Examples:
    # url(r'^$', 'prafuldms.views.home', name='home'),
    # url(r'^prafuldms/', include('prafuldms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)