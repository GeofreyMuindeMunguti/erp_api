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

class ProcurementTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating procurement team tasks."""
    queryset = ProcurementTeam.objects.order_by('created_at').annotate(po_sum=F('po_steel_cost') + F('po_electrical_materials_cost')+ F('po_subcontractors_cost'))
    serializer_class = ProcurementTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


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


class CommercialTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 4
        completed_tasks = 0
        approved_quote_status = ''
        po_status = ''
        project_costing_status = ''
        initial_invoice_status = ''
        project_id = pk
        try:
            progress_object = CommercialTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Record does not exist'})
        approved_quote = progress_object.approved_quote_file
        po = progress_object.po_data
        project_costing = progress_object.project_costing_data
        initialinvoice = progress_object.initial_invoice
        if bool(po) is False:
            po_status = "Not uploaded"
        else:
            completed_tasks += 1
            po_status = "Uploaded"
        if bool(initialinvoice) is False:
            initial_invoice_status = "Not Uploaded"
        else:
            completed_tasks += 1
            initial_invoice_status = "Uploaded"
        if bool(approved_quote) is False:
            approved_quote_status = "Not Uploaded"
        else:
            completed_tasks += 1
            approved_quote_status = "Uploaded"
        if bool(project_costing) is False:
            project_costing_status = "Not Uploaded"
        else:
            completed_tasks += 1
            project_costing_status = "Uploaded"
        commercial_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'po_status': po_status, 'initial_invoice_status': initial_invoice_status, 'approved_quote_status': approved_quote_status, 'project_costing_status': project_costing_status, 'progress': commercial_percentage})


class ProcurementProgressTeamView(APIView):

    def get(self, request, pk):
        total_tasks = 3
        completed_tasks = 0
        po_steel_status = ''
        po_electrical_materials_status = ''
        po_subcontractors_status = ''
        project_id = pk
        try:
            progress_object = ProcurementTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Record does not exist'})
        po_steel = progress_object.po_steel
        po_electrical_materials = progress_object.po_electrical_materials
        po_subcontractors = progress_object.po_subcontractors
        if bool(po_steel) is False:
            po_steel_status = "Not uploaded"
        else:
            completed_tasks += 1
            po_steel_status = "Uploaded"
        if bool(po_electrical_materials) is False:
            po_electrical_materials_status = "Not Uploaded"
        else:
            completed_tasks += 1
            po_electrical_materials_status = "Uploaded"
        if bool(po_subcontractors) is False:
            po_subcontractors_status = "Not Uploaded"
        else:
            completed_tasks += 1
            po_subcontractors_status = "Uploaded"
        procurement_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'po_steel_status': po_steel_status, 'po_electrical_materials_status': po_electrical_materials_status, 'po_subcontractors_status': po_subcontractors_status, 'progress': procurement_percentage})


class CivilProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 4
        completed_tasks = 0
        foundation_status = ''
        slabs_status = ''
        site_walling_status = ''
        tower_status = ''
        project_id = pk
        try:
            progress_object = CivilWorksTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Record does not exist'})
        foundation_and_curing_images = progress_object.foundation_and_curing_images
        bts_and_generator_slabs_images = progress_object.bts_and_generator_slabs_images
        site_walling_images_field = progress_object.site_walling_images_field
        tower_field = progress_object.tower_data
        if bool(foundation_and_curing_images) is False:
            foundation_status = "Not uploaded"
        else:
            completed_tasks += 1
            foundation_status = "Uploaded"
        if bool(bts_and_generator_slabs_images) is False:
            slabs_status = "Not Uploaded"
        else:
            completed_tasks += 1
            slabs_status = "Uploaded"
        if bool(site_walling_images_field) is False:
            site_walling_status = "Not Uploaded"
        else:
            completed_tasks += 1
            site_walling_status = "Uploaded"
        if bool(tower_field) is False:
            tower_status = "Not Uploaded"
        else:
            completed_tasks += 1
            tower_status = "Uploaded"
        civil_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'foundation_status': foundation_status, 'slabs_status': slabs_status, 'site_walling_status': site_walling_status, 'tower_status': tower_status, 'progress': civil_percentage})


class InstallationProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 6
        completed_tasks = 0
        electrical_tasks_status = ''
        telecom_tasks_status = ''
        sign_off_status = ''
        rfi_status = ''
        integration_parameter_status = ''
        conditional_acceptance_status = ''
        project_id = pk
        try:
            progress_object = InstallationTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Record does not exist'})
        electrical_tasks_data = progress_object.electrical_tasks_data
        telecom_tasks_data = progress_object.telecom_tasks_data
        signoff = progress_object.signoff
        rfi_document = progress_object.rfi_document
        integration_parameter = progress_object.integration_parameter
        conditional_acceptance_cert = progress_object.conditional_acceptance_cert
        if bool(electrical_tasks_data) is False:
            electrical_tasks_status = "Not uploaded"
        else:
            completed_tasks += 1
            electrical_tasks_status = "Uploaded"
        if bool(telecom_tasks_data) is False:
            telecom_tasks_status = "Not Uploaded"
        else:
            completed_tasks += 1
            telecom_tasks_status = "Uploaded"
        if bool(signoff) is False:
            sign_off_status = "Not Uploaded"
        else:
            completed_tasks += 1
            sign_off_status = "Uploaded"
        if bool(rfi_document) is False:
            rfi_status = "Not Uploaded"
        else:
            completed_tasks += 1
            rfi_status = "Uploaded"
        if bool(integration_parameter) is False:
            integration_parameter_status = "Not Uploaded"
        else:
            completed_tasks += 1
            integration_parameter_status = "Uploaded"
        if bool(conditional_acceptance_cert) is False:
            conditional_acceptance_status = "Not Uploaded"
        else:
            completed_tasks += 1
            conditional_acceptance_status = "Uploaded"
        civil_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'no_of_tasks': total_tasks, 'electrical_tasks_status': electrical_tasks_status, 'telecom_tasks_status': telecom_tasks_status, 'sign_off_status': sign_off_status, 'rfi_status': rfi_status, 'integration_parameter_status': integration_parameter_status, 'conditional_acceptance_status': conditional_acceptance_status, 'progress': civil_percentage})


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


def percentage_function(no_of_complete, total_task):
    """Function to return perecentage of progress  """
    percentage = ((no_of_complete/total_task) * 100)
    return percentage
