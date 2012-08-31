from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('main.urls')),
    (r'^crime/', include('crime.urls')),
    (r'^monitor/', include('monitor.urls')),
    (r'^feeds/', include('feeds.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^admin/', include(admin.site.urls)),
)

# Default robots.txt
if not settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
    )

# Media and Static files for development
if settings.DEBUG:
    # Static files
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    # Media files
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
