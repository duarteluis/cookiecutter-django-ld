from .base import env


# Email process ############################################################################
ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": env(
        "MAILGUN_SENDER_DOMAIN"
    ),  # your Mailgun domain, if needed
}

EMAIL_BACKEND = (
    "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
)
DEFAULT_FROM_EMAIL = env(
    "DEFAULT_FROM_EMAIL"
)  # if you don't already have this in settings
SERVER_EMAIL = env("SERVER_EMAIL")  # ditto (default from-email for Django errors)
EMAIL_OPTOLOGIC_RECEIVER = env("EMAIL_OPTOLOGIC_RECEIVER")
# End Email process #########################################################################
