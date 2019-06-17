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


class ProjectViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = Project.objects.order_by('created_at')
    serializer_class = ProjectSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class ProjectIconViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project icons."""
    queryset = ProjectIcons.objects.order_by('created_at')
    serializer_class = ProjectIconsSerializer

    search_fields = ('site_owner', )
    ordering_fields = ('updated_at', 'project_name', )


class CategoryViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = Category.objects.order_by('created_at')
    serializer_class = CategorySerializer

    search_fields = ('category_name', )
    ordering_fields = ('updated_at', 'category_name', )


####################################### PROCUREMENT TEAM ###########################################################################################################################

# .annotate(po_sum=F('po_steel_cost') + F('po_electrical_materials_cost')+ F('po_subcontractors_cost'))
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
######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################
class ExcavationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ExcavationImage.objects.order_by('created_at')
    serializer_class = ExcavationImageerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ConcretePourCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcretePourCuringPeriodImage.objects.order_by('created_at')
    serializer_class = ConcretePourCuringPeriodImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BTSAndGeneatorSlabsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BTSAndGeneatorSlabsImage.objects.order_by('created_at')
    serializer_class = BTSAndGeneatorSlabsImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
######################################## END #######################################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################

class FoundFootPourImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundFootPourImage.objects.order_by('created_at')
    serializer_class = FoundFootPourImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

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

class BoundaryWallImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BoundaryWallImage.objects.order_by('created_at')
    serializer_class = BoundaryWallImageSerializer

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

class SlabsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating slabs images for civil team."""
    queryset = BTSAndGeneatorSlabsImage.objects.order_by('created_at')
    serializer_class = BTSAndGeneatorSlabsImageSerializer

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



#FILES

class ProjectFilesView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectFilesSerializer

class SiteClearingFilesView(generics.RetrieveAPIView):
    #queryset = SetSiteClearingImage.objects.all()
    def get_queryset(self):
        queryset = SetSiteClearingImage.objects.get(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = SiteClearingFilesSerializer


class TowerBaseImagesView(generics.RetrieveAPIView):
    queryset = TowerBaseImage.objects.all()
    serializer_class = TowerBaseImagesSerializer

class BindingImagesView(generics.RetrieveAPIView):
    queryset = BindingImage.objects.all()
    serializer_class = BindingImagesSerializer

class SteelFixFormworkImagesView(generics.RetrieveAPIView):
    queryset = SteelFixFormworkImage.objects.all()
    serializer_class = SteelFixFormworkImagesSerializer

class ConcretePourCuringImagesView(generics.RetrieveAPIView):
    queryset = ConcretePourCuringImage.objects.all()
    serializer_class = ConcretePourCuringImagesSerializer

#GENERATOR FOUNDATION

class ExcavationImagesView(generics.RetrieveAPIView):
    queryset = ExcavationImage.objects.all()
    serializer_class = ExcavationImagesSerializer

class ConcretePourCuringPeriodImagesView(generics.RetrieveAPIView):
    queryset = ConcretePourCuringPeriodImage.objects.all()
    serializer_class = ConcretePourCuringPeriodImagesSerializer

# BOUNDARY WALL

class FoundFootPourImageView(generics.RetrieveAPIView):
    queryset = FoundFootPourImage.objects.all()
    serializer_class = FoundFootPourImagesSerializer

class BlockworkPanelConstImagesView(generics.RetrieveAPIView):
    queryset = BlockworkPanelConstImage.objects.all()
    serializer_class = BlockworkPanelConstImagesSerializer

class GateInstallationImagesView(generics.RetrieveAPIView):
    queryset = GateInstallationImage.objects.all()
    serializer_class = GateInstallationImagesSerializer

class RazorElectricFenceImagesView(generics.RetrieveAPIView):
    queryset = RazorElectricFenceImage.objects.all()
    serializer_class = RazorElectricFenceImagesSerializer

#TOWER & ANTENNA_COAXs 

class TowerErectionImagesView(generics.RetrieveAPIView):
    queryset = TowerErectionImage.objects.all()
    serializer_class = TowerErectionImagesSerializer

class TowerPaintImagesView(generics.RetrieveAPIView):
    queryset = TowerPaintImage.objects.all()
    serializer_class = TowerPaintImagesSerializer

class CableWaysImagesView(generics.RetrieveAPIView):
    queryset = CableWaysImage.objects.all()
    serializer_class = CableWaysImagesSerializer

class AntennaCoaxInstallImagesView(generics.RetrieveAPIView):
    queryset = AntennaCoaxInstallImage.objects.all()
    serializer_class = AntennaCoaxInstallImagesSerializer

class TowerAntennaCoaxImagesView(generics.RetrieveAPIView):
    queryset = TowerAntennaCoaxImage.objects.all()
    serializer_class = TowerAntennaCoaxImageSerializer

#END

class ProjectPurchaseOrdersView(generics.RetrieveAPIView):
    queryset = ProjectPurchaseOrders.objects.all()
    serializer_class = ProjectPurchaseOrdersFileSerializer

class ProjectCostingFileView(generics.RetrieveAPIView):
    queryset = ProjectCosting.objects.all()
    serializer_class = ProjectCostingFileSerializer

class CommercialTeamFilesView(generics.RetrieveAPIView):
    queryset = CommercialTeam.objects.all()
    serializer_class = CommercialTeamFilesSerializer

class ProcurementTeamFilesView(generics.RetrieveAPIView):
    queryset = ProcurementTeam.objects.all()
    serializer_class = ProcurementTeamFilesSerializer

class HealthDocumentsFilesCivilTeamView(generics.RetrieveAPIView):
    queryset = HealthDocumentsCivilTeam.objects.all()
    serializer_class = HealthDocumentsFilesCivilTeamSerializer

class AccessApprovalFileCivilView(generics.RetrieveAPIView):
    queryset = AccessApprovalCivil.objects.all()
    serializer_class = AccessApprovalFileCivilSerializer

class UndergroundTasksFilesView(generics.RetrieveAPIView):
    queryset = UndergroundTasks.objects.all()
    serializer_class = UndergroundTasksFilesSerializer

class ReticulationAPSinstallationFilesView(generics.RetrieveAPIView):
    queryset = ReticulationAPSinstallation.objects.all()
    serializer_class = ReticulationAPSinstallationFilesSerializer

class ElectricalEarthingImagesView(generics.RetrieveAPIView):
    queryset = ElectricalEarthing.objects.all()
    serializer_class = ElectricalEarthingImagesSerializer

class GeneratorInstallationImagesView(generics.RetrieveAPIView):
    queryset = GeneratorInstallation.objects.all()
    serializer_class = GeneratorInstallationImagesSerializer

class KPLCSolarImagesView(generics.RetrieveAPIView):
    queryset = KPLCSolarImage.objects.all()
    serializer_class = KPLCSolarImagesSerializer

class BTSinstallationTaskImagesView(generics.RetrieveAPIView):
    queryset = BTSinstallationTask.objects.all()
    serializer_class = BTSinstallationTaskImagesSerializer

class MWInstallationTaskImagesView(generics.RetrieveAPIView):
    queryset = MWInstallationTask.objects.all()
    serializer_class = MWInstallationTaskImagesSerializer

class InstallationTeamFilesView(generics.RetrieveAPIView):
    queryset = InstallationTeam.objects.all()
    serializer_class = InstallationTeamFilesSerializer
