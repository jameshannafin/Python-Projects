
#### #### IMPORTS #### ####
import datetime
from distutils import filelist
import string
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os

#DEVELOPER: James Hannafin
#Build Date = 2022,1,20

#Time Deltas
delta_oneDay = datetime.timedelta(days = 1) #Store time delta of one day in a var 
delta_oneWeek = datetime.timedelta(days = 7) #Store time delta of one week in a var 

#Dates
date_today = datetime.datetime.today() #Store todays date in a var
date_yesterday = (date_today - delta_oneDay) #Store yesterdays date in a var by subtracting the time delta of one day

class ParentWindow(Frame): #Main (only) GUI Window
    
    def __init__ (self, master): #question 1 ??
        Frame.__init__ (self) #??
        self.master = master #??
        destination = "No Destination Selected"
        source = "No Source Selected"
        dailyUpdates = IntVar #Declaring a var to use for the checkbox.
    
        self.master.resizable(width=False,height=False) #Cannot resize the window
        self.master.geometry('{}x{}'.format(900,600)) #Window Size
        self.master.title("File Transfer") #App title
        self.master.config(bg='darkgray') #Window Background Color

        #Source Label
        self.lbl_sourceLabel = Label(self.master,text="Source: ",font=("Helvetica",16),fg='black',bg='lightgray') #Create a label with the given parameters
        self.lbl_sourceLabel.grid(row=0, column = 0,padx=(30,0),pady=(30,0)) #Position the label as indicated 

        #Destination Label
        self.lbl_destinationLabel = Label(self.master,text="Destination: ",font=("Helvetica",16),fg='black',bg='lightgray')
        self.lbl_destinationLabel.grid(row=1, column = 0,padx=(30,0),pady=(30,0))

        #Selected Source *** I want these to update when a source or destination selected **question 2
        self.txt_source = Entry(self.master,font=("Helvetica,16"),fg='black',bg='lightblue')
        self.txt_source.grid(row=0,column=3,padx=(30,0),pady=(30,0))

        #Selected Destination *** I want these to update when a source or destination selected **question 2
        self.txt_destination = Entry(self.master,font=("Helvetica",16),fg='black',bg='lightblue')
        self.txt_destination.grid(row=1,column=3,padx=(30,0),pady=(30,0))

        #Select Source BTN ##Use the button widget to trigger a function which will open a file dialog 
        self.btn_selSource= ttk.Button(win, text="Select", command=self.select_source)
        self.btn_selSource.grid(row = 0, column = 2,padx=(0,90),pady=(30,0))

        #Select Destination Button ##Use the button widget to trigger a function which will open a file dialog 
        self.btn_selDest= ttk.Button(win, text="Select", command= self.select_destination)
        self.btn_selDest.grid(row = 1, column = 2,padx=(0,90),pady=(30,0))

        #Transfer all files Button ## A buttun to manually transfer all files from the source to the destination
        self.btn_transferAll = Button(self.master, text = 'Transfer All', width=10, height = 2, command = self.transfer_all)
        self.btn_transferAll.grid(row=6,column=0,padx=(0,0),pady=(30,0))

        #Close the app
        self.btn_close = Button(self.master, text = 'Close', width=10, height = 2,command = self.close)
        self.btn_close.grid(row=6,column=3,padx=(0,90),pady=(30,0))

    #### Functions ####

    #Select a source folder.
    def select_source(self):
        print("Source Changed")#Confirm this in the console
        self.txt_source.delete(0,'end')
        source= filedialog.askdirectory()
        self.txt_source.insert(0,source)
       
    #Select a destination folder.
    def select_destination(self):
        print("Destination Changed")#Confirm this in the consol
        self.txt_destination.delete(0,'end')
        destination = filedialog.askdirectory()
        self.txt_destination.insert(0,destination)
       
    #Transfer all files from the source to the the destination
    def transfer_all(self):#Transfer all files from source to destination
        oneDay = 86400.00 #Seconds
        source = self.txt_source.get()
        destination = self.txt_destination.get()
        filelist = os.listdir(source)
        print("Running the datetime autotransfer module")#Debug
        print("Source:" + source)
        print("File List:")
        print(filelist)
        
        for i in filelist: #Iterate through each item with a for loop

            #Identify the current file 
            currentFile = source+"/"+i 
            print("Checking file...")
            print("File Path:")
            print(currentFile)
            
            currentFileName = os.path.basename(currentFile)
            print("File Name:")
            print(currentFileName)

            currentFileModDateTime =  os.path.getmtime(currentFile) #Ascertain the time the current file was last modified
            print("File Last Modified:")
            print(currentFileModDateTime)

        
            if (currentFileModDateTime > oneDay ): #86,400 seconds are in a day, so if the current file hasnt been modified for over a day it will transfer 
                shutil.move(currentFile,destination)#Use the shutil module to .move a file to a new folder 
                print("A file has been transferred")

            

    #Close the app
    #   
    def close(self):
        self.master.destroy()

## Main Loop
if __name__ == "__main__":                  
    win = Tk()#Create initial window
    App = ParentWindow(win)#*** Question 4
    win.mainloop()#Loop the program
