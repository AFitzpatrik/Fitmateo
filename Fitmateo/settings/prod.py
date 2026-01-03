from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "fitmateo",
        "USER": "fitmateo",
        "PASSWORD": "secret",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
