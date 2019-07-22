from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import *
from erp_construction.models import *
from .models import *
from rest_framework.authtoken.models import Token


class FttsSiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsSite
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')


class FttsCommercialTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = FttsCommercialTeam
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
