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

################################################ FIBER CIVIL TEAM ##############################################################################################################################################################################################################################################
class SitePoleInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SitePoleInstallation.objects.order_by('created_at')
    serializer_class = SitePoleInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteTrenchingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteTrenching.objects.order_by('created_at')
    serializer_class = SiteTrenchingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteDuctInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteDuctInstallation.objects.order_by('created_at')
    serializer_class = SiteDuctInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteCableInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteCableInstallation.objects.order_by('created_at')
    serializer_class = SiteCableInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteManHoleInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ManHoleInstallation.objects.order_by('created_at')
    serializer_class = SiteManHoleInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsCivilTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FttsCivilTeam.objects.order_by('created_at')
    serializer_class = FttsCivilTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

################################################ END ##############################################################################################################################################################################################################################################################

################################################ FIBER INSTALLATION TEAM ##############################################################################################################################################################################################################################################

class SiteTerminalInHseViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteTerminalInHse.objects.order_by('created_at')
    serializer_class = SiteTerminalInHseSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteInterceptionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteInterception.objects.order_by('created_at')
    serializer_class = SiteInterceptionSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsIssuesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Issues ."""
    queryset = FttsIssues.objects.order_by('created_at')
    serializer_class = FttsIssuesSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FttsInstallationTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FttsInstallationTeam.objects.order_by('created_at')
    serializer_class = FttsInstallationTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Issues ."""
    queryset = FttsTeam.objects.order_by('created_at')
    serializer_class = FttsTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

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
