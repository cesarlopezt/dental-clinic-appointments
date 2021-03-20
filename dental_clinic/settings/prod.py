import os
import dj_database_url

from .base import BASE_DIR, MIDDLEWARE, DATABASES

# SECRET_KEY = os.environ['SECRET_KEY']

# DEBUG = False

ALLOWED_HOSTS = ['*']

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)


MIDDLEWARE = MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
