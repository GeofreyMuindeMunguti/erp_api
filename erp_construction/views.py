from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from .models import *
from django.db.models import Sum, F
from django.contrib.auth.models import User
from datetime import datetime

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status, viewsets
from rest_framework.decorators import parser_classes
from rest_framework.decorators import detail_route


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
    
class BtsProjectViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = BtsProject.objects.order_by('created_at')
    serializer_class = BtsProjectSerializer

    search_fields = ('bts_project_name', )
    ordering_fields = ('updated_at', 'bts_project_name', )

class BtsSiteViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = BtsSite.objects.order_by('created_at')
    serializer_class = BtsSiteSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ProjectIconViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project icons."""
    queryset = ProjectIcons.objects.order_by('created_at')
    serializer_class = ProjectIconsSerializer

    search_fields = ('site_owner', )
    ordering_fields = ('updated_at', 'site_name', )


class CategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = Category.objects.order_by('created_at')
    serializer_class = CategorySerializer

    search_fields = ('category_name', )
    ordering_fields = ('updated_at', 'category_name', )


####################################### PROCUREMENT TEAM ###########################################################################################################################

class ProcurementTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating procurement team tasks."""
    queryset = ProcurementTeam.objects.order_by('created_at')
    serializer_class = ProcurementTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

######################################## END #######################################################################################################################################

class ProjectCostingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating project costing."""
    queryset = ProjectCosting.objects.order_by('created_at')
    serializer_class = ProjectCostingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class ProjectPOSViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating project costing."""
    queryset = ProjectPurchaseOrders.objects.order_by('created_at')
    serializer_class = ProjectPurchaseOrdersSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class CommercialTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating commercial team tasks."""
    queryset = CommercialTeam.objects.order_by('created_at')
    serializer_class = CommercialTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class HealthDocCivilViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating health docs for civil team."""
    queryset = HealthDocumentsCivilTeam.objects.order_by('created_at')
    serializer_class = HealthDocumentsCivilTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class AccessApprovalCivilViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating access approval docs for civil team."""
    queryset = AccessApprovalCivil.objects.order_by('created_at')
    serializer_class = AccessApprovalCivilSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

####################################### KPI ###############################################################################################################################

class KpiViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating access approval docs for civil team."""
    queryset = Kpi.objects.order_by('created_at')
    serializer_class = KpiSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

######################################## END #######################################################################################################################################

####################################### TASKS ###############################################################################################################################

class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating access approval docs for civil team."""
    queryset = Task.objects.order_by('created_at')
    serializer_class = TaskSerializer

    search_fields = ('task_name', )
    ordering_fields = ('updated_at', 'task_name', )

######################################## END #######################################################################################################################################

####################################### SUBTASKS ###############################################################################################################################

class SubTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating access approval docs for civil team."""
    queryset = SubTask.objects.order_by('created_at')
    serializer_class = SubTaskSerializer

    search_fields = ('subtask_name', )
    ordering_fields = ('updated_at', 'subtask_name', )

######################################## END #######################################################################################################################################

####################################### START FOUNDATION IMAGES ###########################################################################################################################

class FoundationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundationImage.objects.order_by('created_at')
    serializer_class = FoundationImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SetSiteClearingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SetSiteClearingImage.objects.order_by('created_at')
    serializer_class = SiteClearingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class TowerBaseImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerBaseImage.objects.order_by('created_at')
    serializer_class = TowerBaseImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BindingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BindingImage.objects.order_by('created_at')
    serializer_class = BindingImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SteelFixFormworkImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SteelFixFormworkImage.objects.order_by('created_at')
    serializer_class = SteelFixFormworkImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class ConcretePourImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcretePourImage.objects.order_by('created_at')
    serializer_class = ConcretePourImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name',)


class ConcreteCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcreteCuringPeriodImage.objects.order_by('created_at')
    serializer_class = ConcreteCuringPeriodImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################
class ExcavationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ExcavationImage.objects.order_by('created_at')
    serializer_class = ExcavationImageerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class bs241ConcretePourCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241ConcretePourCuringPeriodImage.objects.order_by('created_at')
    serializer_class = ConcretePourCuringPeriodImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BS241AndGeneatorSlabsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241AndGeneatorSlabsImage.objects.order_by('created_at')
    serializer_class = BS241AndGeneatorSlabsImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

