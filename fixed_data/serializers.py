from .models import *

from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = '__all__'




class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__' 


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = '__all__'



class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'




