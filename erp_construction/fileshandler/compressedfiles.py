#from rest_framework import generics, permissions, permissions
from rest_framework.response import Response
from django.http import HttpResponse
from .filemixin import PermissionMixin
from erp_construction.models import Project
from rest_framework.views import APIView
from django.http import Http404
from django.conf import settings
from django.http import FileResponse
import os



baseurl = settings.BASE_IP  # use this in production
print(baseurl)

baseurl='http://127.0.0.1:8000'   ##Hard Coded URLs for testing/Development

#################################FILES Compression Block#####################################################
class CompressionMixin(object):

    def make_ZIP_file(self,output_filename ,source_dir):
        import shutil
        return shutil.make_archive(output_filename, 'zip', source_dir).split('erp_api')# / 'zip' change to get any other compression type


    def make_TAR_file(self,output_filename, source_dir): 
        import tarfile
        with tarfile.open(output_filename, "w:gz") as tar:  # w.bz2 / w.gz / w.xz   # Selections
            return tar.add(source_dir, arcname=os.path.basename(source_dir))



class UpdateCompressedFilesAndDownload(APIView,PermissionMixin,CompressionMixin):
    """
    Update and Retrieve compressed files & images per project
    """
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def make_ZIP_file(self,output_filename ,source_dir):
        import shutil
        return shutil.make_archive(output_filename, 'zip', source_dir).split('erp_api')[1] #TODO there is inconsistent path issue here to resolve
       # return output_filename


    def make_TAR_file(self,output_filename, source_dir): 
        import tarfile
        with tarfile.open(output_filename, "w:gz") as tar:  # w.bz2 / w.gz / w.xz   # Selections
            tar.add(source_dir, arcname=os.path.basename(source_dir))
            return output_filename


    def update_compressed_files(self):
        #TODO 
    
        ## Begin BLOCK to validate if files and images has been uploaded yet before compression and download
       
        if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject),'files')) is False:
            cfile = 'Files does not exist'
            zfile = 'Files does not exist'

            if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject),'images')) is False:
                cmage = 'Images does not exist'
                zmage = 'Images does not exist'

            else:

                cmage = self.make_TAR_file('media/projects/{}/images.tar.gz'.format(self.projectobject.project_name),'media/projects/{}/images/'.format(self.projectobject.project_name))
                zmage = self.make_ZIP_file('media/projects/{}/images'.format(self.projectobject.project_name),'media/projects/{}/images/'.format(self.projectobject.project_name))
        else:
            if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject),'images')) is False:
                cfile = self.make_TAR_file('media/projects/{}/files.tar.gz'.format(self.projectobject.project_name),'media/projects/{}/files/'.format(self.projectobject.project_name))
                cmage = 'Images does not exist'

                zfile = self.make_ZIP_file('media/projects/{}/files'.format(self.projectobject.project_name),'media/projects/{}/files/'.format(self.projectobject.project_name))
                zmage = 'Images does not exist'
            else:

                cfile = self.make_TAR_file('media/projects/{}/files.tar.gz'.format(self.projectobject.project_name),'media/projects/{}/files/'.format(self.projectobject.project_name))
                cmage = self.make_TAR_file('media/projects/{}/images.tar.gz'.format(self.projectobject.project_name),'media/projects/{}/images/'.format(self.projectobject.project_name))
                
                zfile = self.make_ZIP_file('media/projects/{}/files'.format(self.projectobject.project_name),'media/projects/{}/files/'.format(self.projectobject.project_name))
                zmage = self.make_ZIP_file('media/projects/{}/images'.format(self.projectobject.project_name),'media/projects/{}/images/'.format(self.projectobject.project_name))
               ## END  BLOCK to validate if files and images has been uploaded yet before compression and download
        
        return cfile , cmage ,zfile ,zmage


    def get(self, request, pk, format=None):
        """
        Return compressed files.
        """
        self.projectobject = self.get_object(pk)
        cfile,cmage ,zfile,zmage  =self.update_compressed_files()


        #for tarfile
        compressed_project_files = baseurl+'/{}'.format(cfile)   ##Hard Coded URLs for testing/Development
        compressed_project_images = baseurl+'/{}'.format(cmage)   

        # for ZIP file

        compressed_project_files_zip = baseurl+'{}'.format(zfile) 
        compressed_project_images_zip = baseurl+'{}'.format(zmage)   

       # return Response({'files':compressed_project_files,'images':compressed_project_images,'files_Zip':compressed_project_files_zip,'images_Zip':compressed_project_images_zip,}) 
        return Response({'files_Zip':compressed_project_files_zip,'images_Zip':compressed_project_images_zip,}) 
      


class DownloadExistingCompressedFiles(APIView,PermissionMixin):
    """
    Retrieve existing compressed files & images per project
    """
    
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get_existing_compressed_files(self):


        if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject.project_name),'files')) is False:
            efile =  'Files does not exist'
            zfile = 'Files does not exist'

    
            if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject.project_name),'images')) is False:
                emage = 'Images does not exist'
                zmage = 'Images does not exist'

            else:
                
                emage = 'media/projects/{}/images.tar.gz'.format(self.projectobject.project_name)
                zmage = 'Images does not exist'
        else:
            if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject),'images')) is False:
                
                emage = 'Images does not exist'
                efile = 'media/projects/{}/files.tar.gz'.format(self.projectobject.project_name)

                zmage = 'Images does not exist'
                zfile = 'media/projects/{}/files.zip'.format(self.projectobject.project_name)
            else:

                efile ='media/projects/{}/files.tar.gz'.format(self.projectobject.project_name)
                emage = 'media/projects/{}/images.tar.gz'.format(self.projectobject.project_name)

                zfile ='media/projects/{}/files.zip'.format(self.projectobject.project_name)
                zmage = 'media/projects/{}/images.zip'.format(self.projectobject.project_name)
               ## END  BLOCK to validate if files and images has been uploaded yet before compression and download
        
        return efile,emage ,zfile ,zmage
    
    def get(self, request, pk, format=None):
        """
        Return compressed files.
        """
        self.projectobject = self.get_object(pk)
        efile,emage ,zfile, zmage  =self.get_existing_compressed_files()

         

        compressed_project_files = baseurl+'/{}'.format(efile)   
        compressed_project_images = baseurl+'/{}'.format(emage)   

        compressed_project_files_zip = baseurl+'/{}'.format(zfile)   #
        compressed_project_images_zip = baseurl+'/{}'.format(zmage)   
        
        return Response({'files':compressed_project_files,'images':compressed_project_images,'files_zip':compressed_project_files_zip,'images_zip':compressed_project_images_zip,}) 




