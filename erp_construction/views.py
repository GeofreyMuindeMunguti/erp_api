from django.shortcuts import render

from rest_framework.views import APIView,status
from rest_framework import viewsets,status,generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from . serializers import *
from . models import *
from django.contrib.auth.models import User

# Create your views here.
# User List
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
