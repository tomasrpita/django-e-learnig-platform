from decouple import config
from .base import *

DEBUG = False
ADMINS = [
    ("Tomás R. Pita", "tomasrpita@gmail.com"),
]

ALLOWED_HOSTS = [".educaproject.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": 5432,
    }
}


REDIS_URL = "redis://cache:6379"
CACHES["default"]["LOCATION"] = REDIS_URL
CHANNEL_LAYERS["default"]["CONFIG"]["hosts"] = [REDIS_URL]

ALLOWED_HOSTS = ["educaproject.com", "www.educaproject.com"]

SECRET_KEY = config("SECRET_KEY")

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
