#!/bin/bash

#THIS VERSION ATTEMPTS TO BACKUP DIRECTLY TO A BOOTABLE SD.  DOES IT WORK??? WHO KNOWS?
#be sure to mount the **second** SD partition

rsync -aHAXvr --delete-during --exclude-from=rsync-exclude.txt / /mnt/usbhd/
