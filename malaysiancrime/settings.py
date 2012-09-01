DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Kegan Gan', 'kegan@kegan.info'),
    ('Renyi Khor', 'renyi.ace@gmail.com'),
)
MANAGERS = ADMINS

SITE_ID                         = 1
USE_TZ                          = True
TIME_ZONE                       = 'Asia/Kuala_Lumpur'
LANGUAGE_CODE                   = 'en-us'
USE_I18N                        = False
USE_L10N                        = False
INTERNAL_IPS                    = ("127.0.0.1",)
SESSION_ENGINE                  = 'django.contrib.sessions.backends.cached_db'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
WSGI_APPLICATION                = 'malaysiancrime.wsgi.application'

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
CSRF_COOKIE_NAME            = '%scsrftoken' % PROJECT_DIRNAME
LANGUAGE_COOKIE_NAME        = '%slanguage' % PROJECT_DIRNAME
SESSION_COOKIE_NAME         = '%ssession' % PROJECT_DIRNAME

STATIC_DIR  = '/opt/static/'
STATIC_URL  = '/static/'
STATIC_ROOT = '%sstatic/' % STATIC_DIR
MEDIA_ROOT  = '%smedia/%s/' % (STATIC_DIR, PROJECT_DIRNAME)
MEDIA_URL   = '/media/%s/' % PROJECT_DIRNAME

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
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
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    # "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'malaysiancrime.urls'

TEMPLATE_DIRS = (
    # os.path.join(PROJECT_DIR, 'templates')
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    'django.contrib.messages',
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    'django.contrib.humanize',
    'django.contrib.comments',
    'django.contrib.markup',

    # Django apps
    'south',
    # "mailer",
    # "compressor",
    # "tastypie",
    # "debug_toolbar",
    # "django_extensions",

    # Malaysian Crime,
    'malaysiancrime',
    'malaysiancrime.crime',
    'malaysiancrime.main',
    'malaysiancrime.monitor',
]

# CACHE Middleware
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_MIDDLEWARE_SECONDS        = 600

from local_settings import *

try:
    # Developers settings
    pass
except ImportError:
    pass

try:
    # Deployment settings
    from live_settings import *
except ImportError:
    pass
