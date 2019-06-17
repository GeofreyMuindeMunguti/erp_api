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


#################################FILES  HANDLING VIEWS   BLOCK#####################################################

class FilesView(APIView):

    def get(self, request, format=None):
        "TO DO"
        resp = "# TO DO         '.  By the way ,you gotta be kidding! Is returnig all file of all project nessesary realy?!It make sense to return per project only.!"
        return Response(resp)


class ProjectFilesView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectFilesSerializer

class SiteClearingFilesView(generics.RetrieveAPIView):
    #queryset = SetSiteClearingImage.objects.all()
    def get_queryset(self):
        queryset = SetSiteClearingImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = SiteClearingFilesSerializer


class TowerBaseImagesView(generics.RetrieveAPIView):
    queryset = TowerBaseImage.objects.all()
    serializer_class = TowerBaseImagesSerializer

class BindingImagesView(generics.RetrieveAPIView):
    queryset = BindingImage.objects.all()
    serializer_class = BindingImagesSerializer

    bindingimage = BindingImagesSerializer(read_only=True)
    class Meta:
        model = Project
        fields = ('geotech_file','access_letter','approved_drawing','final_acceptance_cert','setsiteclearingimage','towerbaseimage','bindingimage',)
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
