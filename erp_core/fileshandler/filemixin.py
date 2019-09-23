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




# need to be defactored


@deconstructible  #fixmigrations issues
class UploadToProjectDir(object):
    '''Dynamically returns the project directory to which this file should be uploaded.'''
    #path = "BTSProjects/{0}/{1}{2}"
    path = "{0}/{1}/{2}/{3}"

    def __init__(self,main_path ,sub_path):
        #Initialize instance with sub_path    i.e . #upload_dir = UploadToProjectDir('Projects/images/')
        self.sub_path = sub_path
        self.main_path =main_path

    def __call__(self, instance, filename):
        #Create  Project_name/Filename(self.sun_path)  Dir Structure
        try:
            project_path = str(instance.project_name).strip()
            return self.path.format(self.main_path ,project_path, self.sub_path, filename)

        except:
            return self.path.format(self.main_path,'FILES', self.sub_path, filename)



@deconstructible  #fixmigrations issues
class UploadToProjectDirSubTask(object):
    '''Dynamically returns the project directory to which this file should be uploaded.'''
   # path = "BTSProjects/{0}/{1}{2}"
    path = "{0}/{1}/{2}/{3}"

    def __init__(self,main_path, sub_path):
        #Initialize instance with sub_path    i.e . #upload_dir = UploadToProjectDir('Projects/images/')
        self.sub_path = sub_path
        self.main_path = main_path

    def __call__(self, instance, filename):
        #Create  Project_name/Filename(self.sun_path)  Dir Structure
        try:
            try:
                project_path = str(instance.project_name).split(':')[1].strip()
                return self.path.format(self.main_path ,project_path, self.sub_path, filename)
            except:
                project_path = str(instance.site_name).split(':')[1].strip()
                return self.path.format(self.main_path ,project_path, self.sub_path, filename)

        except Exception as e:
            print(e)
            return self.path.format(self.main_path ,'FILES', self.sub_path, filename)


@deconstructible  #fixmigrations issues
class UploadToProjectDirDate(object):
    '''Dynamically returns the project directory to which this file should be uploaded.'''
    path = "{0}/{1}/{2}{3}/{4}"
    
    def __init__(self, main_path ,sub_path):
        #Initialize instance with sub_path    i.e . #upload_dir = UploadToProjectDir('Projects/images/')
        self.sub_path = sub_path
        self.main_path = main_path

    def __call__(self, instance, filename):
        #Create  Project_name/Filename(self.sun_path)  Dir Structure
        try:

            project_path = str(instance.sub_task).split(':')[2].strip()

            return self.path.format(self.main_path ,project_path, self.sub_path,instance.work_day, filename)

        except:
            return self.path.format(self.main_path ,'FILES', self.sub_path,instance.work_day,  filename)

@deconstructible  #fixmigrations issues
class UploadToProjectDirImage(object):
    '''Dynamically returns the project directory to which this file should be uploaded.'''
    path = "{0}/{1}/{2}{3}/{4}"

    def __init__(self, main_path ,sub_path):
        #Initialize instance with sub_path    i.e . #upload_dir = UploadToProjectDir('Projects/images/')
        self.main_path = main_path
        self.sub_path = sub_path


    def __call__(self, instance, filename):
        #Create  Project_name/Filename(self.sun_path)  Dir Structure
        try:

            project_path = str(instance.day_image).split(':')[2].strip()
            date_path = str(instance.day_image).split(':')[4].strip()

            return self.path.format( self.main_path ,project_path, self.sub_path,date_path, filename)
            
        except:
            date_path = ''
            return self.path.format(self.main_path ,'FILES', self.sub_path,date_path,  filename)

