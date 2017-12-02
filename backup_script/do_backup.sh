#!/bin/bash

rsync -aHv --delete-during --exclude-from=rsync-exclude.txt / /mnt/usbhd/pi_backup/
