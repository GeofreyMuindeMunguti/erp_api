from rest_framework import serializers
from .models import Project, ProcurementTeam, HealthDocumentsCivilTeam, AccessApprovalCivil, CivilWorksTeam, FoundationImage, BTSAndGeneatorSlabsImage, SiteWallingImage


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

    health_documents = HealthDocumentsCivilTeamSerializer(required=True, many=True)
    access_approvals_field = AccessApprovalCivilSerializer(required=True, many=True)
    foundation_and_curing_images = FoundationImageSerializer(required=True, many=True)
    bts_and_generator_slabs_images = BTSAndGeneatorSlabsImageSerializer(required=True, many=True)
    site_walling_images_field = SiteWallingImageSerializer(required=True, many=True)

    class Meta:
        model = CivilWorksTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')

    def create(self, validated_data):
        access_approval_datas = validated_data.pop('access_approvals_field')
        health_documents = validated_data.pop('health_documents')
        foundation_images = validated_data.pop('foundation_and_curing_images')
        slabs_images = validated_data.pop('bts_and_generator_slabs_images')
        walling_images = validated_data.pop('site_walling_images_field')
        civilworks = CivilWorksTeam.objects.create(**validated_data)
        for access_approval_data in access_approval_datas:
            access_approvals_field = AccessApprovalCivilSerializer.create(AccessApprovalCivilSerializer(), validated_data=access_approval_data)
            access_approvals_field.save()
            civilworks.access_approvals_field.add(access_approvals_field)
        for health_document in health_documents:
            health_documents = HealthDocumentsCivilTeamSerializer.create(HealthDocumentsCivilTeamSerializer(), validated_data=health_document)
            health_documents.save()
            civilworks.health_documents.add(health_documents)
        for foundation_image in foundation_images:
            foundation_image = FoundationImageSerializer.create(FoundationImageSerializer(), validated_data=foundation_image)
            foundation_image.save()
            civilworks.foundation_and_curing_images.add(foundation_image)
        for slabs_image in slabs_images:
            slabs_image = BTSAndGeneatorSlabsImageSerializer.create(BTSAndGeneatorSlabsImageSerializer(), validated_data=slabs_image)
            slabs_image.save()
            civilworks.bts_and_generator_slabs_images.add(slabs_image)
        for walling_image in walling_images:
            walling_image = SiteWallingImageSerializer.create(SiteWallingImageSerializer(), validated_data=walling_image)
            walling_image.save()
            civilworks.site_walling_images_field.add(walling_image)
        return civilworks
