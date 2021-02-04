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
import tkinter
from tkinter import *
import tkinter as tk


#Main GUI frame
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master.title("F.I.O.N.A.: File I/O Now Automated")

        #grids can be different dimensions
        self.labelTxt = Label(text = "Choose Source", font=("Arial", 12))
        self.labelTxt.grid(row=0,column=0, padx=20, pady=(20,0))

        self.txtEntry = Entry(self.master, font=("Helvetica", 12))
        self.txtEntry.grid(row=1, column=0, padx=(30,15), pady=(10,10), columnspan=2, sticky=W+E)

        self.btnSubmit = Button(self.master, text="Submit", width=12, height=1, command=self.customEntry)
        self.btnSubmit.grid(row=2, column=1, padx=(0,10) , pady=(0,10))

        self.master.columnconfigure(1,weight=1)

    #Custom GUI function for button commands 
    def customEntry(self):
        #retrieves/holds user input
        txtEntryVariable = self.txtEntry.get()

        
        #An action for this template to do smething would go below here
 
        


         

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

       
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
