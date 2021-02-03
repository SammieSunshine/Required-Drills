# Python Ver: 3.8.5
#
# Author: Samantha Billips
#
"""FILE TRANSFER ASSIGNMENT PART THREE
Users are now asking for a user interface to make using the script easier and more versatile.

Desired features of the UI:

Allow the user to browse and choose a specific folder that will contain the files to be checked daily.

Allow the user to browse and choose a specific folder that will receive the copied files.

Allow the user to manually initiate the 'file check' process that is performed by the script.

Add comments throughout your Python explaining your code.

You have been asked to create this UI."""

import shutil
import datetime
import os
from tkinter import *
from tkinter import filedialog



class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')


    def getPath(self):
        self.path = filedialog.askdirectory()
        return self.path

    def startButton(self, path_value):
        self.buttonFrame = Frame(self)
        self.buttonFrame.pack()
        self.start_Button = Button(self.buttonFrame, text = 'Start',
                                   path_value)).grid(row = 0, column =0)

    def beginOp(self, path_value):
        count = 0
        os.chdir(path_value)
        self.file_list = os.listdir()
        numFile = len(self.file_list)
        if len(self.file_list) == 0 :
            self.LabelErr = Label(text = "Error: Empty Folder").pack
            exit()
        for file in self.file_list:
            if file.endswith(".txt")
         

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
