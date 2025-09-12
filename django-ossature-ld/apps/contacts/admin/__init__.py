from django.contrib import admin
from apps.contacts.models.customer import (
    CustomerAddress,
    CustomerPhone,
    CustomerEmail,
    CustomerWebsite,
)
from apps.contacts.models.supplier import (
    SupplierAddress,
    SupplierPhone,
    SupplierEmail,
    SupplierWebsite,
)


class ContactInline(admin.TabularInline):
    extra = 0
    show_change_link = True


class CustomerAddressInline(ContactInline):
    model = CustomerAddress


class CustomerPhoneInline(ContactInline):
    model = CustomerPhone


class CustomerEmailInline(ContactInline):
    model = CustomerEmail


class CustomerWebsiteInline(ContactInline):
    model = CustomerWebsite


class SupplierAddressInline(ContactInline):
    model = SupplierAddress


class SupplierPhoneInline(ContactInline):
    model = SupplierPhone


class SupplierEmailInline(ContactInline):
    model = SupplierEmail


class SupplierWebsiteInline(ContactInline):
    model = SupplierWebsite


# Tu peux aussi enregistrer les modèles individuellement si tu ne fais pas d’inline.
for model in [
    CustomerAddress,
    CustomerPhone,
    CustomerEmail,
    CustomerWebsite,
    SupplierAddress,
    SupplierPhone,
    SupplierEmail,
    SupplierWebsite,
]:
    admin.site.register(model)
