# flake8: noqa
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog_db',
        'USER': 'blog_user',
        'PASSWORD':'eix8Pipo5niegu2sie1i',
        'HOST': 'db',
    }
}
