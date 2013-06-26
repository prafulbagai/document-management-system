from django.conf.urls.defaults import *
from django.contrib.auth.views import login,logout

urlpatterns = patterns('', 
    
                       url(r'^list/$', 'apps.login.views.list', name='list'),
                       (r'^login/$', 'django.contrib.auth.views.login', {
    'template_name': 'login/login.html'}),
                       url(r'^register/$', 'apps.login.views.register', name='register'),
               #        url(r'^$', 'apps.login.views.delete', name='delete'),
                                            
                      )
