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
STATIC_URL = '/static/'

#location where django collect all static files
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# location where you will store your static files
STATICFILES_DIRS = [os.path.join(BASE_DIR,'moviesapp/static')
]
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'