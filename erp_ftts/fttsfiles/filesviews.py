"""Extract files and images per project.
"""
#---------
# Imports
#---------

from .filesserializers import *
from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from erp_ftts.models import *
from rest_framework import status, viewsets
from erp_core.fileshandler.filemixin import DefaultsMixin



#################################FILES  HANDLING VIEWS   BLOCK#####################################################


class FttsSiteFilesView(generics.RetrieveAPIView):
    ''' Main View to return all files per project'''

    queryset = FttsSite.objects.all()
    serializer_class = FttsSiteFilesSerializer



#

class FttsCommercialTeamASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTSProject.objects.all()
    serializer_class = FttsCommercialTeamASubTaskFilesSerializer


class FttsSurveyPhotosASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = FttsSurveyPhotosSubTaskAFilesSerializer


class SiteTrenchingASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = SiteTrenchingSubTaskAFilesSerializer

class SiteDuctASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = SiteDuctASubTaskFilesSerializer



class ManHoleInstallationASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = ManHoleInstallationASubTaskFilesSerializer



class SiteCableInstallationASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = SiteCableInstallationASubTaskFilesSerializer



class SiteTerminalInHseASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = SiteTerminalInHseASubTaskFilesSerializer



class SiteInterceptionFilesView(generics.RetrieveAPIView,DefaultsMixin):
    def get_queryset(self):
        queryset = SiteInterception.objects.filter(site_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = SiteInterceptionSubTaskFilesSerializer


class SiteInterceptionASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = SiteInterceptionASubTaskFilesSerializer