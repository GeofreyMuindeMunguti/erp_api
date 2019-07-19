from . import models

from rest_framework import serializers


class FTTHProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FTTHProject
        fields = (
            'pk', 
            'project_name', 
            'description', 
            'initial_kmz', 
            'is_acknowledged', 
            'created_by',
            'created_at', 
            'updated_at', 
            'is_active', 
        )

