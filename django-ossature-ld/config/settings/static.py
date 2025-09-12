# settings/static.py
from .base import BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "config/public/static"
STATICFILES_DIRS = [
    BASE_DIR / "config/base/static",
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "config/public/media"
