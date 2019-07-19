from . import models
from . import serializers
from rest_framework import viewsets, permissions


class FTTHProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the FTTHProject class"""

    queryset = models.FTTHProject.objects.all()
    serializer_class = serializers.FTTHProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

