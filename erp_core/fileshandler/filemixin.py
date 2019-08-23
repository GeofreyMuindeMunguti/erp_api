#from django.shortcuts import render
from rest_framework import generics, permissions, permissions, filters
from django.utils.deconstruct import deconstructible


class DefaultsMixin(object):

    """Default settings for view authentication, permissions,filtering and pagination."""

    paginate_by = 25     # Pages of API end points/URLs
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (filters.SearchFilter,)

    #authentication_classes = (authentication.BasicAuthentication,authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

class PermissionMixin(object):

    """Default settings for files view authentication, permissions"""
    #authentication_classes = (authentication.BasicAuthentication,authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    #To DO
    # Add  file access restrictions to allow only specific roles to access and/or download files



@deconstructible  #fixmigrations issues
class UploadToProjectDir(object):
    '''Dynamically returns the project directory to which this file should be uploaded.'''
    path = "BTSProjects/{0}/{1}{2}"

    def __init__(self, sub_path):
        #Initialize instance with sub_path    i.e . #upload_dir = UploadToProjectDir('Projects/images/')
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        #Create  Project_name/Filename(self.sun_path)  Dir Structure
        return self.path.format(instance.project_name, self.sub_path, filename)



@deconstructible  #fixmigrations issues
class UploadToProjectDirDailyImage(object):
    '''Dynamically returns the project directory to which this file should be uploaded.'''
    path = "projects/{0}/{1}{2}"

    def __init__(self, sub_path):
        #Initialize instance with sub_path    i.e . #upload_dir = UploadToProjectDir('Projects/images/')
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        #Create  Project_name/Filename(self.sun_path)  Dir Structure
        #project_path = instance.images.split(:)[23]

        return self.path.format(project_path, self.sub_path, filename)
        