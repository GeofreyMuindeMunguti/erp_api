#from django.shortcuts import render
from rest_framework import generics, permissions, permissions, filters





class DefaultsMixin(object):

    """Default settings for view authentication, permissions,filtering and pagination."""

    paginate_by = 25     # Pages of API end points/URLs
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (filters.SearchFilter,)

    #authentication_classes = (authentication.BasicAuthentication,authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,) 

class PermissionMixinMixin(object):

    """Default settings for files view authentication, permissions"""
    #authentication_classes = (authentication.BasicAuthentication,authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,) 

    #To DO
    # Add  file access restrictions to allow only specific roles to access and/or download files
