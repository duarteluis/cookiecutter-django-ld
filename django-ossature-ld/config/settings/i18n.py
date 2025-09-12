# settings/i18n.py

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/
from .base import BASE_DIR
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = "fr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ("fr", _("French")),
    ("en", _("English")),
    ("de", _("German")),
)

LANGUAGE_CODE = "en"

LOCALE_PATHS = [
    BASE_DIR / "config/base/locale",
]
