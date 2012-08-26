from django.conf.urls.defaults import *

from feeders import *
# from django.contrib.syndication.views import Feed

feeds = {
    'latest': LatestEntries,
    'commented' : CommentedEntries,
    'updated' : UpdatedEntries,
}

urlpatterns = patterns('',
    url(r'(?P<url>.*).xml$', 'django.contrib.syndication.views.Feed', {'feed_dict': feeds}, name='feeds-latest'),
)
