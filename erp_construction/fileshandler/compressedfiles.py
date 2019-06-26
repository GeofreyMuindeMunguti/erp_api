#from django.shortcuts import render
from rest_framework import generics, permissions, permissions, filters
from rest_framework.response import Response
from .filemixin import PermissionMixin
from erp_construction.models import Project
from rest_framework.views import APIView
#################################FILES Compression Block#####################################################

# Pull compressed file Views


# class FileArchiver(generics.RetrieveAPIView,PermissionMixin):
#     ''' view to GET compressed files and images'''
    
#     def make_tarfile(self,output_filename, source_dir):
#         import tarfile
#         import os
#         with tarfile.open(output_filename, "w:bz2") as tar:  # w.bz2 w.gz
#             tar.add(source_dir, arcname=os.path.basename(source_dir))
#             return output_filename

#         #TO DO

#     def update_compressed_files(self):
#         #pass
#         self.allfiles = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
#         self.allimages= self.make_tarfile('media/compressed/images.tar.bz2','media/images/')

#         # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
#         # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
#         # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        
#         # TO DO


#     def get(self, request,pk, format=None):
#         """
#         Compress files compressed files.
#         """

#         self.update_compressed_files()
    
#         all_filesfiles = 'http://127.0.0.1:8000/{}'.format(self.allfiles)
#         all_images =  'http://127.0.0.1:8000/{}'.format(self.allimages)

        
#         return Response({'all_files': all_filesfiles,'all_images':all_images,})

class CompressedFilesDownLoader(APIView):
    ''' Retrieve compressed files per project '''

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def make_tarfile(self,output_filename, source_dir):
        import tarfile
        import os
        with tarfile.open(output_filename, "w:bz2") as tar:  # w.bz2 w.gz
            tar.add(source_dir, arcname=os.path.basename(source_dir))
            return output_filename

        #TO DO

    def update_compressed_files(self):
        #pass
        print('updating files')
        self.allfiles = self.make_tarfile('media/compressed/files.tar.bz2','media/projects/{}/files/'.format(self.project_name))
        self.allimages = self.make_tarfile('media/compressed/files.tar.bz2','media/projects/{}/images/'.format(self.project_name))

        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        
        # TO DO

    def get(self, request,pk,format=None):
        """
        Compress files compressed files.
        """
        cfile= self.get_object(pk)

        self.project_name = cfile.project_name

        self.update_compressed_files()
    
        all_filesfiles = 'http://127.0.0.1:8000/{}'.format(self.allfiles)
        all_images =  'http://127.0.0.1:8000/{}'.format(self.allimages)

        
        return Response({'all_files': all_filesfiles,'all_images':all_images,})



    #  '''   


    # def get(self, request, format=None):
    #     """
    #     Return compressed files.
    #     """
    #     import os
    #     if (os.path.basename("media/compressed/files.tar.bz2") is  None):
    #         print('Yeaaaaa am there BRO!')
    #         compressed_project_files = 'http://127.0.0.1:8000/media/compressed/files.tar.bz2'
    #     else:
    #         print('File compression started.')
    #         cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
    #         print('Compression Done')
    #         compressed_project_files = 'http://127.0.0.1:8000/{}'.format(cfile)

    #     print(compressed_project_files)
    #     return Response({'files':compressed_project_files,'images':compressed_project_files,})

 

 # Pull compressed file Views

class FileArchiver(generics.RetrieveAPIView):
    ''' view to GET compressed files and images'''

    def make_tarfile(self,output_filename, source_dir):
        import tarfile
        import os
        with tarfile.open(output_filename, "w:bz2") as tar:  # w.bz2 w.gz
            tar.add(source_dir, arcname=os.path.basename(source_dir))
            return output_filename

    def update_compressed_files(self):
        pass
        self.allfiles = self.make_tarfile('media/projects/Project4/compressed/files.tar.bz2','media/projects/Project4/files/')
        self.allimages= self.make_tarfile('media/projects/Project4/compressed/images.tar.bz2','media/projects/Project4/images/')

        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')

    
    def get(self, request, format=None):
        """
        Return compressed files.
        """
        print('File compression started.')
        cfile = self.make_tarfile('media/projects/Project4/files4.tar.bz2','media/projects/Project4/files/')
        print('Compression Done')

        compressed_project_files = 'http://127.0.0.1:8000/{}'.format(cfile)

        print(compressed_project_files)
        return Response({'files':compressed_project_files,})


import os
file_name = 'media/projects/Project4/files4.tar.bz2'

def download(request,file_name):
    
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name) 
    return response

 