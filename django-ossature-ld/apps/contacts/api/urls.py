from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.contacts.api.viewsets.address import (
    CustomerAddressViewSet,
    SupplierAddressViewSet,
)
from apps.contacts.api.viewsets.phone import CustomerPhoneViewSet, SupplierPhoneViewSet
from apps.contacts.api.viewsets.email import CustomerEmailViewSet, SupplierEmailViewSet
from apps.contacts.api.viewsets.website import (
    CustomerWebsiteViewSet,
    SupplierWebsiteViewSet,
)

router = DefaultRouter()

# Customer resources
router.register(
    r"customers/addresses", CustomerAddressViewSet, basename="customer-address"
)
router.register(r"customers/phones", CustomerPhoneViewSet, basename="customer-phone")
router.register(r"customers/emails", CustomerEmailViewSet, basename="customer-email")
router.register(
    r"customers/websites", CustomerWebsiteViewSet, basename="customer-website"
)

# Supplier resources
router.register(
    r"suppliers/addresses", SupplierAddressViewSet, basename="supplier-address"
)
router.register(r"suppliers/phones", SupplierPhoneViewSet, basename="supplier-phone")
router.register(r"suppliers/emails", SupplierEmailViewSet, basename="supplier-email")
router.register(
    r"suppliers/websites", SupplierWebsiteViewSet, basename="supplier-website"
)

urlpatterns = [
    path("", include(router.urls)),
]
