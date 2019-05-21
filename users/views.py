from django.shortcuts import render
from users.serializers import *
from rest_framework import generics, permissions, viewsets, serializers, permissions, filters, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
