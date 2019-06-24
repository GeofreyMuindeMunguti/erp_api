"""Extract files and images per project.
"""

#__author__  = "Gibeon\ (langat@adriankenya.com)"


#---------
# Imports
#---------

from .filesserializers import *
from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from erp_construction.models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status, viewsets
from rest_framework.decorators import parser_classes
from rest_framework.decorators import detail_route
from .filemixin import DefaultsMixin ,PermissionMixin
    


#################################FILES  HANDLING VIEWS   BLOCK#####################################################

class FilesView(APIView):

    def get(self, request, format=None):
        "TO DO"
        resp = "# TO DO        USE  erp_construction/ files/<int:pk>/  :  pk is project ID"
        return Response(resp)


class ProjectFilesView(generics.RetrieveAPIView,DefaultsMixin):
    ''' Main View to return all files per project'''

    queryset = Project.objects.all()
    serializer_class = ProjectFilesSerializer



    # Views for individual files type

class SiteClearingFilesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = SetSiteClearingImage.objects.all()
    def get_queryset(self):
     #   print('This are the Kwargs i need to know:',self.kwargs,self.serializer_class)
        queryset = SetSiteClearingImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = SiteClearingFilesSerializer

class TowerBaseImagesView(generics.RetrieveAPIView,DefaultsMixin):
   # queryset = TowerBaseImage.objects.all()
    def get_queryset(self):
        queryset = TowerBaseImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = TowerBaseImagesSerializer

class BindingImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = BindingImage.objects.all()
    def get_queryset(self):
        queryset = BindingImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    
    serializer_class = BindingImagesSerializer

class SteelFixFormworkImagesView(generics.RetrieveAPIView,DefaultsMixin):

    #queryset = SteelFixFormworkImage.objects.all()

    def get_queryset(self):
        queryset = SteelFixFormworkImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = SteelFixFormworkImagesSerializer

class ConcretePourImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = ConcretePourImage.objects.all()

    def get_queryset(self):
        queryset = ConcretePourImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ConcretePourImagesSerializer

#GENERATOR FOUNDATION

class ExcavationImagesView(generics.RetrieveAPIView,DefaultsMixin):
   # queryset = ExcavationImage.objects.all()

    def get_queryset(self):
        queryset = ExcavationImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ExcavationImagesSerializer

class ConcreteCuringPeriodImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = ConcretePourCuringPeriodImage.objects.all()
    def get_queryset(self):
        queryset = ConcretePourCuringImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ConcreteCuringPeriodImagesSerializer

# BOUNDARY WALL

class FoundFootPourImageView(generics.RetrieveAPIView,DefaultsMixin):
   # queryset = FoundFootPourImage.objects.all()
    def get_queryset(self):
        queryset = FoundFootPourImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = FoundFootPourImagesSerializer

class BlockworkPanelConstImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = BlockworkPanelConstImage.objects.all()
    def get_queryset(self):
        queryset = BlockworkPanelConstImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = BlockworkPanelConstImagesSerializer

class GateInstallationImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = GateInstallationImage.objects.all()
    def get_queryset(self):
        queryset = GateInstallationImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = GateInstallationImagesSerializer

class RazorElectricFenceImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = RazorElectricFenceImage.objects.all()
    def get_queryset(self):
        queryset = RazorElectricFenceImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = RazorElectricFenceImagesSerializer

#TOWER & ANTENNA_COAXs 

class TowerErectionImagesView(generics.RetrieveAPIView,DefaultsMixin):
   # queryset = TowerErectionImage.objects.all()
    def get_queryset(self):
        queryset = TowerErectionImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = TowerErectionImagesSerializer

class TowerPaintImagesView(generics.RetrieveAPIView,DefaultsMixin):
   # queryset = TowerPaintImage.objects.all()
    def get_queryset(self):
        queryset = TowerPaintImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = TowerPaintImagesSerializer

class CableWaysImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = CableWaysImage.objects.all()
    def get_queryset(self):
        queryset = CableWaysImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = CableWaysImagesSerializer

class AntennaCoaxInstallImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = AntennaCoaxInstallImage.objects.all()
    def get_queryset(self):
        queryset = AntennaCoaxInstallImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = AntennaCoaxInstallImagesSerializer

class TowerAntennaCoaxImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = TowerAntennaCoaxImage.objects.all()
    def get_queryset(self):
        queryset = TowerErectionImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = TowerAntennaCoaxImageSerializer

#END

class ProjectPurchaseOrdersView(generics.RetrieveAPIView,DefaultsMixin):
   # queryset = ProjectPurchaseOrders.objects.all()
    def get_queryset(self):
        queryset = ProjectPurchaseOrders.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ProjectPurchaseOrdersFileSerializer

class ProjectCostingFileView(generics.RetrieveAPIView,DefaultsMixin):
   # queryset = ProjectCosting.objects.all()
    def get_queryset(self):
        queryset = ProjectCosting.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ProjectCostingFileSerializer

class CommercialTeamFilesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = CommercialTeam.objects.all()
    def get_queryset(self):
        queryset = CommercialTeam.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = CommercialTeamFilesSerializer

class ProcurementTeamFilesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = ProcurementTeam.objects.all()
    def get_queryset(self):
        queryset = ProcurementTeam.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ProcurementTeamFilesSerializer

class HealthDocumentsFilesCivilTeamView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = HealthDocumentsCivilTeam.objects.all()
    def get_queryset(self):
        queryset = HealthDocumentsCivilTeam.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = HealthDocumentsFilesCivilTeamSerializer

class AccessApprovalFileCivilView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = AccessApprovalCivil.objects.all()
    def get_queryset(self):
        queryset = AccessApprovalCivil.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = AccessApprovalFileCivilSerializer

class UndergroundTasksFilesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = UndergroundTasks.objects.all()
    def get_queryset(self):
        queryset = UndergroundTasks.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = UndergroundTasksFilesSerializer

class ReticulationAPSinstallationFilesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = ReticulationAPSinstallation.objects.all()
    def get_queryset(self):
        queryset = ReticulationAPSinstallation.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ReticulationAPSinstallationFilesSerializer

class ElectricalEarthingImagesView(generics.RetrieveAPIView,DefaultsMixin):
   # queryset = ElectricalEarthing.objects.all()
    def get_queryset(self):
        queryset = ElectricalEarthing.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ElectricalEarthingImagesSerializer

class GeneratorInstallationImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = GeneratorInstallation.objects.all()
    def get_queryset(self):
        queryset = GeneratorInstallation.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = GeneratorInstallationImagesSerializer

class KPLCSolarImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = KPLCSolarImage.objects.all()
    def get_queryset(self):
        queryset = KPLCSolarImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = KPLCSolarImagesSerializer

class BTSinstallationTaskImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = BTSinstallationTask.objects.all()
    def get_queryset(self):
        queryset = BTSinstallationTask.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = BTSinstallationTaskImagesSerializer

class MWInstallationTaskImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = MWInstallationTask.objects.all()
    def get_queryset(self):
        queryset = MWInstallationTask.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = MWInstallationTaskImagesSerializer

class InstallationTeamFilesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = InstallationTeam.objects.all()
    def get_queryset(self):
        queryset = InstallationTeam.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = InstallationTeamFilesSerializer

