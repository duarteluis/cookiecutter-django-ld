import pytest
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

User = get_user_model()


@pytest.mark.django_db
class TestCustomUserManager:

    def test_create_user_success(self):
        user = User.objects.create_user(
            email="user@example.com",
            password="securepassword123",
            first_name="John",
            last_name="Doe",
        )
        assert user.email == "user@example.com"
        assert user.check_password("securepassword123")
        assert user.is_active is True
        assert user.is_staff is False
        assert user.is_superuser is False

    def test_create_user_without_email_raises_error(self):
        with pytest.raises(ValueError) as exc_info:
            User.objects.create_user(email="", password="password123")
        assert "The Email field must be set" in str(exc_info.value)

    def test_create_superuser_success(self):
        admin = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpass123",
            first_name="Alice",
            last_name="Smith",
        )
        assert admin.is_superuser is True
        assert admin.is_staff is True

    def test_create_superuser_with_invalid_flags_raises_error(self):
        with pytest.raises(ValueError) as exc_info:
            User.objects.create_superuser(
                email="admin2@example.com", password="adminpass123", is_superuser=False
            )
        assert "Superuser must have is_superuser=True." in str(exc_info.value)

        with pytest.raises(ValueError) as exc_info:
            User.objects.create_superuser(
                email="admin3@example.com", password="adminpass123", is_staff=False
            )
        assert "Superuser must have is_staff=True." in str(exc_info.value)
