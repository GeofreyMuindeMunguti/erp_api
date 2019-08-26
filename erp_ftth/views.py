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


class FTTHProjectViewSet(DefaultsMixin,viewsets.ModelViewSet):
    """ViewSet for the FTTHProject class"""

    queryset = FTTHProject.objects.all()
    serializer_class = FTTHProjectSerializer

#################################FTTH VIEWSETS#################################


class FtthInterceptionPointViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthInterceptionPoint.objects.order_by('created_at')
    serializer_class = FtthInterceptionPointSerializer

    search_fields = ('interception_point_name', )
    ordering_fields = ('created_at', 'interception_point_name', )


class ftthSurveyPhotosViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ftthSurveyPhotos.objects.order_by('created_at')
    serializer_class = ftthSurveyPhotosSerializer

    search_fields = ('project_name', )
    ordering_fields = ('created_at', 'project_name', )


class ftthSurveyViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ftthSurvey.objects.order_by('created_at')
    serializer_class = ftthSurveySerializer

    search_fields = ('project_name', )
    ordering_fields = ('created_at', 'project_name', )


#################################END OF FTTH VIEWSETS##########################

class FtthCommercialTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthCommercialTeam.objects.order_by('created_at')
    serializer_class = FtthCommercialTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthProcurementTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthProcurementTeam.objects.order_by('created_at')
    serializer_class = FtthProcurementTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

################################################ FIBER CIVIL TEAM ##############################################################################################################################################################################################################################################
class FtthPoleInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthPoleInstallationImage.objects.order_by('created_at')
    serializer_class = FtthPoleInstallationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DailyFtthPoleInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyFtthPoleInstallation.objects.order_by('created_at')
    serializer_class = DailyFtthPoleInstallationSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthPoleInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthPoleInstallation.objects.order_by('created_at')
    serializer_class = FtthPoleInstallationSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
"""END"""
class FtthTrenchingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthTrenchingImage.objects.order_by('created_at')
    serializer_class = FtthTrenchingImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DailyFtthTrenchingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyFtthTrenching.objects.order_by('created_at')
    serializer_class = DailyFtthTrenchingSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthTrenchingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthTrenching.objects.order_by('created_at')
    serializer_class = FtthTrenchingSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
"""END"""
class FtthBackfillingImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthBackfillingImage.objects.order_by('created_at')
    serializer_class = FtthBackfillingImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DailyFtthBackfillingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyFtthBackfilling.objects.order_by('created_at')
    serializer_class = DailyFtthBackfillingSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthBackfillingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthBackfilling.objects.order_by('created_at')
    serializer_class = FtthBackfillingSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
"""END"""
class FtthCableInstallationImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthCableInstallationImage.objects.order_by('created_at')
    serializer_class = FtthCableInstallationImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DailyFtthCableInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyFtthCableInstallation.objects.order_by('created_at')
    serializer_class = DailyFtthCableInstallationSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthCableInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthCableInstallation.objects.order_by('created_at')
    serializer_class = FtthCableInstallationSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthCivilTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthCivilTeam.objects.order_by('created_at')
    serializer_class = FtthCivilTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

################################################ END ##############################################################################################################################################################################################################################################################

################################################ FIBER INSTALLATION TEAM ##############################################################################################################################################################################################################################################
class FtthSplicingEnclosureImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicingEnclosureImage.objects.order_by('created_at')
    serializer_class = FtthSplicingEnclosureImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DailyFtthSplicingEnclosureViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyFtthSplicingEnclosure.objects.order_by('created_at')
    serializer_class = DailyFtthSplicingEnclosureSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthSplicingEnclosureViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicingEnclosure.objects.order_by('created_at')
    serializer_class = FtthSplicingEnclosureSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
"""END"""
class FtthSplicingFATImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicingFATImage.objects.order_by('created_at')
    serializer_class = FtthSplicingFATImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DailyFtthSplicingFATViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyFtthSplicingFAT.objects.order_by('created_at')
    serializer_class = DailyFtthSplicingFATSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthSplicingFATViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicingFAT.objects.order_by('created_at')
    serializer_class = FtthSplicingFATSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
"""END"""
class FtthSplicingFDTImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicingFDTImage.objects.order_by('created_at')
    serializer_class = FtthSplicingFDTImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DailyFtthSplicingFDTViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyFtthSplicingFDT.objects.order_by('created_at')
    serializer_class = DailyFtthSplicingFDTSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthSplicingFDTViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicingFDT.objects.order_by('created_at')
    serializer_class = FtthSplicingFDTSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthSplicingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicing.objects.order_by('created_at')
    serializer_class = FtthCoreProvisionSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )
"""END"""
class FtthPowerLevelsImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthPowerLevelsImage.objects.order_by('created_at')
    serializer_class = FtthPowerLevelsImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DailyFtthPowerLevelsViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyFtthPowerLevels.objects.order_by('created_at')
    serializer_class = DailyFtthPowerLevelsSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthPowerLevelsViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthPowerLevels.objects.order_by('created_at')
    serializer_class = FtthPowerLevelsSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

"""END"""
class FtthOTDRTracesImageViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthOTDRTracesImage.objects.order_by('created_at')
    serializer_class = FtthOTDRTracesImageSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class DailyFtthOTDRTracesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = DailyFtthOTDRTraces.objects.order_by('created_at')
    serializer_class = DailyFtthOTDRTracesSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

class FtthOTDRTracesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthOTDRTraces.objects.order_by('created_at')
    serializer_class = FtthOTDRTracesSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class FtthSignalTestingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSignalTesting.objects.order_by('created_at')
    serializer_class = FtthSignalTestingSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class FtthIssuesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Issues ."""
    queryset = FtthIssues.objects.order_by('created_at')
    serializer_class = FtthIssuesSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class FtthInstallationTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthInstallationTeam.objects.order_by('created_at')
    serializer_class = FtthInstallationTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )


class FtthTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Issues ."""
    queryset = FtthTeam.objects.order_by('created_at')
    serializer_class = FtthTeamSerializer

    search_fields = ('project_name', )
    ordering_fields = ('updated_at', 'project_name', )

################################################ END ##############################################################################################################################################################################################################################################################
