
#Probally more imports than i need, but i do not understand the difference 
import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os

appBuilder = "James Hannafin"
appBuildDate = datetime.date(2022,1,20)

#Time Deltas
delta_oneDay = datetime.timedelta(days = 1)
delta_oneWeek = datetime.timedelta(days = 7)

#Dates
date_today = datetime.datetime.today()
date_yesterday = (date_today - delta_oneDay)




class ParentWindow(Frame):
    
    def __init__ (self, master):
        Frame.__init__ (self) #***
        self.master = master #***
        destination = "No Destination Selected"
        source = "No Source Selected"
        dailyUpdates = IntVar() #***ERROR
        self.master.resizable(width=False,height=False) #Cannot resize the window
        self.master.geometry('{}x{}'.format(900,600)) #Window Size
        self.master.title("File Transfer") #App title
        self.master.config(bg='darkgray') #Window Background Color
                          
        #Source Label
        self.lbl_sourceLabel = Label(self.master,text="Source: ",font=("Helvetica",16),fg='black',bg='lightgray')
        self.lbl_sourceLabel.grid(row=0, column = 0,padx=(30,0),pady=(30,0))

        #Destination Label
        self.lbl_destinationLabel = Label(self.master,text="Destination: ",font=("Helvetica",16),fg='black',bg='lightgray')
        self.lbl_destinationLabel.grid(row=1, column = 0,padx=(30,0),pady=(30,0))

        #Selected Source
        self.lbl_source = Label(self.master,text=source,font=("Helvetica",16),fg='black',bg='lightblue')
        self.lbl_source.grid(row=0,column=3,padx=(30,0),pady=(30,0))

        #Selected Destination
        self.lbl_destination = Label(self.master,text=destination,font=("Helvetica",16),fg='black',bg='lightblue')
        self.lbl_destination.grid(row=1,column=3,padx=(30,0),pady=(30,0))

        #Select Source BTN
        self.btn_selSource= ttk.Button(win, text="Select", command=self.select_source)
        self.btn_selSource.grid(row = 0, column = 2,padx=(0,90),pady=(30,0))

        #Select Destination Button
        self.btn_selDest= ttk.Button(win, text="Select", command= self.select_destination)
        self.btn_selDest.grid(row = 1, column = 2,padx=(0,90),pady=(30,0))

        #Transfer all files Button
        self.btn_transferAll = Button(self.master, text = 'Transfer All', width=10, height = 2, command = self.transfer_all)
        self.btn_transferAll.grid(row=6,column=0,padx=(0,0),pady=(30,0))

        #Close the app
        self.btn_close = Button(self.master, text = 'Close', width=10, height = 2,command = self.close)
        self.btn_close.grid(row=6,column=3,padx=(0,90),pady=(30,0))

        #Daily Backup
        self.btn_dailyBackups = Checkbutton(self.master, text = "Daily Updates",variable=dailyUpdates)
        self.btn_dailyBackups.grid (row= 6, column = 2)

    

    #### Functions ####
        
    def select_source():#Select a source folder.
       source= filedialog.askdirectory()
       
    def select_destination():#Select a destination folder.
       destination= filedialog.askdirectory()
       
    def transfer_all():#Transfer all files from source to destination
        files = os.listdir(master.source)
        for i in files:
            shutil.move(source+i,destination)
            print("A file has been transferred")
         
    def close(self):#Close the app
        self.master.destroy()

#### #### Transfer Files that are older than 24 hours  #### ####        
    
##    if dailyUpdates == 1:
##        print("Running the datetime autotransfer module")
##        Run filetransfer algorithm
##        for i in files:
##            #We are saying move the files representred by i to their new destinations
##            currentFile = source+i
##            currentFileModDateTime =  os.path.getmtime(currentFile)
##            print(currentFileModDateTime)
##            print(date_yesterday)
##            if currentFileModDateTime > date_yesterday:
##                shutil.move(source+i,destination)
##                print("A file has been transferred")
##


print("Source:" + source)
print("Daily Updates:" + str(dailyUpdates))
print("Destination:" + destination)
print("Todays Date:"+ str(date_today))


if __name__ == "__main__":                  
    win = Tk()#Create initial window
    App = ParentWindow(win)#***
    win.mainloop()#Loop the program
