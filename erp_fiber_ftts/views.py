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
from erp_core.viewspermissions import DefaultsMixin # Access controll to views


class FTTSProjectViewSet(viewsets.ModelViewSet,DefaultsMixin):
    """ViewSet for the FTTSProject class"""

    queryset = FTTSProject.objects.all()
    serializer_class = FTTSProjectSerializer
    
    search_fields = ('project_name','project_name' )
    ordering_fields = ('updated_at', 'site_name', )

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

class ProjectTrenchingViewSet(viewsets.ModelViewSet,DefaultsMixin):
    """ViewSet for the ProjectTrenching class"""

    queryset = ProjectTrenching.objects.all()
    serializer_class = ProjectTrenchingSerializer


class SiteTrenchingViewSet(viewsets.ModelViewSet,DefaultsMixin):
    """ViewSet for the SiteTrenching class"""

    queryset = SiteTrenching.objects.all()
    serializer_class = SiteTrenchingSerializer


class FTTSTrenchingImageViewSet(viewsets.ModelViewSet,DefaultsMixin):
    """ViewSet for the FTTSTrenchingImage class"""

    queryset = FTTSTrenchingImage.objects.all()
    serializer_class = FTTSTrenchingImageSerializer
    #permission_classes = [permissions.IsAuthenticated]

# class SiteTrenchingViewSet(DefaultsMixin, viewsets.ModelViewSet):
#     queryset = SiteTrenching.objects.order_by('created_at')
#     serializer_class = SiteTrenchingSerializer

#     search_fields = ('site_name', )
#     ordering_fields = ('updated_at', 'site_name', )


class SiteBackfillingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteBackfilling.objects.order_by('created_at')
    serializer_class = SiteBackfillingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteCableInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteCableInstallation.objects.order_by('created_at')
    serializer_class = SiteCableInstallationSerializer

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

class SiteIntegrationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteIntegration.objects.order_by('created_at')
    serializer_class = SiteIntegrationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class SiteAsBuiltViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteAsBuilt.objects.order_by('created_at')
    serializer_class = SiteAsBuiltSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FttsInstallationTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FttsInstallationTeam.objects.order_by('created_at')
    serializer_class = FttsInstallationTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

################################################ END ##############################################################################################################################################################################################################################################################
