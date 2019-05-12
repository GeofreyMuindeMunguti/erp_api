from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from . serializers import *
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# User List
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Login Users
class UserLoginView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserloginSerializer

    def post(self, request, format='json'):
        serializer = UserloginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
