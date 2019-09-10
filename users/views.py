from django.shortcuts import render
from django.contrib.auth.models import User
from users.serializers import *
from datetime import datetime

from rest_framework import generics,viewsets, serializers, filters, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny

from .serializers import JWTSerializer
from django.contrib.contenttypes.models import ContentType

# from users.permissions import IsLoggedInUserOrAdmin, IsAdminUser

# Create your views here.
# API
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
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    '''
    We configure the SearchFilter by adding a search_fields attribute to each
    ViewSet . We configure the OrderingFilter by adding a list of fields, which can be used
    for ordering the ordering_fields .
    '''


class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer


# Users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #         return [permission() for permission in permission_classes]

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


"""MESSAGING"""

"""CHAT"""
class ChatViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    def get_queryset(self):
     queryset = self.queryset
     query_set = (queryset.filter(sender=self.request.user)|queryset.filter(receiver=self.request.user))
     return query_set

class SentEmailViewSet(viewsets.ModelViewSet):

    serializer_class = SentEmailSerializer
    queryset = SentEmail.objects.all()
    def get_queryset(self):
        queryset = self.queryset
        query_set = (queryset.filter(sender=self.request.user)|queryset.filter(receiver=self.request.user))
        return query_set

class EmailConfigViewSet(viewsets.ModelViewSet):

    serializer_class = EmailConfigSerializer
    queryset = EmailConfig.objects.all()

"""END"""

# Permission
class PermissionMapViewSet(viewsets.ModelViewSet):
    queryset = PermissionMap.objects.all()
    serializer_class = PermissionMapSerializer


# location
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.order_by('created_at')
    serializer_class = LocationSerializer

    search_fields = ('location_name', )
    ordering_fields = ('updated_at', 'location_name', )


# casuals
class CasualViewSet(viewsets.ModelViewSet):
    queryset = Casual.objects.order_by('created_at')
    serializer_class = CasualSerializer

    search_fields = ('casual_name', )
    ordering_fields = ('updated_at', 'casual_name', )


class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.order_by('created_at')
    serializer_class = EngineerProfileSerializer

    lookup_fields = ( 'username')
    ordering_fields = ('updated_at', 'engineer_name', )


class RatesViewSet(viewsets.ModelViewSet):
    queryset = Rates.objects.order_by('created_at')
    serializer_class = RatesSerializer

    search_fields = ('id', )
    ordering_fields = ('updated_at', 'engineers_rate', )


class ContentTypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer

    search_fields = ('id', )




class ProjectTeamFTTSViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProjectTeam class"""

    queryset = ProjectTeamFTTS.objects.all()
    serializer_class = ProjectTeamFTTSSerializer
   # permission_classes = [permissions.IsAuthenticated]


class ProjectTeamFTTHViewSet(viewsets.ModelViewSet):
    """ViewSet for the ProjectTeam class"""

    queryset = ProjectTeamFTTH.objects.all()
    serializer_class = ProjectTeamFTTHSerializer
   # permission_classes = [permissions.IsAuthenticated]

