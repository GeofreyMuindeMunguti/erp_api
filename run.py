import os
import time
import gc

SLEEP_TIME = 300 # you can change this as per your needs


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
