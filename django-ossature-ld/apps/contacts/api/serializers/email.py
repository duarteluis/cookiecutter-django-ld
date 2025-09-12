from rest_framework import serializers
from apps.contacts.models.customer import CustomerEmail
from apps.contacts.models.supplier import SupplierEmail


class CustomerEmailSerializer(serializers.ModelSerializer):
    """Serializer for customer email addresses."""

    class Meta:
        model = CustomerEmail
        fields = "__all__"
        read_only_fields = ["created", "updated", "created_by", "updated_by"]


class SupplierEmailSerializer(serializers.ModelSerializer):
    """Serializer for supplier email addresses."""

    class Meta:
        model = SupplierEmail
        fields = "__all__"
        read_only_fields = ["created", "updated", "created_by", "updated_by"]
