from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.contacts.models.customer import CustomerAddress
from apps.contacts.models.supplier import SupplierAddress
from apps.accounts.api.serializers.profile import (
    CustomerAddressSerializer,
    SupplierAddressSerializer,
)


class CustomerAddressViewSet(viewsets.ModelViewSet):
    """Full CRUD viewset for customer addresses."""

    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
    permission_classes = [IsAuthenticated]


class SupplierAddressViewSet(viewsets.ModelViewSet):
    """Full CRUD viewset for supplier addresses."""

    queryset = SupplierAddress.objects.all()
    serializer_class = SupplierAddressSerializer
    permission_classes = [IsAuthenticated]
