from django.shortcuts import render
from erp_core.serializers import *
from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from .models import *
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


# class MainSiteViewSet(DefaultsMixin,viewsets.ModelViewSet):
#     """ViewSet for the MainSite class"""
#
#     queryset = MainSite.objects.order_by('created_at')
#     serializer_class = MainSiteSerializer
#
#     search_fields = ('site_name', )
#     ordering_fields = ('updated_at', 'site_name', )
