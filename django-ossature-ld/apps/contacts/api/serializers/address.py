from rest_framework import serializers
from apps.contacts.models.customer import CustomerAddress
from apps.contacts.models.supplier import SupplierAddress


class CustomerAddressSerializer(serializers.ModelSerializer):
    """Serializer for customer addresses."""

    class Meta:
        model = CustomerAddress
        fields = "__all__"
        read_only_fields = ["created", "updated", "created_by", "updated_by"]


class SupplierAddressSerializer(serializers.ModelSerializer):
    """Serializer for supplier addresses."""

    class Meta:
        model = SupplierAddress
        fields = "__all__"
        read_only_fields = ["created", "updated", "created_by", "updated_by"]
