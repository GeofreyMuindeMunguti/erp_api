#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time
import gc

# SLEEP_TIME = 300
#
# def update_folder_permissions():
#     """Update folder and file permissions
#     """
#
#     while True:
#         print("Running command...")
#         command = "chmod -R 755 media/"
#         os.system(command)
#         gc.collect()
#         print("Sleeping for {} seconds".format(SLEEP_TIME))
#         time.sleep(SLEEP_TIME)
#
#
# if __name__ == '__main__':
#     update_folder_permissions()

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erpProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
