from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('malaysiancrime.main.urls')),
    (r'^crime/', include('malaysiancrime.crime.urls')),
    (r'^monitor/', include('malaysiancrime.monitor.urls')),
    (r'^feeds/', include('malaysiancrime.feeds.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^admin/', include(admin.site.urls)),
)

# Media and Static files for development
if settings.DEBUG:
    # Static files
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    # Media files
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
