# settings/database.py
import os
from .base import BASE_DIR, env

# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

if os.environ.get("DJANGO_DEBUG", "dev") == "prod":
    DATABASES = {
        "default": env.db(),
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
