from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.accounts.api.viewsets.profile import (
    CustomerProfileViewSet,
    SupplierProfileViewSet,
)
from apps.accounts.api.views.me import MeView

router = DefaultRouter()

# Profiles (read-only)
router.register(r"customers", CustomerProfileViewSet, basename="customer-profile")
router.register(r"suppliers", SupplierProfileViewSet, basename="supplier-profile")

urlpatterns = [
    path("me/", MeView.as_view(), name="user-me"),
    path("", include(router.urls)),
]
