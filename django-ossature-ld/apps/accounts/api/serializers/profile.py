from rest_framework import serializers
from apps.accounts.models.profiles import CustomerProfile, SupplierProfile

from apps.contacts.api.serializers.address import (
    CustomerAddressSerializer,
    SupplierAddressSerializer,
)
from apps.contacts.api.serializers.phone import (
    CustomerPhoneSerializer,
    SupplierPhoneSerializer,
)
from apps.contacts.api.serializers.email import (
    CustomerEmailSerializer,
    SupplierEmailSerializer,
)
from apps.contacts.api.serializers.website import (
    CustomerWebsiteSerializer,
    SupplierWebsiteSerializer,
)


class CustomerProfileSerializer(serializers.ModelSerializer):
    """Serializer for customer profile enriched with user and contact data."""

    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    addresses = CustomerAddressSerializer(many=True, read_only=True)
    phones = CustomerPhoneSerializer(many=True, read_only=True)
    emails = CustomerEmailSerializer(many=True, read_only=True)
    websites = CustomerWebsiteSerializer(many=True, read_only=True)

    class Meta:
        model = CustomerProfile
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "addresses",
            "phones",
            "emails",
            "websites",
            "created",
            "updated",
        ]


class SupplierProfileSerializer(serializers.ModelSerializer):
    """Serializer for supplier profile enriched with user and contact data."""

    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    addresses = SupplierAddressSerializer(many=True, read_only=True)
    phones = SupplierPhoneSerializer(many=True, read_only=True)
    emails = SupplierEmailSerializer(many=True, read_only=True)
    websites = SupplierWebsiteSerializer(many=True, read_only=True)

    class Meta:
        model = SupplierProfile
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "addresses",
            "phones",
            "emails",
            "websites",
            "created",
            "updated",
        ]
