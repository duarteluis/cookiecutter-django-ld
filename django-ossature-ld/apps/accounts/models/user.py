# apps/accounts/models/user.py

import uuid
import re

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.managers import CustomUserManager
from encrypted_model_fields.fields import EncryptedCharField
from apps.accounts.utils import extract_initials_from_name


class UserProfileType(models.TextChoices):
    """
    Defines the different types of user profiles.
    """

    CUSTOMER = "customer", _("Customer")
    ADMIN = "admin", _("Administrator")
    SUPPLIER = "supplier", _("Supplier")


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model using email as the unique identifier.
    Includes encrypted first and last names and a profile type.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_index=True
    )
    email = models.EmailField(_("email address"), unique=True, db_index=True)
    first_name = EncryptedCharField(_("first name"), max_length=150)
    last_name = EncryptedCharField(_("last name"), max_length=150)
    profile = models.CharField(
        _("Profile"),
        max_length=20,
        choices=UserProfileType.choices,
        default=UserProfileType.CUSTOMER,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    EMAIL_FIELD = "email"

    @property
    def full_name(self) -> str:
        """
        Returns the user's full name with capitalization.
        """
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @property
    def short_name(self) -> str:
        """
        Returns the user's first name with capitalization.
        """
        return self.first_name.capitalize()

    def extract_initials(self) -> str:
        """
        Returns the uppercase initials of the user's full name,
        using a shared utility function.
        """
        return extract_initials_from_name(self.full_name)

    def get_email_field_name(self) -> str:
        return "email"

    def __str__(self):
        """
        String representation of the user, showing the email and formatted name.
        """
        if self.last_name and self.first_name:
            return f"{self.email} ({self.last_name.upper()} {self.first_name})"
        return self.email

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["email"]
