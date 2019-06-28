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



##TODO _Code below Under research on usability/adaptability to  production enviroment /
baseurl = settings.ALLOWED_HOSTS
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
         # TO DO # rewrite below code in more  pythonic way : may be write vadidate function
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

            #TODO :::Resolve this issue //"http://127.0.0.1:8000/Images does not exist"

        #for tarfile
        compressed_project_files = baseurl+'/{}'.format(cfile)   ##Hard Coded URLs for testing/Development
        compressed_project_images = baseurl+'/{}'.format(cmage)   

        # for ZIP file

        compressed_project_files_zip = baseurl+'/{}'.format(zfile)   ##Hard Coded URLs for testing/Development
        compressed_project_images_zip = baseurl+'/{}'.format(zmage)   

        return Response({'files':compressed_project_files,'images':compressed_project_images,'files_Zip':compressed_project_files_zip,'images_Zip':compressed_project_images_zip,}) 
      


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
        #TO DO 
        #implement gZIP here instead of  TAR files

               ## Begin BLOCK to validate if files and images has been uploaded yet before compression and download
                # TO DO # rewrite below code in more  pythonic way : may be write vadidate function

        if os.path.exists(os.path.join('media','projects','{}'.format(self.projectobject.project_name),'files')) is False:
            efile =  'Files does not exist'
            zfile = 'Files does not exist'

            #os.mkdir(os.path.join('media','projects','{}'.format(self.projectobject),'files'))/make file dir if not existing
    
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

            #TO DO :::Resolve this issue //"http://127.0.0.1:8000/Images does not exist"
        # TO DO : Find a better way to address issues// Can on DEV /Debug=True

        compressed_project_files = baseurl+'/{}'.format(efile)   ##Hard Coded URLs for testing/Development/ replace with production URL
        compressed_project_images = baseurl+'/{}'.format(emage)   ##Hard Coded URLs for testing/Development

        compressed_project_files_zip = baseurl+'/{}'.format(zfile)   ##Hard Coded URLs for testing/Development
        compressed_project_images_zip = baseurl+'/{}'.format(zmage)   ##Hard Coded URLs for testing/Development
        
        return Response({'files':compressed_project_files,'images':compressed_project_images,'files_zip':compressed_project_files_zip,'images_zip':compressed_project_images_zip,}) 




###TODO DOWNLOAD STUFF //It seems download can only be done on frontend and not through API???

'''
##BACKEND 

file_path = file_url
FilePointer = open(file_path,"r")
response = HttpResponse(FilePointer,content_type='application/zip')
response['Content-Disposition'] = 'attachment; filename=NameOfFile'

return response.

##ANGULAR FRONTEND

   $http.get("http://"+$localStorage.ip+":"+$localStorage.port+"/exportDB").success(function(response) {
        var dataURI = 'data:application/octet-stream;base64,' + btoa(response);
        $('<a></a>').attr({
            download:  'db.csv',
            href: dataURI
        })[0].click();
    });

'''
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


#  #response = HttpResponse(mimetype='application/zip')
# #response['Content-Disposition'] = 'filename=logs_%s.zip' % date



# # filem = open('media/projects/Project1/images.tar.gz', 'rb')
# #return FileResponse(open(filem, 'rb'))


# #return Response({'files':compressed_project_files,'images':compressed_project_images,'files_Zip':compressed_project_files_zip,'images_Zip':compressed_project_images_zip,}) 

# zip_file = open('media/projects/Project1/files.tar.gz', 'rb')

# response = HttpResponse(zip_file, content_type='application/zip')
# response['Content-Disposition'] = 'attachment; filename=files.zip'

# return response


