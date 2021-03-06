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

class IRROF7FreeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = IRROF7Free.objects.all()
    serializer_class = IRROF7FreeSerializer

    search_fields = ('project_name', )
    ordering_fields = ('project_name', )

class BtsSiteViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = BtsSite.objects.order_by('created_at')
    serializer_class = BtsSiteSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BtsBudgetViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = BtsBudget.objects.order_by('created_at')
    serializer_class = BtsBudgetSerializer

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
###Geo_changes

class SetSiteClearingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SetSiteClearingImage.objects.order_by('created_at')
    serializer_class = SiteClearingSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class SiteClearingDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteClearingDate.objects.order_by('created_at')
    serializer_class = SiteClearingDateSerializer
    
    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class SiteClearingImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteClearingImageDaily.objects.order_by('created_at')
    serializer_class = SiteClearingImageDailySerializer
    
    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

###end    
##Geo_changes
class TowerBaseImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerBaseImage.objects.order_by('created_at')
    serializer_class = TowerBaseImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class TowerBaseImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = TowerBaseImageDaily.objects.order_by('created_at')
    serializer_class = TowerBaseImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class TowerBaseDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = TowerBaseDate.objects.order_by('created_at')
    serializer_class = TowerBaseDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

###End

####Geo_changes

class BindingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BindingImage.objects.order_by('created_at')
    serializer_class = BindingImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BindingImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = BindingImageDaily.objects.order_by('created_at')
    serializer_class = BindingImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BindingDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = BindingDate.objects.order_by('created_at')
    serializer_class = BindingDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

####End

##Geo_changes
class SteelFixFormworkImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = SteelFixFormworkImage.objects.order_by('created_at')
    serializer_class = SteelFixFormworkImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class SteelFixFormworkImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SteelFixFormworkImageDaily.objects.order_by('created_at')
    serializer_class = SteelFixFormworkImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class SteelFixFormworkDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SteelFixFormworkDate.objects.order_by('created_at')
    serializer_class = SteelFixFormworkDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

####End

####Geo_changes
class ConcretePourImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcretePourImage.objects.order_by('created_at')
    serializer_class = ConcretePourImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name',)

class ConcretePourDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ConcretePourDate.objects.order_by('created_at')
    serializer_class = ConcretePourDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name',)

class ConcretePourImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ConcretePourImageDaily.objects.order_by('created_at')
    serializer_class = ConcretePourImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name',)

###End
###Geo_changes
class ConcreteCuringPeriodDocsViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcreteCuringPeriodDocs.objects.order_by('created_at')
    serializer_class = ConcreteCuringPeriodDocsSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ConcreteCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ConcreteCuringPeriodImage.objects.order_by('created_at')
    serializer_class = ConcreteCuringPeriodImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ConcreteCuringPeriodImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ConcreteCuringPeriodImageDaily.objects.order_by('created_at')
    serializer_class = ConcreteCuringPeriodImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ConcreteCuringPeriodDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ConcreteCuringPeriodDate.objects.order_by('created_at')
    serializer_class = ConcreteCuringPeriodDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

###End
###Geo_changes
class DeliveryOfMaterialandEquipementViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = DeliveryOfMaterialandEquipement.objects.order_by('created_at')
    serializer_class = DeliveryOfMaterialandEquipementSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DeliveryOfMaterialandEquipementDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DeliveryOfMaterialandEquipementDaily.objects.order_by('created_at')
    serializer_class = DeliveryOfMaterialandEquipementDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DeliveryOfMaterialandEquipementDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DeliveryOfMaterialandEquipementDate.objects.order_by('created_at')
    serializer_class = DeliveryOfMaterialandEquipementDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

######################################## END #######################################################################################################################################

#######################################BS241 & GENERATOR FOUNDATION ###########################################################################################################################
###Geo_changes
class ExcavationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ExcavationImage.objects.order_by('created_at')
    serializer_class = ExcavationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ExcavationImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ExcavationImageDaily.objects.order_by('created_at')
    serializer_class = ExcavationImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ExcavationDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ExcavationDate.objects.order_by('created_at')
    serializer_class = ExcavationDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

####End

###Geo_changes
class bs241ConcretePourCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241ConcretePourCuringPeriodImage.objects.order_by('created_at')
    serializer_class = ConcretePourCuringPeriodImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class bs241ConcretePourCuringPeriodImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = BS241ConcretePourCuringPeriodImage.objects.order_by('created_at')
    serializer_class = ConcretePourCuringPeriodImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class bs241ConcretePourCuringPeriodDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = BS241ConcretePourCuringPeriodImage.objects.order_by('created_at')
    serializer_class = ConcretePourCuringPeriodDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

###End

###Geo_changes
class BS241ImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241Image.objects.order_by('created_at')
    serializer_class = BS241ImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BS241ImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241ImageDaily.objects.order_by('created_at')
    serializer_class = BS241ImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BS241DateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241Date.objects.order_by('created_at')
    serializer_class = BS241DateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class BS241AndGeneatorSlabsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BS241AndGeneatorSlabsImage.objects.order_by('created_at')
    serializer_class = BS241AndGeneatorSlabsImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

######################################## END #######################################################################################################################################

#######################################GENERATOR SLAB FOUNDATION ###########################################################################################################################
###Geo_changes
class GenExcavationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GenExcavationImage.objects.order_by('created_at')
    serializer_class = GenExcavationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class GenExcavationImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GenExcavationImageDaily.objects.order_by('created_at')
    serializer_class = GenExcavationImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class GenExcavationDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GenExcavationDate.objects.order_by('created_at')
    serializer_class = GenExcavationDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
