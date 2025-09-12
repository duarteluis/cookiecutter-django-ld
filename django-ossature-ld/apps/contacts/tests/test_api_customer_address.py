import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.accounts.models.user import UserProfileType
from apps.accounts.models.profiles import CustomerProfile
from apps.contacts.models.customer import CustomerAddress


@pytest.mark.django_db
def test_authenticated_customer_can_create_address():
    user = (
        CustomerProfile.objects.first().user
        if CustomerProfile.objects.exists()
        else CustomerProfile.objects.create(user=create_test_user("client")).user
    )
    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse(
        "customer-addresses-list", kwargs={"customer_pk": user.customerprofile.pk}
    )
    payload = {
        "address_line1": "123 Rue de Lyon",
        "postal_code": "1000",
        "city": "Lausanne",
        "country": "CH",
    }

    response = client.post(url, payload, format="json")
    assert response.status_code == 201
    assert CustomerAddress.objects.filter(customer__user=user).count() == 1


@pytest.mark.django_db
def test_customer_cannot_access_another_customer_addresses():
    user1 = create_test_user("client1")
    user2 = create_test_user("client2")
    CustomerProfile.objects.get_or_create(user=user1)
    profile2 = CustomerProfile.objects.get_or_create(user=user2)[0]

    # Create address for user2
    CustomerAddress.objects.create(
        customer=profile2,
        address_line1="123 Rue",
        postal_code="1000",
        city="Genève",
        country="CH",
    )

    client = APIClient()
    client.force_authenticate(user=user1)
    url = reverse("customer-addresses-list", kwargs={"customer_pk": profile2.pk})

    response = client.get(url)
    assert response.status_code in [403, 404]  # depending on your permission strategy


def create_test_user(email_prefix):
    from django.contrib.auth import get_user_model

    User = get_user_model()
    return User.objects.create_user(
        email=f"{email_prefix}@example.com",
        password="pass",
        first_name=email_prefix.capitalize(),
        last_name="Test",
        profile=UserProfileType.CUSTOMER,
    )
