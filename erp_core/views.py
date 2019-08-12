from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets, permissions



class MainSiteViewSet(viewsets.ModelViewSet):
    """ViewSet for the MainSite class"""

    queryset = models.MainSite.objects.all()
    serializer_class = serializers.MainSiteSerializer
    permission_classes = [permissions.IsAuthenticated]
