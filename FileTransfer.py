#
#
# Python Ver: 3.8.5
#
# Author: Samantha Billips
#
#
# Assignment: File Transfer
#   1. Create 2 new folders on desktop labeled Folder A and Folder B
#   2. Create 4 .txt files with some meaningless content ("this is file 1",etc)
#       in folder A
#


# Create a scipt that will transfer files from folder A to folder B

import shutil
import os

# Set where the source of the files are
source = '/Users/saman/Desktop/FolderA/'

# set destination path to FolderB
destination = '/Users/saman/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
#move files represented by 'i' to their new destianation
    shutil.move(source+i, destination)
