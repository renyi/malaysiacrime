from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from views import *


urlpatterns = patterns('',
    url(r'^subscribe/$', subscribe, name='monitor-subscribe'),
    url(r'^subscribe/done/$', direct_to_template, {'template': 'monitor/subscribe_done.html'}, name='monitor-subscribe-done'),

    url(r'^unsubscribe/(?P<uuid>[\w\d]{32})/$', unsubscribe, name='monitor-unsubscribe'),
    url(r'^unsubscribe/done/$', direct_to_template, {'template': 'monitor/unsubscribe_done.html'}, name='monitor-unsubscribe-done'),

    url(r'^info/(?P<uuid>[\w\d]{32})/$', information, name='monitor-info'),
)
