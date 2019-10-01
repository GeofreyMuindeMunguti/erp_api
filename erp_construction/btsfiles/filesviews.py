"""Extract files and images per project.
"""
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
from erp_construction.fileshandler.filemixin import DefaultsMixin



#################################FILES  HANDLING VIEWS   BLOCK#####################################################

class FilesView(APIView):

    def get(self, request, format=None):
        "TO DO"
        resp = "# TO DO        USE  erp_construction/ files/<int:pk>/  :  pk is project ID"
        return Response(resp)


class BtsSiteFilesView(generics.RetrieveAPIView,DefaultsMixin):
    ''' Main View to return all files per project'''

    queryset = BtsSite.objects.all()
    serializer_class = SiteFilesSerializer



    # Views for individual files type

class SiteClearingFilesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = SetSiteClearingImage.objects.all()
    def get_queryset(self):
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


class ConcreteCuringImagesView(generics.RetrieveAPIView,DefaultsMixin):

    def get_queryset(self):
        queryset = ConcreteCuringPeriodImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ConcreteCuringImagesSerializer

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
        queryset = BS241ConcretePourCuringPeriodImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ConcreteCuringPeriodImagesSerializer

# BOUNDARY WALL

class FoundFootPourImageView(generics.RetrieveAPIView,DefaultsMixin):
   # queryset = FoundFootPourImage.objects.all()
    def get_queryset(self):
        queryset = FoundFootPourImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = FoundFootPourImagesSerializer

class BWCableConduitsImageView(generics.RetrieveAPIView,DefaultsMixin):
     
    def get_queryset(self):
        queryset = BWCableConduitsImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = BWCableConduitsImageSerializer

class BWBlindingImageView(generics.RetrieveAPIView,DefaultsMixin):
     
    def get_queryset(self):
        queryset = BWBlindingImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = BWBlindingImageSerializer

class ExcavationstripFoundationsImageView(generics.RetrieveAPIView,DefaultsMixin):
     
    def get_queryset(self):
        queryset = ExcavationstripFoundationsImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ExcavationstripFoundationsImageSerializer

class BWConcretePourCuringPeriodImageView(generics.RetrieveAPIView,DefaultsMixin):
     
    def get_queryset(self):
        queryset = BWConcretePourCuringPeriodImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = BWConcretePourCuringPeriodImageSerializer


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

class AviationLightsInstallationImageView(generics.RetrieveAPIView,DefaultsMixin):

    def get_queryset(self):
        queryset = AviationLightsInstallationImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = AviationLightsInstallationImageSerializer

class EarthInstallationImageView(generics.RetrieveAPIView,DefaultsMixin):
    
    def get_queryset(self):
        queryset = EarthInstallationImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = EarthInstallationImageSerializer

class CableInstallationImageView(generics.RetrieveAPIView,DefaultsMixin):
    
    def get_queryset(self):
        queryset = CableInstallationImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = CableInstallationImageSerializer

class TowerDeliveryImageView(generics.RetrieveAPIView,DefaultsMixin):
   
    def get_queryset(self):
        queryset = TowerDeliveryImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = TowerDeliveryImageSerializer



class AntennaCoaxInstallImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = AntennaCoaxInstallImage.objects.all()
    def get_queryset(self):
        queryset = AntennaCoaxInstallImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = AntennaCoaxInstallImagesSerializer



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


class HealthDocumentsFilesInstallationTeamView(generics.RetrieveAPIView,DefaultsMixin):

    def get_queryset(self):
        queryset = HealthDocumentsInstallationTeam.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = HealthDocumentsFilesInstallationTeamSerializer


class AccessApprovalFileInstallationView(generics.RetrieveAPIView,DefaultsMixin):

    def get_queryset(self):
        queryset = AccessApprovalInstallation.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = AccessApprovalFileInstallationSerializer


class UndergroundTasksFilesView(generics.RetrieveAPIView,DefaultsMixin):

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


class IssueImageView(generics.RetrieveAPIView,DefaultsMixin):

    def get_queryset(self):
        queryset = Issues.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = IssueImageSerializer

class IRROF7FreeFilesView(generics.RetrieveAPIView,DefaultsMixin):
    
    def get_queryset(self):
        queryset = IRROF7Free.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = IRROF7FreeFilesSerializer

class FabricationQualityInspectionImageFilesView(generics.RetrieveAPIView,DefaultsMixin):
    
    def get_queryset(self):
        queryset = FabricationQualityInspectionImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = FabricationQualityInspectionImageFilesSerializer

class FabricationSteelDeckImageFilesView(generics.RetrieveAPIView,DefaultsMixin):
    
    def get_queryset(self):
        queryset = FabricationSteelDeckImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = FabricationSteelDeckImageFilesSerializer

class GalvanisationImageFilesView(generics.RetrieveAPIView,DefaultsMixin):
    
    def get_queryset(self):
        queryset = GalvanisationImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = GalvanisationImageFilesSerializer