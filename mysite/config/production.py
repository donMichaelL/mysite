from .base import *


SECRET_KEY = os.environ.get('SECRET_KEY', True)


DEBUG = True


django_heroku.settings(locals())
