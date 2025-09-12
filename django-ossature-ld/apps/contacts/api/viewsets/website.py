from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.contacts.models.customer import CustomerWebsite
from apps.contacts.models.supplier import SupplierWebsite
from apps.accounts.api.serializers.profile import (
    CustomerWebsiteSerializer,
    SupplierWebsiteSerializer,
)


class CustomerWebsiteViewSet(viewsets.ModelViewSet):
    """Full CRUD viewset for customer websites."""

    queryset = CustomerWebsite.objects.all()
    serializer_class = CustomerWebsiteSerializer
    permission_classes = [IsAuthenticated]


class SupplierWebsiteViewSet(viewsets.ModelViewSet):
    """Full CRUD viewset for supplier websites."""

    queryset = SupplierWebsite.objects.all()
    serializer_class = SupplierWebsiteSerializer
    permission_classes = [IsAuthenticated]
