from django.shortcuts import render
from django.contrib.auth.models import User
from users.serializers import *

from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import JWTSerializer


# Create your views here.
class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
