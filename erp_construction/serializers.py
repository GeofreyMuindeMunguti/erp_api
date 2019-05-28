from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import CustomUser
from .models import *
from rest_framework.authtoken.models import Token


class ProjectIconsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectIcons
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProcurementTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcurementTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProjectCostingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectCosting
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ProjectPurchaseOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectPurchaseOrders
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class CommercialTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommercialTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class HealthDocumentsCivilTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthDocumentsCivilTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class AccessApprovalCivilSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalCivil
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class FoundationImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoundationImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SiteClearingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SetSiteClearingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class TowerBaseImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TowerBaseImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BindingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BindingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SteelFixFormworkImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SteelFixFormworkImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ConcretePourCuringImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConcretePourCuringImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class BTSAndGeneatorSlabsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTSAndGeneatorSlabsImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class SiteWallingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteWallingImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class CivilWorksTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = CivilWorksTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class InstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class HealthDocumentsInstallationTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthDocumentsInstallationTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class AccessApprovalInstallationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessApprovalInstallation
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class RFAndLinkImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RFAndLinkImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class ElectricalImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricalImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class KPLCSolarImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPLCSolarImage
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
