# flake8: noqa
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog_db',
        'USER': 'blog_user',
        'PASSWORD':'!23qweASD',
        'HOST': 'db',
    }
}
