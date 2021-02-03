# Python Ver: 3.8.5
#
# Author: Samantha Billips
#
"""FILE TRANSFER ASSIGNMENT PART TWO
 But now your company's users create or edit a collection of text files throughout the day.
 These text files represent data about customer orders.
 Once per day, any files that are new, or that were edited within the previous 24 hours,
 must be sent to the home office. To facilitate this, these new or updated files need to be copied to
 a specific 'destination' folder on a computer so that a special file transfer program can grab them and
 transfer them to the home office.
 The process of figuring out which files are new or recently edited (and copying them to the 'destination' folder),
 is currently being done manually. This is very expensive in terms of manpower.
   1. Create two folders: one to hold the files that get created or modified throughout the day, and another to receive
       the folders that your script determines should be copied over daily.
   2. To aid in your development efforts, you should create .txt files to add to the first folder,
       using Notepad or a similar program. You should also copy some older text files in there if you'd like. You should
       use files that you can edit so that you can control whether or not they are meant to be detected as 'modified in the
       last 24 hours' by your program.
   3. Create a script that will automate this task."""

import shutil
import datetime
import os


# Folder with created/edited files
src = '/Users/saman/Desktop/TA-python-course/FilesBase/'

# automate modified files to this folder
dest = '/Users/saman/Desktop/TA-python-course/FilesSend/'


files = os.listdir(src)
dest = os.listdir(dest)

os.chdir(src)

for file in files:
    with open(file) as f:
        print(file, f.read())

for file in files:
    
        shutil.copy(file, dest) #copies files represented by 'i' to dest_folder. if dest_folder already contains files,they will be overwritten

for file in files:
    if os.path.isfile(file): #checks to see if items are files
        shutil.copy(file, dest) #copies files represented by 'file' to dest_folder. if dest_folder already contains files,they will be overwritten


for file in files:
    if os.path.isfile(file): #checks to see if items are files
        shutil.move(file, dest) #copies files represented by 'file' to dest_folder. if dest_folder already contains files,they will be overwritten

for file in files:
    if os.path.isfile(file): #checks to see if items are files
        print(dest_folder)
        full_dest = os.path.join(dest, file) #connects/joins the folder
        print(full_dest)
        print("\n")
        shutil.move(file, full_dest) #files moved to dest_folder
