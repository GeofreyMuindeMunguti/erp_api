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

# class FttsCommercialTeamFilesView(generics.RetrieveAPIView):
#     def get_queryset(self):
#         queryset = FttsCommercialTeam.objects.filter(site_name_id=self.kwargs["pk"])
#         return queryset
#     serializer_class = FttsCommercialTeamFilesSerializer



class FttsCommercialTeamASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FTTSProject.objects.all()
    serializer_class = FttsCommercialTeamASubTaskFilesSerializer


class FttsSurveyPhotosASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = FttsSurveyPhotosSubTaskAFilesSerializer

# class SiteTrenchingFilesFilesView(generics.RetrieveAPIView,DefaultsMixin):
#     def get_queryset(self):
#         queryset = SiteTrenching.objects.filter(site_name_id=self.kwargs["pk"])
#         return queryset
#     serializer_class = SiteTrenchingSubTaskFilesSerializer

##
class SiteTrenchingASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = SiteTrenchingSubTaskAFilesSerializer


##
# class SiteTrenchingFilesFilesView(generics.RetrieveAPIView,DefaultsMixin):
#     def get_queryset(self):
#         queryset = SiteTrenching.objects.filter(site_name_id=self.kwargs["pk"])
#         return queryset
#     serializer_class = SiteTrenchingSubTaskFilesSerializer



##
class SiteDuctASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = SiteDuctASubTaskFilesSerializer

##


# class SiteDuctInstallationFilesView(generics.RetrieveAPIView,DefaultsMixin):
#     def get_queryset(self):
#         queryset = SiteDuctInstallation.objects.filter(site_name_id=self.kwargs["pk"])
#         return queryset
#     serializer_class = SiteDuctInstallationSubTaskFilesSerializer

class ManHoleInstallationASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = ManHoleInstallationASubTaskFilesSerializer


# class ManHoleInstallationFilesView(generics.RetrieveAPIView,DefaultsMixin):
#     def get_queryset(self):
#         queryset = ManHoleInstallation.objects.filter(site_name_id=self.kwargs["pk"])
#         return queryset
#     serializer_class = ManHoleInstallationSubTaskFilesSerializer

# class SiteCableInstallationFilesView(generics.RetrieveAPIView,DefaultsMixin):
#     def get_queryset(self):
#         queryset = SiteCableInstallation.objects.filter(site_name_id=self.kwargs["pk"])
#         return queryset
#     serializer_class = SiteCableInstallationSubTaskFilesSerializer


class SiteCableInstallationASubTaskFilesView(generics.RetrieveAPIView,DefaultsMixin):
    queryset = FttsSite.objects.all()
    serializer_class = SiteCableInstallationASubTaskFilesSerializer


# class SiteTerminalInHseFilesView(generics.RetrieveAPIView,DefaultsMixin):
#     def get_queryset(self):
#         queryset = SiteTerminalInHse.objects.filter(site_name_id=self.kwargs["pk"])
#         return queryset
#     serializer_class = SiteTerminalInHseSubTaskFilesSerializer



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