import pytest
from django.contrib.auth import get_user_model
from apps.accounts.models.user import UserProfileType
from apps.accounts.models.profiles import CustomerProfile, SupplierProfile

User = get_user_model()


@pytest.mark.django_db
def test_customer_profile_created_on_user_creation():
    user = User.objects.create_user(
        email="client@example.com",
        password="pass",
        first_name="Jean",
        last_name="Client",
        profile=UserProfileType.CUSTOMER,
    )
    assert CustomerProfile.objects.filter(user=user).exists()


@pytest.mark.django_db
def test_supplier_profile_created_on_user_creation():
    user = User.objects.create_user(
        email="supplier@example.com",
        password="pass",
        first_name="Fournisseur",
        last_name="X",
        profile=UserProfileType.SUPPLIER,
    )
    assert SupplierProfile.objects.filter(user=user).exists()


@pytest.mark.django_db
def test_no_profile_created_for_admin_user():
    user = User.objects.create_user(
        email="admin@example.com",
        password="adminpass",
        first_name="Admin",
        last_name="User",
        profile=UserProfileType.ADMIN,
    )
    assert not CustomerProfile.objects.filter(user=user).exists()
    assert not SupplierProfile.objects.filter(user=user).exists()
