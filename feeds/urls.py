from django.conf.urls.defaults import *

from feeders import *


feeds = {
    'latest': LatestEntries,
    'commented' : CommentedEntries,
    'updated' : UpdatedEntries,
}

urlpatterns = patterns('',
    url(r'(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}, name='feeds-latest'),
)
