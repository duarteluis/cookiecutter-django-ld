from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models.user import CustomUser, UserProfileType
from .models import CustomerProfile, SupplierProfile

from apps.contacts.models.customer import CustomerAddress


class CustomerAddressInline(admin.TabularInline):
    model = CustomerAddress
    extra = 0
    fields = ("title", "address_line1", "postal_code", "city", "country")
    show_change_link = True


class CustomerProfileInline(admin.StackedInline):
    model = CustomerProfile
    can_delete = False
    verbose_name = _("Customer Profile")
    verbose_name_plural = _("Customer Profile")
    fk_name = "user"
    extra = 0


class SupplierProfileInline(admin.StackedInline):
    model = SupplierProfile
    can_delete = False
    verbose_name = _("Supplier Profile")
    verbose_name_plural = _("Supplier Profile")
    fk_name = "user"
    extra = 0


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "company_name",
    )
    list_filter = ("user__is_staff", "user__is_active")
    search_fields = ("user__email", "user__first_name", "user__last_name")
    readonly_fields = ("created_by", "updated_by")
    ordering = ("user__email",)
    inlines = [CustomerAddressInline]


@admin.register(SupplierProfile)
class SupplierProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "company_name",
    )
    list_filter = ("user__is_staff", "user__is_active")
    search_fields = ("user__email", "user__first_name", "user__last_name")
    readonly_fields = ("created_by", "updated_by")
    ordering = ("user__email",)


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """
    Administration du CustomUser avec affichage conditionnel du profil client ou fournisseur.
    """

    model = CustomUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "profile",
        "is_staff",
        "is_active",
        "view_user_profile_link",
    )
    list_filter = ("is_staff", "is_active", "profile")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    fieldsets = (
        (_("Informations de connexion"), {"fields": ("email", "password")}),
        (
            _("Informations personnelles"),
            {"fields": ("first_name", "last_name", "profile")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "profile",
                ),
            },
        ),
    )

    inlines = [CustomerProfileInline, SupplierProfileInline]

    def view_user_profile_link(self, obj):
        if obj.profile == UserProfileType.CUSTOMER and hasattr(obj, "customer_profile"):
            url = f"/admin/accounts/customerprofile/{obj.customer_profile.id}/change/"
            return format_html('<a href="{}">{}</a>', url, _("Voir le profil"))
        if obj.profile == UserProfileType.SUPPLIER and hasattr(obj, "supplier_profile"):
            url = f"/admin/accounts/supplierprofile/{obj.supplier_profile.id}/change/"
            return format_html('<a href="{}">{}</a>', url, _("Voir le profil"))
        return "-"

    view_user_profile_link.short_description = _("Profil user (customer or supplier")
