import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_custom_user_str_representation():
    user = User.objects.create_user(
        email="john.doe@example.com",
        password="securepass123",
        first_name="John",
        last_name="Doe",
    )
    assert str(user) == "john.doe@example.com (DOE John)"


@pytest.mark.django_db
def test_custom_user_full_name_and_short_name():
    user = User.objects.create_user(
        email="a@example.com", password="pass", first_name="alice", last_name="smith"
    )
    assert user.full_name == "Alice Smith"
    assert user.short_name == "Alice"


@pytest.mark.django_db
def test_custom_user_initials():
    user = User.objects.create_user(
        email="z@example.com",
        password="pass",
        first_name="Élise",
        last_name="de La Roche",
    )
    assert user.extract_initials() == "ÉDLR"
