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


class DefaultsMixin(object):
    paginate_by = 25     # Pages of API end points/URLs
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (filters.SearchFilter,)


class FTTHProjectViewSet(DefaultsMixin,ModelViewSet):
    """ViewSet for the FTTHProject class"""

    queryset = FTTHProject.objects.all()
    serializer_class = FTTHProjectSerializer



class FtthCommercialTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthCommercialTeam.objects.order_by('created_at')
    serializer_class = FtthCommercialTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthProcurementTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthProcurementTeam.objects.order_by('created_at')
    serializer_class = FtthProcurementTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

################################################ FIBER CIVIL TEAM ##############################################################################################################################################################################################################################################

class FtthPoleInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthPoleInstallation.objects.order_by('created_at')
    serializer_class = FtthPoleInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthTrenchingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthTrenching.objects.order_by('created_at')
    serializer_class = FtthTrenchingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthBackfillingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthBackfilling.objects.order_by('created_at')
    serializer_class = FtthBackfillingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthCableInstallationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthCableInstallation.objects.order_by('created_at')
    serializer_class = FtthCableInstallationSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthCivilTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthCivilTeam.objects.order_by('created_at')
    serializer_class = FtthCivilTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

################################################ END ##############################################################################################################################################################################################################################################################

################################################ FIBER INSTALLATION TEAM ##############################################################################################################################################################################################################################################

class FtthSplicingEnclosureViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicingEnclosure.objects.order_by('created_at')
    serializer_class = FtthSplicingEnclosureSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthSplicingFATViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicingFAT.objects.order_by('created_at')
    serializer_class = FtthSplicingFATSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthSplicingFDTViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicingFDT.objects.order_by('created_at')
    serializer_class = FtthSplicingFDTSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthSplicingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSplicing.objects.order_by('created_at')
    serializer_class = FtthCoreProvisionSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthPowerLevelsViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthPowerLevels.objects.order_by('created_at')
    serializer_class = FtthPowerLevelsSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthOTDRTracesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthOTDRTraces.objects.order_by('created_at')
    serializer_class = FtthOTDRTracesSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthAsBuiltViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthAsBuilt.objects.order_by('created_at')
    serializer_class = FtthAsBuiltSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthSignalTestingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthSignalTesting.objects.order_by('created_at')
    serializer_class = FtthSignalTestingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

class FtthInstallationTeamViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = FtthInstallationTeam.objects.order_by('created_at')
    serializer_class = FtthInstallationTeamSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )
################################################ END ##############################################################################################################################################################################################################################################################
