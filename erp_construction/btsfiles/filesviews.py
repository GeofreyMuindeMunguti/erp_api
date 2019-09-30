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

class BtsSiteFilesCommonView(generics.RetrieveAPIView,DefaultsMixin):
    ''' Main View to return all files per project'''

    queryset = BtsSite.objects.all()
    serializer_class = SiteFilesCSerializer

    # Views for individual files type

class SiteClearingFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = SiteClearingFilesSerializer



class TowerBaseImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = TowerBaseImagesSerializer



class BindingImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = BindingImagesSerializer

class SteelFixFormworkImagesView(generics.RetrieveAPIView,DefaultsMixin):

    queryset = BtsSite.objects.all()
    serializer_class = SteelFixFormworkImagesSerializer


class ConcretePourImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()

    serializer_class = ConcretePourImagesSerializer


class ConcreteCuringImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = ConcreteCuringImagesSerializer

#GENERATOR FOUNDATION

class ExcavationImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = ExcavationImagesSerializer

class ConcreteCuringPeriodImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = ConcreteCuringPeriodImagesSerializer

# BOUNDARY WALL

class FoundFootPourImageView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = FoundFootPourImagesSerializer

class BlockworkPanelConstImagesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = BlockworkPanelConstImage.objects.all()

    queryset = BtsSite.objects.all()
    serializer_class = BlockworkPanelConstImagesSerializer

class GateInstallationImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = GateInstallationImagesSerializer

class RazorElectricFenceImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = RazorElectricFenceImagesSerializer

#TOWER & ANTENNA_COAXs

class TowerErectionImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = TowerErectionImagesSerializer

class TowerPaintImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = TowerPaintImagesSerializer

class CableWaysImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = CableWaysImagesSerializer

class AntennaCoaxInstallImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = AntennaCoaxInstallImagesSerializer



#END

class ProjectPurchaseOrdersView(generics.RetrieveAPIView,DefaultsMixin):
    def get_queryset(self):
        queryset = ProjectPurchaseOrders.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ProjectPurchaseOrdersFileSerializer

class ProjectCostingFileView(generics.RetrieveAPIView,DefaultsMixin):
    def get_queryset(self):
        queryset = ProjectCosting.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ProjectCostingFileSerializer

class CommercialTeamFilesView(generics.RetrieveAPIView,DefaultsMixin):
    def get_queryset(self):
        queryset = CommercialTeam.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = CommercialTeamFilesSerializer

class ProcurementTeamFilesView(generics.RetrieveAPIView,DefaultsMixin):
    def get_queryset(self):
        queryset = ProcurementTeam.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = ProcurementTeamFilesSerializer

class HealthDocumentsFilesCivilTeamView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = HealthDocumentsFilesCivilTeamSerializer

class AccessApprovalFileCivilView(generics.RetrieveAPIView,DefaultsMixin):
    def get_queryset(self):
        queryset = AccessApprovalCivil.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = AccessApprovalFileCivilSerializer


class HealthDocumentsFilesInstallationTeamView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = HealthDocumentsFilesInstallationTeamSerializer


class AccessApprovalFileInstallationView(generics.RetrieveAPIView,DefaultsMixin):

    def get_queryset(self):
        queryset = AccessApprovalInstallation.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = AccessApprovalFileInstallationSerializer


class UndergroundTasksFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()    
    serializer_class = UndergroundTasksFilesSerializer

class ReticulationAPSinstallationFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = ReticulationAPSinstallationFilesSerializer

class ElectricalEarthingImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = ElectricalEarthingImagesSerializer

class GeneratorInstallationImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = GeneratorInstallationImagesSerializer

class KPLCSolarImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = KPLCSolarImagesSerializer

class BTSinstallationTaskImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
    serializer_class = BTSinstallationTaskImagesSerializer

class MWInstallationTaskImagesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()

    serializer_class = MWInstallationTaskImagesSerializer

class InstallationTeamFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = BtsSite.objects.all()
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