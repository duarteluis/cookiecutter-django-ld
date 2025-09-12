from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

from apps.accounts.models import UserProfileType
from apps.accounts.models.profiles import CustomerProfile, SupplierProfile
from apps.accounts.api.serializers.profile import (
    CustomerProfileSerializer,
    SupplierProfileSerializer,
)


@extend_schema(
    summary="Profil de l'utilisateur connecté",
    description="Retourne le profil client ou fournisseur selon le rôle du compte connecté.",
    responses={
        200: OpenApiResponse(
            CustomerProfileSerializer, description="Profil client ou fournisseur"
        ),
        404: OpenApiResponse(description="Profil non trouvé ou rôle non supporté"),
    },
)
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user

        if user.profile == UserProfileType.CUSTOMER:
            try:
                profile = CustomerProfile.objects.select_related("user").get(user=user)
                return Response(CustomerProfileSerializer(profile).data)
            except CustomerProfile.DoesNotExist:
                raise NotFound("Customer profile not found.")

        elif user.profile == UserProfileType.SUPPLIER:
            try:
                profile = SupplierProfile.objects.select_related("user").get(user=user)
                return Response(SupplierProfileSerializer(profile).data)
            except SupplierProfile.DoesNotExist:
                raise NotFound("Supplier profile not found.")

        raise NotFound("Unknown or unsupported user profile.")
