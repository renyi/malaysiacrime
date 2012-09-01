DEBUG          = False
TEMPLATE_DEBUG = False
# CSRF_COOKIE_DOMAIN = ""

# Change this !
SECRET_KEY     = 'r_j!-y#89b7ph$2%7yf(q8x5z9*&moq(q-dt^vmcl-&e*tap8@'

# Postgres
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mcrime",
        "USER": "",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "OPTIONS": {
            "autocommit": True,
        }
    }
}

# Mailer + Gmail
DEFAULT_FROM_EMAIL  = 'admin@home.org'
EMAIL_BACKEND       = 'mailer.backend.DbBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True

# pylibmc
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': [
#             '127.0.0.1:11211',
#             # '192.168.1.2:11211',
#             # '192.168.1.3:11211'
#         ],
#     }
# }

# Compressor
# COMPRESS_ENABLED     = True
# COMPRESS_CSS_FILTERS = [
#     'compressor.filters.css_default.CssAbsoluteFilter',
#     'compressor.filters.cssmin.CSSMinFilter',
# ]

# COMPRESS_JS_FILTERS = [
#     'compressor.filters.jsmin.JSMinFilter',
# ]