######################################## END #######################################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################

class FoundFootPourImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundFootPourImage.objects.order_by('created_at')
    serializer_class = FoundFootPourImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BlockworkPanelConstImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BlockworkPanelConstImage.objects.order_by('created_at')
    serializer_class = BlockworkPanelConstImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class GateInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GateInstallationImage.objects.order_by('created_at')
    serializer_class = GateInstallationImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class RazorElectricFenceImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = RazorElectricFenceImage.objects.order_by('created_at')
    serializer_class = RazorElectricFenceImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BoundaryWallImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BoundaryWallImage.objects.order_by('created_at')
    serializer_class = BoundaryWallImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAX ###########################################################################################################################
class TowerErectionImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerErectionImage.objects.order_by('created_at')
    serializer_class = TowerErectionImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class TowerPaintImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerPaintImage.objects.order_by('created_at')
    serializer_class = TowerPaintImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class CableWaysImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = CableWaysImage.objects.order_by('created_at')
    serializer_class = CableWaysImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class AntennaCoaxInstallImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = AntennaCoaxInstallImage.objects.order_by('created_at')
    serializer_class = AntennaCoaxInstallImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class TowerAntennaCoaxImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerAntennaCoaxImage.objects.order_by('created_at')
    serializer_class = TowerAntennaCoaxImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )
######################################## END #######################################################################################################################################

class CivilTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating tasks for civil team."""
    queryset = CivilWorksTeam.objects.order_by('created_at')
    serializer_class = CivilWorksTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class InstallationTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating installation team."""
    queryset = InstallationTeam.objects.order_by('created_at')
    serializer_class = InstallationTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class ElectricalTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Electrical Tasks."""
    queryset = ElectricalTasks.objects.order_by('created_at')
    serializer_class = ElectricalTasksSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class GeneratorInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating generator installation tasks."""
    queryset = GeneratorInstallation.objects.order_by('created_at')
    serializer_class = GeneratorInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class EarthingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating electrical earthing tasks."""
    queryset = ElectricalEarthing.objects.order_by('created_at')
    serializer_class = ElectricalEarthingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class ReticulationAPSViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating aps and reticulation tasks."""
    queryset = ReticulationAPSinstallation.objects.order_by('created_at')
    serializer_class = ReticulationAPSinstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class UndergroundTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating aps and reticulation tasks."""
    queryset = UndergroundTasks.objects.order_by('created_at')
    serializer_class = UndergroundTasksSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class TelecomTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating telecom tasks."""
    queryset = TelecomTasks.objects.order_by('created_at')
    serializer_class = TelecomTasksSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class MWInstallationTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating mw installation tasks."""
    queryset = MWInstallationTask.objects.order_by('created_at')
    serializer_class = MWInstallationTaskSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class BTSInstallationTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating bts installation tasks."""
    queryset = BTSinstallationTask.objects.order_by('created_at')
    serializer_class = BTSinstallationTaskSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class HealthDocumentsInstallationTeamViewset(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating HealthDocument for electrical installation  team."""
    queryset = HealthDocumentsInstallationTeam.objects.order_by('created_at')
    serializer_class = HealthDocumentsInstallationTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class AccessApprovalInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating installation team."""
    queryset = AccessApprovalInstallation.objects.order_by('created_at')
    serializer_class = AccessApprovalInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class KPLCSolarImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating KPLC & Solar images for Electrical team."""
    queryset = KPLCSolarImage.objects.order_by('created_at')
    serializer_class = KPLCSolarImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class WarrantyCertificateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Warranty certificates."""
    queryset = WarrantyCertificate.objects.order_by('created_at')
    serializer_class = WarrantyCertificateSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class TestCetificateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Test certificates."""
    queryset = TestCetificate.objects.order_by('created_at')
    serializer_class = TestCetificateSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


class IssuesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Issues ."""
    queryset = Issues.objects.order_by('created_at')
    serializer_class = IssuesSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


def status_function(model_class, request):
    """Function to return status of previous team before posting """
    status = 'Previous Team Not Approved'
    site_name = request.POST['site_name']
    previous_team = model_class.objects.get(site_name=site_name)
    status_field = previous_team.is_approved
    if status_field is True:
        status = 'Approved'
        return status
    else:
        return status
