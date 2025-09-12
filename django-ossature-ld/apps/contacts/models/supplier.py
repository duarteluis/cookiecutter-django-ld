from django.db import models
from apps.common.models import (
    AddressModel,
    PhoneLinkModel,
    EmailLinkModel,
    WebLinkModel,
)
from apps.accounts.models.profiles import SupplierProfile


class SupplierAddress(AddressModel):
    supplier = models.ForeignKey(
        SupplierProfile, on_delete=models.CASCADE, related_name="addresses"
    )


class SupplierPhone(PhoneLinkModel):
    supplier = models.ForeignKey(
        SupplierProfile, on_delete=models.CASCADE, related_name="phones"
    )


class SupplierEmail(EmailLinkModel):
    supplier = models.ForeignKey(
        SupplierProfile, on_delete=models.CASCADE, related_name="emails"
    )


class SupplierWebsite(WebLinkModel):
    supplier = models.ForeignKey(
        SupplierProfile, on_delete=models.CASCADE, related_name="websites"
    )
