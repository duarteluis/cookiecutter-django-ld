# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.accounts.models.user import CustomUser, UserProfileType
from apps.accounts.models.profiles import CustomerProfile, SupplierProfile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically creates a related profile based on the user's role when a new user is created.

    - CUSTOMER → creates a linked CustomerProfile
    - SUPPLIER → creates a linked SupplierProfile
    """
    if not created:
        return

    if instance.profile == UserProfileType.CUSTOMER:
        CustomerProfile.objects.create(user=instance)

    elif instance.profile == UserProfileType.SUPPLIER:
        SupplierProfile.objects.create(user=instance)
