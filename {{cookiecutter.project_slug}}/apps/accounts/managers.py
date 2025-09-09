from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user manager for the CustomUser model.
    Handles user and superuser creation with email as the unique identifier.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            extra_fields (dict): Additional user fields.

        Raises:
            ValueError: If email is not provided.

        Returns:
            CustomUser: A newly created user instance.
        """
        if not email:
            raise ValueError(_("The Email field must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.

        Ensures:
            - is_staff is True
            - is_superuser is True
            - profile is set to ADMIN
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        # Lazy import to avoid circular dependency
        from .models import UserProfileType

        extra_fields.setdefault("profile", UserProfileType.ADMIN)

        return self.create_user(email, password, **extra_fields)
