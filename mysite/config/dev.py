from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+ed_o4gk1k=^kyi0pa%b970pr(*3l4u4u$7*)!1su^qkrx&mc)'

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}
