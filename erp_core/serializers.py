from .models import Project

from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = (
            'id', 
            'project_name', 
            'project_type',
            'created_at', 
            'updated_at', 
            'is_active', 
        )

