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


# class FTTSProjectGetView(generics.RetrieveAPIView,DefaultsMixin):
#     ''' Main View to return all files per project'''

#     queryset = FttsSite.objects.all()
#     serializer_class = BtsSiteFilesSerializer


class FttsSiteFilesView(generics.RetrieveAPIView):
    ''' Main View to return all files per project'''

    queryset = FttsSite.objects.all()
    serializer_class = FttsSiteFilesSerializer


#     # Views for individual files type

class FttsCommercialTeamFilesView(generics.RetrieveAPIView):
    def get_queryset(self):
        queryset = FttsCommercialTeam.objects.filter(site_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = FttsCommercialTeamFilesSerializer

class SitePoleInstallationFilesView(generics.RetrieveAPIView):#,DefaultFilePermisionMixin):
    def get_queryset(self):
        queryset = SitePoleInstallation.objects.filter(site_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = SitePoleInstallationFilesSerializer






