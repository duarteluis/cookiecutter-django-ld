# settings/middleware.py
from .base import DEBUG

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "apps.accounts.middleware.CurrentUserMiddleware",
    "pwned_passwords_django.middleware.pwned_passwords_middleware",

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",

    # Middlewares tiers
    # "utm_tracker.middleware.UtmSessionMiddleware",
    # "utm_tracker.middleware.LeadSourceMiddleware",
    # "apps.tracking.middleware.ActivityTrackingMiddleware",
    "allauth.usersessions.middleware.UserSessionsMiddleware",
    # "django_htmx.middleware.HtmxMiddleware",
]
