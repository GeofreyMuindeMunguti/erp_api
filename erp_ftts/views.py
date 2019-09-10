from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from .models import *
from erp_construction.models import *
from users.models import *
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

from erp_core.viewspermissions import *

class FTTSProjectViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """ViewSet for the FTTSProject class"""

    queryset = FTTSProject.objects.order_by('created_at')
    serializer_class = FTTSProjectSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsSiteViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """ViewSet for the FTTSProject class"""

    queryset = FttsSite.objects.order_by('created_at')
    serializer_class = FttsSiteSerializer

    search_fields = ('project_name','site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsSiteListView(generics.ListCreateAPIView):
    """ViewSet for the FTTSProject class"""
    def get_queryset(self):
        queryset = FttsSite.objects.filter(ftts_project_id=self.kwargs["pk"])
        return queryset

    serializer_class = FttsSiteSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )


#################################FTTH VIEWSETS#################################


class InterceptionPointViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = InterceptionPoint.objects.order_by('created_at')
    serializer_class = InterceptionPointSerializer

    search_fields = ('interception_point_name', )
    ordering_fields = ('created_at', 'interception_point_name', )


class fttsSurveyPhotosViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = fttsSurveyPhotos.objects.order_by('created_at')
    serializer_class = fttsSurveyPhotosSerializer

    search_fields = ('site_name', )
    ordering_fields = ('created_at', 'site_name', )


class fttsSurveyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = fttsSurvey.objects.order_by('created_at')
    serializer_class = fttsSurveySerializer

    search_fields = ('site_name', )
    ordering_fields = ('created_at', 'site_name', )


#################################END OF FTTH VIEWSETS##########################

class FttsCommercialTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FttsCommercialTeam.objects.order_by('created_at')
    serializer_class = FttsCommercialTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsProcurementTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FttsProcurementTeam.objects.order_by('created_at')
    serializer_class = FttsProcurementTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsCertificatesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FttsCertificates.objects.order_by('created_at')
    serializer_class = FttsCertificatesSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

################################################ FIBER CIVIL TEAM ##############################################################################################################################################################################################################################################
class SiteTrenchingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteTrenchingImage.objects.order_by('created_at')
    serializer_class = SiteTrenchingImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class DailySiteTrenchingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailySiteTrenching.objects.order_by('created_at')
    serializer_class = DailySiteTrenchingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteTrenchingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteTrenching.objects.order_by('created_at')
    serializer_class = SiteTrenchingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteDuctInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteDuctInstallationImage.objects.order_by('created_at')
    serializer_class = SiteDuctInstallationImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class DailySiteDuctInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailySiteDuctInstallation.objects.order_by('created_at')
    serializer_class = DailySiteDuctInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteDuctInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteDuctInstallation.objects.order_by('created_at')
    serializer_class = SiteDuctInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class ManHoleInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ManHoleInstallationImage.objects.order_by('created_at')
    serializer_class = ManHoleInstallationImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class DailyManHoleInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyManHoleInstallation.objects.order_by('created_at')
    serializer_class = DailyManHoleInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteManHoleInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ManHoleInstallation.objects.order_by('created_at')
    serializer_class = SiteManHoleInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteCableInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteCableInstallationImage.objects.order_by('created_at')
    serializer_class = SiteCableInstallationImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class DailySiteCableInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailySiteCableInstallation.objects.order_by('created_at')
    serializer_class = DailySiteCableInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteCableInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteCableInstallation.objects.order_by('created_at')
    serializer_class = SiteCableInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsAccessApprovalCivilViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating health docs for civil team."""
    queryset = FttsAccessApprovalCivil.objects.order_by('created_at')
    serializer_class = FttsAccessApprovalCivilSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsHealthDocumentsCivilTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating access approval docs for civil team."""
    queryset = FttsHealthDocumentsCivilTeam.objects.order_by('created_at')
    serializer_class = FttsHealthDocumentsCivilTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsCivilTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FttsCivilTeam.objects.order_by('created_at')
    serializer_class = FttsCivilTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

################################################ END ##############################################################################################################################################################################################################################################################

################################################ FIBER INSTALLATION TEAM ##############################################################################################################################################################################################################################################

class SiteTerminalInHseImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteTerminalInHseImage.objects.order_by('created_at')
    serializer_class = SiteTerminalInHseImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class DailySiteTerminalInHseViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailySiteTerminalInHse.objects.order_by('created_at')
    serializer_class = DailySiteTerminalInHseSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteTerminalInHseViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteTerminalInHse.objects.order_by('created_at')
    serializer_class = SiteTerminalInHseSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteInterceptionImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteInterceptionImage.objects.order_by('created_at')
    serializer_class = SiteInterceptionImageSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class DailySiteInterceptionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailySiteInterception.objects.order_by('created_at')
    serializer_class = DailySiteInterceptionSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteInterceptionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteInterception.objects.order_by('created_at')
    serializer_class = SiteInterceptionSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsAccessApprovalInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating health docs for civil team."""
    queryset = FttsAccessApprovalInstallation.objects.order_by('created_at')
    serializer_class = FttsAccessApprovalInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsHealthDocsInstallationTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating access approval docs for civil team."""
    queryset = FttsHealthDocsInstallationTeam.objects.order_by('created_at')
    serializer_class = FttsHealthDocsInstallationTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsIssuesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Issues ."""
    queryset = FttsIssues.objects.order_by('created_at')
    serializer_class = FttsIssuesSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsInstallationTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FttsInstallationTeam.objects.order_by('created_at')
    serializer_class = FttsInstallationTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Issues ."""
    queryset = FttsTeam.objects.order_by('created_at')
    serializer_class = FttsTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

"""CASUALS"""
class DailyCivilWorkProductionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """ViewSet for the DailyCivilWorkProduction class"""

    queryset = DailyCivilWorkProduction.objects.all()
    serializer_class = DailyCivilWorkProductionSerializer

class CasualDailyRegisterViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """ViewSet for the FTTSCasualDailyRegister class"""

    queryset = CasualDailyRegister.objects.all()
    serializer_class = CasualDailyRegisterSerializer

class FTTSCasualDailyRegisterViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """ViewSet for the FTTSCasualDailyRegister class"""

    queryset = FTTSCasualDailyRegister.objects.all()
    serializer_class = FTTSCasualDailyRegisterSerializer
