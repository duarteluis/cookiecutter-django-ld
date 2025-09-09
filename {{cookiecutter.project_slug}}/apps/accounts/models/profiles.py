# apps/accounts/models/profile.py
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.accounts.models.user import CustomUser
from apps.common.models import AuditModel
from encrypted_model_fields.fields import EncryptedCharField


class CustomerProfile(AuditModel):
    """
    Profil spécifique pour les utilisateurs ayant le rôle de client.
    Contient des informations professionnelles et une référence UUID publique.
    Hérite de AuditModel pour inclure created, modified, created_by, updated_by.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="customer_profile"
    )
    company_name = EncryptedCharField("Company name", max_length=255, blank=True)

    def __str__(self):
        return f"Customer profile for {self.user.email}"


class SupplierProfile(AuditModel):
    """
    Profil spécifique pour les utilisateurs ayant le rôle de fournisseur.
    Contient des informations professionnelles et une référence UUID publique.
    Hérite de AuditModel pour inclure created, modified, created_by, updated_by.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="supplier_profile"
    )
    company_name = EncryptedCharField("Company name", max_length=255, blank=True)

    def __str__(self):
        return f"Supplier profile for {self.user.email}"
