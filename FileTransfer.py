

#### #### Datetime Module #### ####
import datetime
import os
appBuilder = "James Hannafin"
appBuildDate = datetime.date(2022,1,20)

#Time Deltas
delta_oneDay = datetime.timedelta(days = 1)
delta_oneWeek = datetime.timedelta(days = 7)

#Dates
date_today = datetime.datetime.today()
date_yesterday = (date_today - delta_oneDay)

#Console
print(date_today)
print(date_yesterday)
#### #### #### #### #### #### ####




#### #### File Transfer #### ####
import shutil


#set where the source of the files are
source = '/Users/James/Desktop/FolderAlpha/' #New/Modded Files

#Set the destination path to folder b
destination = '/Users/James/Desktop/FolderBravo/' #24 Hour Auto save.
files = os.listdir(source)#Create a list m


#Every 24 hours, run through a loop and check which files are 
for i in files:
    #We are saying move the files representred by i to their new destinations
    currentFile = source+i
    currentFileModDateTime =  os.path.getmtime(currentFile)
    print(currentFileModDateTime)
    print(date_yesterday)
    if currentFileModDateTime > date_yesterday:
        shutil.move(source+i,destination)
        print("A file has been transferred")
        
    
