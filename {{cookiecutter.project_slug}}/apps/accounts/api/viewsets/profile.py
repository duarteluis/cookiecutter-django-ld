from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models.profiles import CustomerProfile, SupplierProfile
from apps.accounts.api.serializers.profile import (
    CustomerProfileSerializer,
    SupplierProfileSerializer,
)


class CustomerProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only viewset for customer profiles with user and contact data."""

    queryset = CustomerProfile.objects.select_related("user").all()
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsAuthenticated]


class SupplierProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only viewset for supplier profiles with user and contact data."""

    queryset = SupplierProfile.objects.select_related("user").all()
    serializer_class = SupplierProfileSerializer
    permission_classes = [IsAuthenticated]
