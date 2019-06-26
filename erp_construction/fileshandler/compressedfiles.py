#from django.shortcuts import render
from rest_framework import generics, permissions, permissions, filters
from rest_framework.response import Response
from .filemixin import PermissionMixin
from erp_construction.models import Project
from rest_framework.views import APIView
from erp_construction.serializers   import ProjectSerializer
from django.http import Http404
from django.conf import settings
#################################FILES Compression Block#####################################################


class CompressedFilesDownload(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def make_tarfile(self,output_filename, source_dir):
        import tarfile
        import os
        with tarfile.open(output_filename, "w:gz") as tar:  # w.bz2 w.gz
            tar.add(source_dir, arcname=os.path.basename(source_dir))
            return output_filename


    def update_compressed_files(self):
        print('File compression started.')
        
        cfile = self.make_tarfile('media/projects/{}/files.tar.gz'.format(self.projectobject.project_name),'media/projects/{}/files/'.format(self.projectobject.project_name))
        cmage = self.make_tarfile('media/projects/{}/images.tar.gz'.format(self.projectobject.project_name),'media/projects/{}/images/'.format(self.projectobject.project_name))
        print('Compression Done')

        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        return cfile ,cmage


    def get(self, request, pk, format=None):
        """
        Return compressed files.
        """
        self.projectobject = self.get_object(pk)
        cfile,cmage =self.update_compressed_files()
        
        ##Hard Coded URLs for testing/Development

        compressed_project_files = 'http://127.0.0.1:8005/{}'.format(cfile)
        compressed_project_images = 'http://127.0.0.1:8005/{}'.format(cmage)

        print(compressed_project_files)
        return Response({'files':compressed_project_files,'images':compressed_project_images,})
        #return Response('Year bro I got you!!') 





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

 