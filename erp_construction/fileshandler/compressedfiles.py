#from django.shortcuts import render
from rest_framework import generics, permissions, permissions, filters
from rest_framework.response import Response
from .filemixin import PermissionMixin




#################################FILES Compression Block#####################################################



# Pull compressed file Views


class FileArchiver(generics.RetrieveAPIView,PermissionMixin):
    ''' view to GET compressed files and images'''

    def make_tarfile(self,output_filename, source_dir):
        import tarfile
        import os
        with tarfile.open(output_filename, "w:bz2") as tar:  # w.bz2 w.gz
            tar.add(source_dir, arcname=os.path.basename(source_dir))
            return output_filename

    def update_compressed_files(self):
        #pass
        self.allfiles = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        self.allimages= self.make_tarfile('media/compressed/files.tar.bz2','media/images/')

        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
        # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')

    def get(self, request, format=None):
        """
        Compress files compressed files.
        """
     
            cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
            print('Compression Done')
            compressed_project_files = 'http://127.0.0.1:8000/{}'.format(cfile)

        print(compressed_project_files)
        return Response({'files':compressed_project_files,'images':compressed_project_files,})


        
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

 

#  # Pull compressed file Views

# class FileArchiver(generics.RetrieveAPIView):
#     ''' view to GET compressed files and images'''

#     def make_tarfile(self,output_filename, source_dir):
#         import tarfile
#         import os
#         with tarfile.open(output_filename, "w:bz2") as tar:  # w.bz2 w.gz
#             tar.add(source_dir, arcname=os.path.basename(source_dir))
#             return output_filename

#     def update_compressed_files(self):
#         pass
#         self.allfiles = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
#         self.allimages= self.make_tarfile('media/compressed/files.tar.bz2','media/files/')

#         # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
#         # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
#         # cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')

    
#     def get(self, request, format=None):
#         """
#         Return compressed files.
#         """
#         import os
#         if (os.path.basename("media/compressed/files.tar.bz2") is  None):
#             print('Yeaaaaa am there BRO!')
#             compressed_project_files = 'http://127.0.0.1:8000/media/compressed/files.tar.bz2'
#         else:
#             print('File compression started.')
#             cfile = self.make_tarfile('media/compressed/files.tar.bz2','media/files/')
#             print('Compression Done')
#             compressed_project_files = 'http://127.0.0.1:8000/{}'.format(cfile)

#         print(compressed_project_files)
#         return Response({'files':compressed_project_files,'images':compressed_project_files,})

 