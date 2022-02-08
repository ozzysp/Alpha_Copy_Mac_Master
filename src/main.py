import os
import shutil
import psutil
from checksumdir import dirhash
from datetime import datetime
from pathlib import Path
from humanize import naturalsize

VOLUMES_PATH = '/System/Volumes/Data/Volumes'


# This class defines devices functions and charateristics
class Devices:
    SIZE = 0
    REM_SIZE = 0
    DATE = '00/00/0000'

    # This function list all volumes mounted in system
    def list_disks(self):
        directories = os.listdir(VOLUMES_PATH)
        return directories

    # This function returns used space in choosed hd
    def used_disk(self):
        used_disk = psutil.disk_usage(VOLUMES_PATH)
        used_space = str(used_disk[1])
        used_bytes = str(used_space[:6])
        natural_bytes = (naturalsize(used_bytes))
        return natural_bytes

    # This function display free space in chosen hd
    def free_disk(self):
        free_disk = psutil.disk_usage(VOLUMES_PATH)
        free_space = str(free_disk[2])
        free_bytes: str = free_space[:3]
        info_free = (free_bytes + ' GB Free')
        return info_free

    # This function select each hd
    def select_from(self, directories=None):
        found_volumes = directories
        return found_volumes

    # This function make new directory in target hd
    def make_new_dir(self):
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H:%M")
        path = os.getcwd()
        path = '/Users/ozz/Desktop'
        os.chdir(path)
        new_folder = dt_string
        os.mkdir(new_folder)

    # This function copy all content from original hd to destination hd
    def copy_files(self, src: str, dst: str):
        shutil.copy2(src, dst)
        with open(dst, 'a') as f:
            os.fsync(f)

        # This function show progress bar bytes
        def progress_bar_be(self):
            try:
                while True:
                    file_copy = (sum([f.stat().st_size for f in Path('/Users/ozz/Desktop/Copied_Files').glob("**/*")]))
                    file_origin = (sum([f.stat().st_size for f in
                                        Path('/Volumes/Mojave HD Ext/Users/ozzy/Downloads').glob("**/*")]))
                    if file_origin == file_copy:
                        break
            except FileNotFoundError:
                pass

        # This function checks integrity of copied files
        def check_hashes(self):
            directoryin = '/Volumes/CatalinaPatcher/Library'
            directoryout = '/Volumes/Mojave HD Ext/Users/ozzy/Desktop/Library'
            md5hashin = dirhash(directoryin, 'md5')
            md5hashout = dirhash(directoryout, 'md5')
            if md5hashin == md5hashout:
                print('This copy is ok')
            else:
                print('Error while copying')

        # This function eject all devices on mount point
        def eject_usb(self):
            command = "sudo udevadm info -q path -p /devices/pci0000:00/0000:00:1d.0/" \
                      "usb1/1-3/1-3.2/1-3.2.2/1-3.2.2.2/1-3.2.2.2:1.0/"
            popen = os.popen(command)
            output = popen.read()
            popen.close()
            output = output.split()
            output = output[1]
            if os.path.exists(output):
                os.remove(output)
                return output


def threading():
    pass


# This function eject all devices on mount point
def eject_usb():
    command = "sudo udevadm info -q path -p /devices/pci0000:00/0000:00:1d.0/usb1/1-3/1-3.2/1-3.2.2/1-3.2.2.2/1-3.2.2" \
              ".2:1.0/ "
    popen = os.popen(command)
    output = popen.read()
    popen.close()
    output = output.split()
    output = output[1]
    if os.path.exists(output):
        os.remove(output)
        return output
