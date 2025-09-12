from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.contacts.models.customer import CustomerPhone
from apps.contacts.models.supplier import SupplierPhone
from apps.accounts.api.serializers.profile import (
    CustomerPhoneSerializer,
    SupplierPhoneSerializer,
)


class CustomerPhoneViewSet(viewsets.ModelViewSet):
    """Full CRUD viewset for customer phone numbers."""

    queryset = CustomerPhone.objects.all()
    serializer_class = CustomerPhoneSerializer
    permission_classes = [IsAuthenticated]


class SupplierPhoneViewSet(viewsets.ModelViewSet):
    """Full CRUD viewset for supplier phone numbers."""

    queryset = SupplierPhone.objects.all()
    serializer_class = SupplierPhoneSerializer
    permission_classes = [IsAuthenticated]
