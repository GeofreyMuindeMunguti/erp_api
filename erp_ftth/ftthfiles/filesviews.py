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


class FTTHProjectGetView(generics.RetrieveAPIView,DefaultsMixin):
    ''' Main View to return all files per project'''

    queryset = FTTHProject.objects.all()
    serializer_class = FTTHProjectFilesSerializer


# class FttsSiteFilesView(generics.RetrieveAPIView):
#     ''' Main View to return all files per project'''

#     queryset = FttsSite.objects.all()
#     serializer_class = FttsSiteFilesSerializer



# #     # Views for individual files type

class FtthPoleInstallationilesView(generics.RetrieveAPIView):
    def get_queryset(self):
        queryset = FtthPoleInstallation.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = FtthPoleInstallationSubTaskFilesSerializer


class FtthTrenchingSubTaskFilesView(generics.RetrieveAPIView):
    def get_queryset(self):
        queryset =  FtthTrenching.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = FtthTrenchingSubTaskFilesSerializer


class FtthBackfillingSubTaskFilesView(generics.RetrieveAPIView):
    def get_queryset(self):
        queryset =  FtthBackfilling.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = FtthBackfillingSubTaskFilesSerializer