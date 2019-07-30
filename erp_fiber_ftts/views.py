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
class FTTSProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the FTTSProject class"""

    queryset = FTTSProject.objects.order_by('created_at')
    serializer_class = FTTSProjectSerializer

    search_fields = ('project_name', )
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

class SiteTrenchingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = SiteTrenching.objects.order_by('created_at')
    serializer_class = SiteTrenchingSerializer

    search_fields = ('site_name', )
    ordering_fields = ('updated_at', 'site_name', )

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