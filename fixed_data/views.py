from . import models
from . import serializers
from rest_framework import viewsets, permissions


class ClientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Client class"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class TechnologyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Technology class"""

    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Service class"""

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class BuildingViewSet(viewsets.ModelViewSet):
    """ViewSet for the Building class"""

    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticated]


class LinkViewSet(viewsets.ModelViewSet):
    """ViewSet for the Link class"""

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

