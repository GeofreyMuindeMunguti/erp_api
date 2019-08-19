"""Extract files and images per project.
"""
#---------
# Imports
#---------

from .filesserializers import *
from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from erp_construction.models import *

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status, viewsets
from rest_framework.decorators import parser_classes
from rest_framework.decorators import detail_route
from erp_core.fileshandler.filemixin import DefaultsMixin



#################################FILES  HANDLING VIEWS   BLOCK#####################################################

class FilesView(APIView):

    def get(self, request, format=None):
        "TO DO"
        resp = "# TO DO        USE  erp_construction/ files/<int:pk>/  :  pk is project ID"
        return Response(resp)


class BtsSiteFilesView(generics.RetrieveAPIView,DefaultsMixin):
    ''' Main View to return all files per project'''

    queryset = BtsSite.objects.all()
    serializer_class = BtsSiteFilesSerializer



    # Views for individual files type

class SiteClearingFilesView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = SetSiteClearingImage.objects.all()
    def get_queryset(self):
        queryset = SetSiteClearingImage.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = SiteClearingFilesSerializer





class AccessApprovalFileCivilView(generics.RetrieveAPIView,DefaultsMixin):
    #queryset = AccessApprovalCivil.objects.all()
    def get_queryset(self):
        queryset = AccessApprovalCivil.objects.filter(project_name_id=self.kwargs["pk"])
        return queryset
    serializer_class = AccessApprovalFileCivilSerializer



