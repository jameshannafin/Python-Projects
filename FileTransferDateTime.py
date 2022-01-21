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

TOC = os.path.getmtime("C:\Users\James\Desktop\FolderBravo\Tales_Of_Cowardice.txt")
print(TOC)




