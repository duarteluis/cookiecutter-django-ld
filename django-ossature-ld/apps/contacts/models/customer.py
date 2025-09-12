from django.db import models
from apps.common.models import (
    AddressModel,
    PhoneLinkModel,
    EmailLinkModel,
    WebLinkModel,
)
from apps.accounts.models.profiles import CustomerProfile


class CustomerAddress(AddressModel):
    customer = models.ForeignKey(
        CustomerProfile, on_delete=models.CASCADE, related_name="addresses"
    )


class CustomerPhone(PhoneLinkModel):
    customer = models.ForeignKey(
        CustomerProfile, on_delete=models.CASCADE, related_name="phones"
    )


class CustomerEmail(EmailLinkModel):
    customer = models.ForeignKey(
        CustomerProfile, on_delete=models.CASCADE, related_name="emails"
    )


class CustomerWebsite(WebLinkModel):
    customer = models.ForeignKey(
        CustomerProfile, on_delete=models.CASCADE, related_name="websites"
    )