###
class GenConcretePourCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GenConcretePourCuringPeriodImage.objects.order_by('created_at')
    serializer_class = GenConcretePourCuringPeriodImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class GenConcretePourCuringPeriodImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GenConcretePourCuringPeriodImageDaily.objects.order_by('created_at')
    serializer_class = GenConcretePourCuringPeriodImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class GenConcretePourCuringPeriodDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GenConcretePourCuringPeriodDate.objects.order_by('created_at')
    serializer_class = GenConcretePourCuringPeriodDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
###
class GenCableConduitsSettingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GenCableConduitsSettingImage.objects.order_by('created_at')
    serializer_class = GenCableConduitsSettingImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class GenCableConduitsSettingImageDailyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GenCableConduitsSettingImageDaily.objects.order_by('created_at')
    serializer_class = GenCableConduitsSettingImageDailySerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class GenCableConduitsSettingDateViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GenCableConduitsSettingDate.objects.order_by('created_at')
    serializer_class = GenCableConduitsSettingDateSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
####End
class GeneatorSlabsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = GeneatorSlabsImage.objects.order_by('created_at')
    serializer_class = GeneatorSlabsImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

######################################## END #######################################################################################################################################

###################################### FABRICATION ###########################################################################################################################
class FabricationSteelDeckImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = FabricationSteelDeckImage.objects.order_by('start_date')
    serializer_class = FabricationSteelDeckImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )

class FabricationQualityInspectionImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = FabricationQualityInspectionImage.objects.order_by('start_date')
    serializer_class = FabricationQualityInspectionImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )

class FabricationRooftopImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = FabricationRooftopImage.objects.order_by('start_date')
    serializer_class = FabricationRooftopImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )
######################################## END #######################################################################################################################################

####################################### INSTALLATION ROOFTOP ###########################################################################################################################
class HackingExistingColumnsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = HackingExistingColumnsImage.objects.order_by('start_date')
    serializer_class = HackingExistingColumnsImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )

class FormworkColumnsConcretePourCuringImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = FormworkColumnsConcretePourCuringImage.objects.order_by('start_date')
    serializer_class = FormworkColumnsConcretePourCuringImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )

class DeliveryToSiteImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = DeliveryToSiteImage.objects.order_by('start_date')
    serializer_class = DeliveryToSiteImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )

class LiftingHoistingFreeIssueImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = LiftingHoistingFreeIssueImage.objects.order_by('start_date')
    serializer_class = LiftingHoistingFreeIssueImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )

class FenceInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = FenceInstallationImage.objects.order_by('start_date')
    serializer_class = FenceInstallationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )

class SiteRestorationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = SiteRestorationImage.objects.order_by('start_date')
    serializer_class = SiteRestorationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )

class InstallationRooftopImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = InstallationRooftopImage.objects.order_by('start_date')
    serializer_class = InstallationRooftopImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )
####################################### END ###########################################################################################################################

####################################### BOUNDARY WALL ###########################################################################################################################

class FoundFootPourImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundFootPourImage.objects.order_by('created_at')
    serializer_class = FoundFootPourImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BWConcretePourCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BWConcretePourCuringPeriodImage.objects.order_by('created_at')
    serializer_class = BWConcretePourCuringPeriodImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )
class ExcavationstripFoundationsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ExcavationstripFoundationsImage.objects.order_by('created_at')
    serializer_class = ExcavationstripFoundationsImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BWCableConduitsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BWCableConduitsImage.objects.order_by('created_at')
    serializer_class = BWCableConduitsImageAdminSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BWBlindingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BWBlindingImage.objects.order_by('created_at')
    serializer_class = BWBlindingImageAdminSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

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

####################################### BOUNDARY WALL ###########################################################################################################################

class FoundFootPourImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = FoundFootPourImage.objects.order_by('created_at')
    serializer_class = FoundFootPourImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BWConcretePourCuringPeriodImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BWConcretePourCuringPeriodImage.objects.order_by('created_at')
    serializer_class = BWConcretePourCuringPeriodImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )
class ExcavationstripFoundationsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ExcavationstripFoundationsImage.objects.order_by('created_at')
    serializer_class = ExcavationstripFoundationsImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BWCableConduitsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BWCableConduitsImage.objects.order_by('created_at')
    serializer_class = BWCableConduitsImageAdminSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class BWBlindingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = BWBlindingImage.objects.order_by('created_at')
    serializer_class = BWBlindingImageAdminSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

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

####################################### MANHOLE SETTING OUT CONSTRUCTION  ###########################################################################################################################
class ManholeSettingExcavationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ManholeSettingExcavationImage.objects.order_by('created_at')
    serializer_class = ManholeSettingExcavationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ManholeBlindingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ManholeBlinding.objects.order_by('created_at')
    serializer_class = TowerPaintImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class ManholeBlockworkViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset =  ManholeBlockwork.objects.order_by('created_at')
    serializer_class = ManholeBlockworkSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name',)

class ManholeSettingOutConstructionImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = ManholeSettingOutConstructionImage.objects.order_by('created_at')
    serializer_class = ManholeSettingOutConstructionImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name',)

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

class CableInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = CableInstallationImage.objects.order_by('created_at')
    serializer_class = CableInstallationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class EarthInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = EarthInstallationImage.objects.order_by('created_at')
    serializer_class = EarthInstallationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class AviationLightsInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = AviationLightsInstallationImage.objects.order_by('created_at')
    serializer_class = AviationLightsInstallationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class TowerDeliveryImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating foundation images for civil team."""
    queryset = TowerDeliveryImage.objects.order_by('created_at')
    serializer_class = TowerDeliveryImageSerializer

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

class GalvanisationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating a project."""
    queryset = GalvanisationImage.objects.order_by('start_date')
    serializer_class = GalvanisationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('start_date','project_name', )
