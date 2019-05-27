from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from .models import *
from django.contrib.auth.models import User
from datetime import datetime

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status, viewsets
from rest_framework.decorators import parser_classes



class DefaultsMixin(object):

    """Default settings for view authentication, permissions,filtering and pagination."""
    """
    #view authentication
    #authentication_classes = (authentication.BasicAuthentication,authentication.TokenAuthentication,)
    # view  permissions,
    #permission_classes = (permissions.IsAuthenticated,)  # alow only authenticated user to access API End points
    # view  pagination.
    """

    paginate_by = 25     # Pages of API end points/URLs
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    """
    #view  filtering
    #DefaultsMixin now defines the list of available filter_backends , which will enable these for all of the existing ViewSets.
    """
    filter_backends = (filters.SearchFilter,)
    '''
    We configure the SearchFilter by adding a search_fields attribute to each
    ViewSet . We configure the OrderingFilter by adding a list of fields, which can be used
    for ordering the ordering_fields .
    '''

class ProjectViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = Project.objects.order_by('created_at')
    serializer_class = ProjectSerializer

    search_fields = ('project_name', )


class ProcurementTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating procurement team tasks."""
    queryset = ProcurementTeam.objects.order_by('created_at')
    serializer_class = ProcurementTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class CommercialTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating commercial team tasks."""
    queryset = CommercialTeam.objects.order_by('created_at')
    serializer_class = CommercialTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class HealthDocCivilViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating health docs for civil team."""
    queryset = HealthDocumentsCivilTeam.objects.order_by('created_at')
    serializer_class = HealthDocumentsCivilTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class AccessApprovalCivilViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating access approval docs for civil team."""
    queryset = AccessApprovalCivil.objects.order_by('created_at')
    serializer_class = AccessApprovalCivilSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class FoundationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundationImage.objects.order_by('created_at')
    serializer_class = FoundationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class SetSiteClearingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SetSiteClearingImage.objects.order_by('created_at')
    serializer_class = SiteClearingSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class TowerBaseImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerBaseImage.objects.order_by('created_at')
    serializer_class = TowerBaseImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BindingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BindingImage.objects.order_by('created_at')
    serializer_class = BindingImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class SteelFixFormworkImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SteelFixFormworkImage.objects.order_by('created_at')
    serializer_class = SteelFixFormworkImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ConcretePourCuringImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcretePourCuringImage.objects.order_by('created_at')
    serializer_class = ConcretePourCuringImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class SlabsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating slabs images for civil team."""
    queryset = BTSAndGeneatorSlabsImage.objects.order_by('created_at')
    serializer_class = BTSAndGeneatorSlabsImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class SiteWallingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating site walling images for civil team."""
    queryset = SiteWallingImage.objects.order_by('created_at')
    serializer_class = SiteWallingImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class CivilTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating tasks for civil team."""
    queryset = CivilWorksTeam.objects.order_by('created_at')
    serializer_class = CivilWorksTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class InstallationTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating installation team."""
    queryset = InstallationTeam.objects.order_by('created_at')
    serializer_class = InstallationTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class HealthDocumentsInstallationTeamViewset(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating HealthDocument for electrical installation  team."""
    queryset = HealthDocumentsInstallationTeam.objects.order_by('created_at')
    serializer_class = HealthDocumentsInstallationTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class AccessApprovalInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating installation team."""
    queryset = AccessApprovalInstallation.objects.order_by('created_at')
    serializer_class = AccessApprovalInstallationSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class RFAndLinkImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating RF & Link  images for Electrical team."""
    queryset = RFAndLinkImage.objects.order_by('created_at')
    serializer_class = RFAndLinkImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class ElectricalImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Electrical Images for Electrical team."""
    queryset = ElectricalImage.objects.order_by('created_at')
    serializer_class = ElectricalImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class KPLCSolarImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating KPLC & Solar images for Electrical team."""
    queryset = KPLCSolarImage.objects.order_by('created_at')
    serializer_class = KPLCSolarImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


def status_function(model_class, request):
    """Function to return status of previous team before posting """
    status = 'Previous Team Not Approved'
    project_name = request.POST['project_name']
    previous_team = model_class.objects.get(project_name=project_name)
    status_field = previous_team.is_approved
    if status_field is True:
        status = 'Approved'
        return status
    else:
        return status
