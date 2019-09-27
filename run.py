<<<<<<< HEAD
 
=======
#!/usr/bin/env python
"""FILE PERMISSIONS"""

>>>>>>> 90696d15faae8c0cb87a9190e0c1cc49f55b9f6c
import os
import time
import gc

<<<<<<< HEAD
SLEEP_TIME = 600 # you can change this as per your needs
=======
SLEEP_TIME = 300 # you can change this as per your needs
>>>>>>> 90696d15faae8c0cb87a9190e0c1cc49f55b9f6c


def update_folder_permissions():
    """Update folder and file permissions
    """

    while True:
        print("Running command...")
        command = "chmod -R 755 media/"
        os.system(command)
        gc.collect()
        print("Sleeping for {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    update_folder_permissions()
