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
from erp_core.viewspermissions import DefaultsMixin



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
    queryset = ProjectIcon.objects.order_by('created_at')
    serializer_class = ProjectIconSerializer

    search_fields = ('site_owner', )
    ordering_fields = ('updated_at', 'project_name', )


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

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

######################################## END #######################################################################################################################################

class ProjectCostingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating project costing."""
    queryset = ProjectCosting.objects.order_by('created_at')
    serializer_class = ProjectCostingSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class ProjectPOSViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating project costing."""
    queryset = ProjectPurchaseOrders.objects.order_by('created_at')
    serializer_class = ProjectPurchaseOrdersSerializer

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

####################################### KPI ###############################################################################################################################

class KpiViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating access approval docs for civil team."""
    queryset = Kpi.objects.order_by('created_at')
    serializer_class = KpiSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

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
# >>>TASK [1]<<<
class FoundationCreationTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundationCreationTask.objects.order_by('created_at')
    serializer_class = FoundationCreationTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

    # SubTask (1)://///////////Site-Clearing Subtask //////////////////

class SiteClearingSubTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SiteClearingSubtask.objects.order_by('created_at')
    serializer_class = SiteClearingSubTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class SiteClearingDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating DailySiteClearingfor civil team."""
    queryset = SiteClearingDate.objects.order_by('created_at')
    serializer_class = SiteClearingDateSerializer

    search_fields = ('work_day', )
    ordering_fields = ('updated_at', 'work_day', )

class SiteClearingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SiteClearingImage.objects.order_by('created_at')
    serializer_class = SiteClearingImageSerializer

    search_fields = ('day_image', )
    ordering_fields = ('updated_at', 'day_image', )

#Better VIEWS Implementation  # TO DO

class DailySiteClearingList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SiteClearingDate.objects.filter(site_clearing_subtask_id=self.kwargs["pk"])
        return queryset
    serializer_class = SiteClearingDateSerializer

# class SiteClearingImageView(generics.ListCreateAPIView):
#     def get_queryset(self):
#         queryset = SiteClearingImage.objects.filter(daily_site_clearing_id=self.kwargs["pk"])
#         return queryset
#     serializer_class = SiteClearingImageSerializer
    

    # SubTask (2)://///////////Tower-Base Subtask //////////////////

class TowerBaseSubTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating tower base  subtasks for civil team."""
    queryset = TowerBaseSubtask.objects.order_by('created_at')
    serializer_class = TowerBaseSubTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class TowerBaseDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating towerbase work day  for civil team."""
    queryset = TowerBaseDate.objects.order_by('created_at')
    serializer_class = TowerBaseDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class TowerBaseImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating tower base daily  images for civil team."""
    queryset = TowerBaseImage.objects.order_by('created_at')
    serializer_class = TowerBaseImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


    # SubTask (3)://///////////BlindingSubTask Subtask //////////////////

class BlindingSubTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating site blindingsubtask for civil team."""
    queryset = BlindingSubtask.objects.order_by('created_at')
    serializer_class = BlindingSubTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BlindingDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BlindingImage.objects.order_by('created_at')
    serializer_class = BlindingDateSerializer

    search_fields = ('work_day', )
    ordering_fields = ('updated_at', 'work_day', )

class BlindingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BlindingImage.objects.order_by('created_at')
    serializer_class = BlindingImageSerializer

    search_fields = ('day_image', )
    ordering_fields = ('updated_at', 'day_image', )

  # SubTask (4):///////////// SteelFixFormwork Subtask //////////////////

class SteelFixFormworkSubtaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SteelFixFormworkSubtask.objects.order_by('created_at')
    serializer_class = SteelFixFormworkSubTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
    
class SteelFixFormworkDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating f oundation images for civil team."""
    queryset = SteelFixFormworkDate.objects.order_by('created_at')
    serializer_class = SteelFixFormworkDateSerializer

    search_fields = ('work_day', )
    ordering_fields = ('updated_at', 'work_day', )

class SteelFixFormworkImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SteelFixFormworkImage.objects.order_by('created_at')
    serializer_class = SteelFixFormworkImageSerializer

    search_fields = ('day_image', )
    ordering_fields = ('updated_at', 'image_day', )

    
# SubTask (5)://///////////ConcretePour Subtask //////////////////

class ConcretePourSubTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcretePourSubtask.objects.order_by('created_at')
    serializer_class = ConcretePourSubTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name',)

class ConcretePourDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcretePourDate.objects.order_by('created_at')
    serializer_class = ConcretePourDateSerializer

    search_fields = ('sub_task', )
    ordering_fields = ('updated_at', 'sub_task',)

class ConcretePourImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcretePourImage.objects.order_by('created_at')
    serializer_class = ConcretePourImageSerializer

    search_fields = ('image_day', )
    ordering_fields = ('updated_at', 'image_day',)

    # SubTask (6)://///////////ConcreteCuringPeriod Subtask //////////////////

class ConcreteCuringPeriodSubTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcreteCuringPeriodSubtask.objects.order_by('created_at')
    serializer_class = ConcreteCuringPeriodSubTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ConcreteCuringPeriodDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcreteCuringPeriodDate.objects.order_by('created_at')
    serializer_class = ConcreteCuringPeriodDateSerializer

    search_fields = ('work_day','sub_task', )
    ordering_fields = ('updated_at', 'work_day', )

class ConcreteCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcreteCuringPeriodImage.objects.order_by('created_at')
    serializer_class = ConcreteCuringPeriodImageSerializer

    search_fields = ('day_image', )
    ordering_fields = ('updated_at', 'day_image', )


######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################
    # SubTask (6)://///////////ConcreteCuringPeriod Subtask //////////////////
class ExcavationSubTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ExcavationSubtask.objects.order_by('created_at')
    serializer_class = ExcavationSubTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ExcavationDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ExcavationDate.objects.order_by('created_at')
    serializer_class = ExcavationDateSerializer

    search_fields = ('work_day','sub_task', )
    ordering_fields = ('updated_at', 'work_day', )

class ExcavationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ExcavationImage.objects.order_by('created_at')
    serializer_class = ExcavationImageSerializer

    search_fields = ('day_image', )
    ordering_fields = ('updated_at', 'day_image', )


    # SubTask (6)://///////////ConcreteCuringPeriod Subtask //////////////////
class Bs241ConcretePourCuringPeriodSubTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241ConcretePourCuringPeriodSubtask.objects.order_by('created_at')
    serializer_class = ConcretePourCuringPeriodSubTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BS241ConcretePourCuringPeriodDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241ConcretePourCuringPeriodDate.objects.order_by('created_at')
    serializer_class = BS241ConcretePourCuringPeriodDateSerializer

    search_fields = ('work_day','sub_task', )
    ordering_fields = ('updated_at', 'work_day', )

class Bs241ConcretePourCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241ConcretePourCuringPeriodImage.objects.order_by('created_at')
    serializer_class = BS241ConcretePourCuringPeriodImageSerializer

    search_fields = ('day_image', )
    ordering_fields = ('updated_at', 'day_image', )
    

    # SubTask (6)://///////////ConcreteCuringPeriod Subtask //////////////////
class BS241AndGeneatorSlabTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241AndGeneratorSlabTask.objects.order_by('created_at')
    serializer_class = BS241AndGeneratorSlabTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

######################################## END #######################################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################
    
    # SubTask (6)://///////////FoundFootPour Subtask //////////////////
class FoundFootPourSubtaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundFootPourSubtask.objects.order_by('created_at')
    serializer_class = FoundFootPourSubtaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class FoundFootPourDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundFootPourDate.objects.order_by('created_at')
    serializer_class = FoundFootPourDateSerializer

    search_fields = ('work_day','sub_task', )
    ordering_fields = ('updated_at', 'work_day', )

class FoundFootPourImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundFootPourImage.objects.order_by('created_at')
    serializer_class = FoundFootPourImageSerializer

    search_fields = ('day_image', )
    ordering_fields = ('updated_at', 'day_image', )
    

    
    # SubTask (2)://///////////ConcreteCuringPeriod Subtask //////////////////
class BlockworkPanelConstImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BlockworkPanelConstImage.objects.order_by('created_at')
    serializer_class = BlockworkPanelConstImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class GateInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GateInstallationImage.objects.order_by('created_at')
    serializer_class = GateInstallationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class RazorElectricFenceImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = RazorElectricFenceImage.objects.order_by('created_at')
    serializer_class = RazorElectricFenceImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BoundaryWallTaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BoundaryWallTask.objects.order_by('created_at')
    serializer_class = BoundaryWallTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

######################################## END #######################################################################################################################################

####################################### TOWER & ANTENNA_COAX ###########################################################################################################################
class TowerErectionImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerErectionImage.objects.order_by('created_at')
    serializer_class = TowerErectionImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class TowerPaintImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerPaintImage.objects.order_by('created_at')
    serializer_class = TowerPaintImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class CableWaysImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = CableWaysImage.objects.order_by('created_at')
    serializer_class = CableWaysImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class AntennaCoaxInstallImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = AntennaCoaxInstallImage.objects.order_by('created_at')
    serializer_class = AntennaCoaxInstallImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class TowerAntennaCoaxImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerAntennaCoaxImage.objects.order_by('created_at')
    serializer_class = TowerAntennaCoaxImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
######################################## END #######################################################################################################################################

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


class ElectricalTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Electrical Tasks."""
    queryset = ElectricalTasks.objects.order_by('created_at')
    serializer_class = ElectricalTasksSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class GeneratorInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating generator installation tasks."""
    queryset = GeneratorInstallation.objects.order_by('created_at')
    serializer_class = GeneratorInstallationSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class EarthingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating electrical earthing tasks."""
    queryset = ElectricalEarthing.objects.order_by('created_at')
    serializer_class = ElectricalEarthingSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class ReticulationAPSViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating aps and reticulation tasks."""
    queryset = ReticulationAPSinstallation.objects.order_by('created_at')
    serializer_class = ReticulationAPSinstallationSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class UndergroundTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating aps and reticulation tasks."""
    queryset = UndergroundTasks.objects.order_by('created_at')
    serializer_class = UndergroundTasksSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class TelecomTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating telecom tasks."""
    queryset = TelecomTasks.objects.order_by('created_at')
    serializer_class = TelecomTasksSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class MWInstallationTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating mw installation tasks."""
    queryset = MWInstallationTask.objects.order_by('created_at')
    serializer_class = MWInstallationTaskSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class BTSInstallationTasksViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating bts installation tasks."""
    queryset = BTSinstallationTask.objects.order_by('created_at')
    serializer_class = BTSinstallationTaskSerializer

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


class KPLCSolarImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating KPLC & Solar images for Electrical team."""
    queryset = KPLCSolarImage.objects.order_by('created_at')
    serializer_class = KPLCSolarImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class WarrantyCertificateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Warranty certificates."""
    queryset = WarrantyCertificate.objects.order_by('created_at')
    serializer_class = WarrantyCertificateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class TestCetificateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Test certificates."""
    queryset = TestCetificate.objects.order_by('created_at')
    serializer_class = TestCetificateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class IssuesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Issues ."""
    queryset = Issues.objects.order_by('created_at')
    serializer_class = IssuesSerializer

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
