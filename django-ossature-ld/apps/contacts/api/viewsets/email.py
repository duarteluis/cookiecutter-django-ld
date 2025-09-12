from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.contacts.models.customer import CustomerEmail
from apps.contacts.models.supplier import SupplierEmail
from apps.accounts.api.serializers.profile import (
    CustomerEmailSerializer,
    SupplierEmailSerializer,
)


class CustomerEmailViewSet(viewsets.ModelViewSet):
    """Full CRUD viewset for customer email addresses."""

    queryset = CustomerEmail.objects.all()
    serializer_class = CustomerEmailSerializer
    permission_classes = [IsAuthenticated]


class SupplierEmailViewSet(viewsets.ModelViewSet):
    """Full CRUD viewset for supplier email addresses."""

    queryset = SupplierEmail.objects.all()
    serializer_class = SupplierEmailSerializer
    permission_classes = [IsAuthenticated]
