from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import (
    TimeStampedModel,
)  # Can be removed if replaced entirely
from model_utils import Choices
from django_countries.fields import CountryField
from phonenumber_field.phonenumber import PhoneNumber
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from encrypted_model_fields.fields import (
    EncryptedCharField,
    EncryptedEmailField,
)

from apps.accounts.middleware import get_current_user


# -----------------------------------------------------------------------------
# Base class with audit fields: authorship and timestamps
# -----------------------------------------------------------------------------
class AuditModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_created",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)s_updated",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk and not self.created_by:
            self.created_by = user
        self.updated_by = user
        super().save(*args, **kwargs)


# -----------------------------------------------------------------------------
# Abstract model for physical addresses, including encrypted fields
# -----------------------------------------------------------------------------
class AddressModel(AuditModel):
    TITLE_CHOICE = Choices(
        (1, "private", _("private")),
        (2, "professional", _("professional")),
        (3, "other", _("other")),
    )

    title = models.IntegerField(choices=TITLE_CHOICE, default=TITLE_CHOICE.private)
    address_line1 = EncryptedCharField(_("Address line 1"), max_length=45)
    address_line2 = EncryptedCharField(_("Address line 2"), max_length=45, blank=True)
    postal_code = EncryptedCharField(_("Postal code"), max_length=45)
    city = EncryptedCharField(_("City"), max_length=45)
    state = EncryptedCharField(_("State"), max_length=45, blank=True, null=True)
    country = CountryField()
    latitude = EncryptedCharField(_("Latitude"), max_length=45, blank=True, null=True)
    longitude = EncryptedCharField(_("Longitude"), max_length=45, blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.postal_code} - {self.city}"

    class Meta:
        abstract = True


# -----------------------------------------------------------------------------
# Abstract model for phone contact details, with encryption and labeling
# -----------------------------------------------------------------------------
class PhoneLinkModel(AuditModel):
    PHONE_TYP_CHOICE = Choices(
        (1, "cellular", _("cell phone")),
        (2, "phone", _("phone")),
        (3, "fax", _("fax machine")),
    )

    TITLE_CHOICE = Choices(
        (1, "private", _("private")),
        (2, "professional", _("professional")),
        (3, "other", _("other")),
    )

    device_type = models.IntegerField(
        choices=PHONE_TYP_CHOICE, default=PHONE_TYP_CHOICE.phone
    )
    title = models.IntegerField(choices=TITLE_CHOICE, default=TITLE_CHOICE.private)
    number = EncryptedCharField(blank=True)
    default_sms_phone_number = models.BooleanField(default=False)

    def get_phone_link_url(self):
        if self.number:
            return f'<a href="tel:{self.number}">{self.number}</a>'
        return ""

    def __str__(self):
        return f"{self.title} ({self.get_device_type_display()}) | {self.number}"

    class Meta:
        abstract = True


# -----------------------------------------------------------------------------
# Abstract model for email contact details, with encrypted email field
# -----------------------------------------------------------------------------
class EmailLinkModel(AuditModel):
    TITLE_CHOICE = Choices(
        (1, "private", _("private")),
        (2, "professional", _("professional")),
        (3, "other", _("other")),
    )

    title = models.IntegerField(choices=TITLE_CHOICE, default=TITLE_CHOICE.private)
    email = EncryptedEmailField(blank=True)
    default = models.BooleanField(default=False)

    def get_email_link_url(self):
        return f'<a href="mailto:{self.email}">{self.email}</a>'

    def __str__(self):
        return f"{self.title} ({self.email})"

    class Meta:
        abstract = True


# -----------------------------------------------------------------------------
# Abstract model for websites, with validation for proper URL format
# -----------------------------------------------------------------------------
class WebLinkModel(AuditModel):
    TITLE_CHOICE = Choices(
        (1, "private", _("private")),
        (2, "professional", _("professional")),
        (3, "other", _("other")),
    )

    title = models.IntegerField(choices=TITLE_CHOICE, default=TITLE_CHOICE.private)
    website = models.URLField(blank=True)

    def clean(self):
        super().clean()
        if self.website:
            validator = URLValidator()
            try:
                validator(self.website)
            except ValidationError:
                raise ValidationError({"website": _("Enter a valid website URL.")})

    def get_web_link_url(self):
        return f'<a href="{self.website}">{self.website}</a>'

    def __str__(self):
        return f"{self.title} ({self.website})"

    class Meta:
        abstract = True
