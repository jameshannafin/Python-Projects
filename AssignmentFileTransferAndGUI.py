
#### #### IMPORTS #### ####
import datetime
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
        self.lbl_source = Label(self.master,text=source,font=("Helvetica",16),fg='black',bg='lightblue')
        self.lbl_source.grid(row=0,column=3,padx=(30,0),pady=(30,0))

        #Selected Destination *** I want these to update when a source or destination selected **question 2
        self.lbl_destination = Label(self.master,text=destination,font=("Helvetica",16),fg='black',bg='lightblue')
        self.lbl_destination.grid(row=1,column=3,padx=(30,0),pady=(30,0))

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

        #Daily Backup
        self.btn_dailyBackups = Checkbutton(self.master, text = "Daily Updates",variable=dailyUpdates)
        self.btn_dailyBackups.grid (row= 6, column = 2)

    

    #### Functions ####

    #Select a source folder.
    def select_source(self):
        print("Source Changed")#Confirm this in the console
        self.source= filedialog.askdirectory()
        self.files = os.listdir(self.source)

    #Select a destination folder.
    def select_destination(self):
        print("Destination Changed")#Confirm this in the console
        self.destination= filedialog.askdirectory()
       
    #Transfer all files from the source to the the destination
    def transfer_all(self):#Transfer all files from source to destination
        files = os.listdir(self.source)
        for i in files:
            shutil.move(self.source+i,self.destination)
            print("A file has been transferred")

    #Close the app
    #   
    def close(self):
        self.master.destroy()

#### #### Transfer Files that are older than 24 hours  #### ####        
    
        if self.dailyUpdates == 1: #If the daily backup checkbox is marked..
            print("Running the datetime autotransfer module")#Debug
            for i in self.files: #Iterate through each item with a for loop
                currentFile = self.source+i #Identify the current file 
                currentFileModDateTime =  os.path.getmtime(currentFile) #Ascertain the time the current file was last modified
                print("File last modified:" + currentFileModDateTime) #Print that time to the console 
                print("Yesterday:" + date_yesterday) #Print yesterday to the console 
                if currentFileModDateTime > date_yesterday: #*** Question 3 If last time the file was modified before yesterday, move it to the destination
                    shutil.move(currentFile,self.destination)#Use the shutil module to .move a file to a new folder 
                    print("A file has been transferred")


        #Debugging
        print("Source:" + self.source)
        print("Daily Updates:" + str(self.dailyUpdates))
        print("Destination:" + self.destination)
        print("Todays Date:"+ str(date_today))

## Main Loop
if __name__ == "__main__":                  
    win = Tk()#Create initial window
    App = ParentWindow(win)#*** Question 4
    win.mainloop()#Loop the program
