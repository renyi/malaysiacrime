DEBUG            = True
TEMPLATE_DEBUG   = True
COMPRESS_ENABLED = False

SECRET_KEY       = 'r_j!-y#89b7ph$2%7yf(q8x5z9*&moq(q-dt^vmcl-&e*tap8@'

EMAIL_BACKEND       = 'mailer.backend.DbBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT          = 587
EMAIL_USE_TLS       = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
