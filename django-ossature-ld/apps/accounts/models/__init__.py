# apps.accounts/models/__init__.py
from .user import CustomUser, UserProfileType
from .profiles import CustomerProfile, SupplierProfile

__all__ = ["CustomUser", "CustomerProfile", "SupplierProfile", "UserProfileType"]
