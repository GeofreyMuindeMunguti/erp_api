#from django.shortcuts import render
from rest_framework import generics, permissions, permissions, filters
from rest_framework.response import Response
from .filemixin import PermissionMixin
from erp_construction.models import Project
from rest_framework.views import APIView
from erp_construction.serializers   import ProjectSerializer
from django.http import Http404
from django.conf import settings
import os
#################################FILES Compression Block#####################################################


class CompressedFilesDownload(APIView):
    """
    Retrieve compressed files & images per project
    """
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def make_tarfile(self,output_filename, source_dir):
        import tarfile
        with tarfile.open(output_filename, "w:xz") as tar:  # w.bz2 w.gz
            tar.add(source_dir, arcname=os.path.basename(source_dir))
            return output_filename


    def update_compressed_files(self):
        #TO DO 
        #implement gZIP here instead of  TAR files

               ## Begin BLOCK to validate if files and images has been uploaded yet before compression and download
                # TO DO # rewrite below code in more  pythonic way : may be write vadidate function

        
       
        if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject),'files')) is False:
            cfile = 'Files does not exist'
            if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject),'images')) is False:
                cmage = 'Images does not exist'
            else:
                cmage = self.make_tarfile('media/projects/{}/images.tar.xz'.format(self.projectobject.project_name),'media/projects/{}/images/'.format(self.projectobject.project_name))
            
        else:
            if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject),'images')) is False:
                cfile = self.make_tarfile('media/projects/{}/files.tar.xz'.format(self.projectobject.project_name),'media/projects/{}/files/'.format(self.projectobject.project_name))
                cmage = 'Images does not exist'
            else:

                cfile = self.make_tarfile('media/projects/{}/files.tar.xz'.format(self.projectobject.project_name),'media/projects/{}/files/'.format(self.projectobject.project_name))
                cmage = self.make_tarfile('media/projects/{}/images.tar.xz'.format(self.projectobject.project_name),'media/projects/{}/images/'.format(self.projectobject.project_name))

               ## END  BLOCK to validate if files and images has been uploaded yet before compression and download
        
        return cfile ,cmage


    def get(self, request, pk, format=None):
        """
        Return compressed files.
        """
        self.projectobject = self.get_object(pk)
        cfile,cmage =self.update_compressed_files()
        if type(cfile) is str:
            pass
            #TO DO :::Resolve this issue //"http://127.0.0.1:8005/Images does not exist"

        
        # TO DO : Find a better way to address issues// Can on DEV /Debug=True
        compressed_project_files = 'http://127.0.0.1:8005/{}'.format(cfile)   ##Hard Coded URLs for testing/Development
        compressed_project_images = 'http://127.0.0.1:8005/{}'.format(cmage)   ##Hard Coded URLs for testing/Development

        return Response({'files':compressed_project_files,'images':compressed_project_images,}) 





###TO DO DOWNLOAD STUFF

# import os
# file_name = 'media/projects/Project4/files4.tar.bz2'

# def download(request,file_name):
    
#     file_path = settings.MEDIA_ROOT +'/'+ file_name
#     file_wrapper = FileWrapper(file(file_path,'rb'))
#     file_mimetype = mimetypes.guess_type(file_path)
#     response = HttpResponse(file_wrapper, content_type=file_mimetype )
#     response['X-Sendfile'] = file_path
#     response['Content-Length'] = os.stat(file_path).st_size
#     response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name) 
#     return response

 