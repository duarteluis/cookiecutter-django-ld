from rest_framework import serializers
from apps.contacts.models.customer import CustomerPhone
from apps.contacts.models.supplier import SupplierPhone


class CustomerPhoneSerializer(serializers.ModelSerializer):
    """Serializer for customer phone numbers."""

    class Meta:
        model = CustomerPhone
        fields = "__all__"
        read_only_fields = ["created", "updated", "created_by", "updated_by"]


class SupplierPhoneSerializer(serializers.ModelSerializer):
    """Serializer for supplier phone numbers."""

    class Meta:
        model = SupplierPhone
        fields = "__all__"
        read_only_fields = ["created", "updated", "created_by", "updated_by"]
