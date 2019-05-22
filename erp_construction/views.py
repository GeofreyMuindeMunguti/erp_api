from django.shortcuts import render
from .serializers import ProjectSerializer, ProcurementTeamSerializer, HealthDocumentsCivilTeamSerializer, AccessApprovalCivilSerializer, CivilWorksTeamSerializer, FoundationImageSerializer, BTSAndGeneatorSlabsImageSerializer, SiteWallingImageSerializer, CommercialTeamSerializer, SafaricomTeamSerializer, UserSerializer,KPLCSolarImageSerializer,ElectricalImageSerializer,RFAndLinkImageSerializer,AccessApprovalInstallationSerializer,InstallationTeamSerializer,HealthDocumentsInstallationTeamSerializer
from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from .models import Project, ProcurementTeam, HealthDocumentsCivilTeam, AccessApprovalCivil, CivilWorksTeam, FoundationImage, BTSAndGeneatorSlabsImage, SiteWallingImage, CommercialTeam, SafaricomTeam,InstallationTeam,AccessApprovalInstallation,KPLCSolarImage,HealthDocumentsInstallationTeam, RFAndLinkImage,ElectricalImage
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime
from django.http import JsonResponse
from rest_framework.views import APIView


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
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    '''
    We configure the SearchFilter by adding a search_fields attribute to each
    ViewSet . We configure the OrderingFilter by adding a list of fields, which can be used
    for ordering the ordering_fields .
    '''


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('date_joined')
    serializer_class = UserSerializer
    ordering_fields = ('updated_at', )


class ProjectViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = Project.objects.order_by('created_at')
    serializer_class = ProjectSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class ProcurementTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating procurement team tasks."""
    queryset = ProcurementTeam.objects.order_by('created_at')
    serializer_class = ProcurementTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

    def create(self, request, *args, **kwargs):
        get_status = status_function(CommercialTeam, request)
        if get_status == 'Approved':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'status': get_status, 'project_name': request.POST['project_name']})


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

    def create(self, request, *args, **kwargs):
        get_status = status_function(ProcurementTeam, request)
        if get_status == 'Approved':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'status': get_status, 'project_name': request.POST['project_name']})


class SafaricomTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating tasks for safaricom team."""
    queryset = SafaricomTeam.objects.order_by('created_at')
    serializer_class = SafaricomTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

    def create(self, request, *args, **kwargs):
        get_status = status_function(InstallationTeam, request)
        if get_status == 'Approved':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'status': get_status, 'project_name': request.POST['project_name']})


class InstallationTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating installation team."""
    queryset = InstallationTeam.objects.order_by('created_at')
    serializer_class = InstallationTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

    def create(self, request, *args, **kwargs):
        get_status = status_function(CivilWorksTeam, request)
        if get_status == 'Approved':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'status': get_status, 'project_name': request.POST['project_name']})


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


class CommercialTeamProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 2
        completed_tasks = 0
        po_status = ''
        initial_invoice_status = ''
        project_id = pk
        try:
            progress_object = CommercialTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Record does not exist'})
        po = progress_object.po_file
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
        commercial_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'po_status': po_status, 'initial_invoice_status': initial_invoice_status, 'progress': commercial_percentage})


class ProcurementTeamView(APIView):

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
        return Response({'po_steel_status': po_steel_status, 'po_electrical_materials_status': po_electrical_materials_status, 'po_subcontractors_status': po_subcontractors_status, 'progress': procurement_percentage})


class CivilProgressView(APIView):

    def get(self, request, pk):
        total_tasks = 3 # CHANGE THIS TO SEVEN WHEN NEW FIELDS ARE IMPLEMENTED
        completed_tasks = 0
        foundation_status = ''
        slabs_status = ''
        site_walling_status = ''
        project_id = pk
        try:
            progress_object = CivilWorksTeam.objects.get(project_name=project_id)
        except Exception as e:
            return Response({'error': 'Record does not exist'})
        foundation_and_curing_images = progress_object.foundation_and_curing_images
        bts_and_generator_slabs_images = progress_object.bts_and_generator_slabs_images
        site_walling_images_field = progress_object.site_walling_images_field
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
        civil_percentage = percentage_function(completed_tasks, total_tasks)
        return Response({'foundation_status': foundation_status, 'slabs_status': slabs_status, 'site_walling_status': site_walling_status, 'progress': civil_percentage})


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
