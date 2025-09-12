from rest_framework import serializers
from apps.contacts.models.customer import CustomerWebsite
from apps.contacts.models.supplier import SupplierWebsite


class CustomerWebsiteSerializer(serializers.ModelSerializer):
    """Serializer for customer websites."""

    class Meta:
        model = CustomerWebsite
        fields = "__all__"
        read_only_fields = ["created", "updated", "created_by", "updated_by"]


class SupplierWebsiteSerializer(serializers.ModelSerializer):
    """Serializer for supplier websites."""

    class Meta:
        model = SupplierWebsite
        fields = "__all__"
        read_only_fields = ["created", "updated", "created_by", "updated_by"]
