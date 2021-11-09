from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': env('DATABASE'),

        'USER': env('USER'),

        'PASSWORD': env('PASSWORD'),

        'HOST': env('HOST'),

        'PORT': env('PORT'),
    }
}


