# settings/apps.py
from .base import DEBUG

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    # Utility plugins
    "django_extensions",
    "django_countries",
    "phonenumber_field",
    "robots",
    "django_recaptcha",
    "django_tables2",
    "django_filters",
    "import_export",
    "crispy_forms",
    "crispy_bootstrap5",
    "versatileimagefield",
    "rosetta",
    "taggit",

    # Security section
    "pwned_passwords_django",
    "encrypted_model_fields",

    # The required `allauth` apps...
    "allauth",
    "allauth.account",
    # The MFA app:
    "allauth.mfa",
    "widget_tweaks",
    "allauth.usersessions",
]

LOCAL_APPS = [
    "apps.accounts",
    "apps.common",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
