import pytest
from apps.accounts.models.user import CustomUser, UserProfileType
from apps.accounts.models.profiles import CustomerProfile, SupplierProfile
from apps.contacts.models.customer import CustomerAddress, CustomerPhone
from apps.contacts.models.supplier import SupplierEmail, SupplierWebsite


@pytest.mark.django_db
def test_customer_can_have_multiple_addresses():
    user = CustomUser.objects.create_user(
        email="customer@example.com",
        password="pass",
        first_name="Alice",
        last_name="C",
        profile=UserProfileType.CUSTOMER,
    )
    customer = CustomerProfile.objects.get(user=user)
    for i in range(3):
        CustomerAddress.objects.create(
            customer=customer,
            address_line1=f"Rue {i}",
            postal_code="1000",
            city="Lausanne",
            country="CH",
        )
    assert customer.addresses.count() == 3


@pytest.mark.django_db
def test_supplier_can_have_multiple_contacts():
    user = CustomUser.objects.create_user(
        email="supplier@example.com",
        password="pass",
        first_name="Bob",
        last_name="F",
        profile=UserProfileType.SUPPLIER,
    )
    supplier = SupplierProfile.objects.get(user=user)

    SupplierEmail.objects.create(supplier=supplier, email="contact1@example.com")
    SupplierWebsite.objects.create(supplier=supplier, website="https://supplier.com")

    assert supplier.emails.count() == 1
    assert supplier.websites.count() == 1
