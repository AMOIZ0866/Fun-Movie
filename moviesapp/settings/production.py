import os

import dj_database_url

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['fumovies.herokuapp.com']

DATABASES = {
    'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'moviesapp_pro',

        'USER': 'ps',

        'PASSWORD': '<password>',

        'HOST': 'localhost',

        'PORT': '5432',
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


