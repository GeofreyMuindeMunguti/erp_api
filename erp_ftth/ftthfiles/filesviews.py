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


# #     # Views for individual files type


class FtthPoleInstallationASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTHProject.objects.all()
    serializer_class = FtthPoleInstallationSubTaskAFilesSerializer


class FtthTrenchingASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTHProject.objects.all()
    serializer_class = FtthTrenchingSubTaskAFilesSerializer


class FtthBackfillingASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTHProject.objects.all()
    serializer_class = FtthBackfillingSubTaskAFilesSerializer

class FtthCableInstallationASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTHProject.objects.all()
    serializer_class = FtthCableInstallationSubTaskAFilesSerializer

class FtthSplicingEnclosureASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTHProject.objects.all()
    serializer_class = FtthSplicingEnclosureASubTaskFilesSerializer

class FtthSplicingFATASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTHProject.objects.all()
    serializer_class = FtthSplicingFATASubTaskFilesSerializer

class FtthSplicingFDTASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTHProject.objects.all()
    serializer_class = FtthSplicingFDTASubTaskFilesSerializer


class FtthCoreProvisionASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    ''' View for ftth core provisioning files'''
    queryset = FTTHProject.objects.all()
    serializer_class = FtthCoreProvisionASubTaskFilesSerializer

class FtthPowerLevelsASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTHProject.objects.all()
    serializer_class = FtthPowerLevelsASubTaskFilesSerializer


class FtthOTDRTracesASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTHProject.objects.all()
    serializer_class =FtthOTDRTracesASubTaskFilesSerializer
