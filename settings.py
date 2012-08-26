# Django settings for malaysiacrime project.

ADMINS = (
    ('Kegan Gan', 'kegan@kegan.info'),
    ('Renyi Khor', 'renyi.ace@gmail.com'),
)
MANAGERS = ADMINS

DEBUG = False
TEMPLATE_DEBUG = False

SITE_ID                         = 1
USE_TZ                          = True
TIME_ZONE                       = 'Asia/Kuala_Lumpur'
LANGUAGE_CODE                   = 'en-us'
USE_I18N                        = False
USE_L10N                        = False
INTERNAL_IPS                    = ("127.0.0.1",)
SESSION_ENGINE                  = 'django.contrib.sessions.backends.cached_db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DATABASE_ENGINE   = ''
DATABASE_NAME     = ''
DATABASE_USER     = ''
DATABASE_PASSWORD = ''
DATABASE_HOST     = ''
DATABASE_PORT     = ''

TIME_INPUT_FORMATS = (
    '%I:%M %p', '%H:%M:%S', '%H:%M'
)

DATE_INPUT_FORMATS = (
    '%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y', '%b %d %Y',
    '%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y',
    '%B %d, %Y', '%d %B %Y', '%d %B, %Y'
)

DATETIME_INPUT_FORMATS = (
    '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d',
    '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y',
    '%d/%m/%y %H:%M:%S', '%d/%m/%y %H:%M', '%d/%m/%y'
)

#########
# PATHS #
#########
import os

PROJECT_ROOT    = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
PROJECT_DIR     = os.path.dirname(__file__)

ROOT_URLCONF                = '%s.urls' % PROJECT_DIRNAME
CACHE_MIDDLEWARE_KEY_PREFIX = '%s' % PROJECT_DIRNAME
CACHE_MIDDLEWARE_ALIAS      = '%s' % PROJECT_DIRNAME
# CSRF_COOKIE_DOMAIN          = ".redbox.com.my"
CSRF_COOKIE_NAME            = '%scsrftoken' % PROJECT_DIRNAME
LANGUAGE_COOKIE_NAME        = '%slanguage' % PROJECT_DIRNAME
SESSION_COOKIE_NAME         = '%ssession' % PROJECT_DIRNAME

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': [
#             '127.0.0.1:11211',
#         ],
#         'KEY_PREFIX': '%s' % PROJECT_DIRNAME,
#     }
# }

STATIC_DIR  = '/opt/static/'
STATIC_URL  = '/static/'
STATIC_ROOT = '%sstatic/' % STATIC_DIR
MEDIA_ROOT  = '%smedia/%s/' % (STATIC_DIR, PROJECT_DIRNAME)
MEDIA_URL   = '/media/%s/' % PROJECT_DIRNAME

# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '----i-am-not-telling-you---'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
)

MIDDLEWARE_CLASSES = (
    'malaysiacrime.SetRemoteAddrFromForwardedFor',
    'django.middleware.cache.UpdateCacheMiddleware',
    "django.middleware.common.CommonMiddleware",
    'django.middleware.cache.FetchFromCacheMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    # "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'malaysiacrime.urls'

TEMPLATE_DIRS = (
    # os.path.join(PROJECT_DIR, 'templates')
)

INSTALLED_APPS = [
    "crime_template",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    'django.contrib.humanize',
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.sitemaps',

    # Django apps
    'south',
    "mailer",
    # "mptt",
    # "tastypie",
    # "debug_toolbar",
    # "django_extensions",
    # "compressor",

    # Malaysian Crime
    'crime',
    'main',
    'monitor',
]

# CACHE Middleware
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_MIDDLEWARE_SECONDS        = 600

# Email
EMAIL_BACKEND       = 'mailer.backend.DbBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True

# Django compressor
# COMPRESS_ENABLED     = True
# COMPRESS_CSS_FILTERS = [
#     'compressor.filters.css_default.CssAbsoluteFilter',
#     'compressor.filters.cssmin.CSSMinFilter',
# ]

# COMPRESS_JS_FILTERS = [
#     'compressor.filters.jsmin.JSMinFilter',
# ]

# Celery
# BROKER_HOST     = "localhost"
# BROKER_PORT     = 5672
# BROKER_USER     = ""
# BROKER_PASSWORD = ""
# BROKER_VHOST    = ""

# CELERY_IMPORTS = []

# import djcelery
# djcelery.setup_loader()
# INSTALLED_APPS += ["djcelery",]

try:
    # Developers settings.
    from local_settings import *
except ImportError:
    pass

try:
    # Deployment settings
    from live_settings import *
except ImportError:
    pass
