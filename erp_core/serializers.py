from rest_framework import serializers, exceptions
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import CustomUser
from .models import *
from rest_framework.authtoken.models import Token



class FiberBudgetSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = FiberBudget
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at', 'is_active')
