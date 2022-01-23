

import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os

appBuilder = "James Hannafin"
appBuildDate = datetime.date(2022,1,20)


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)
        self.master = master
        selectedFile = "Select a file to modify one"
        self.master.resizable(width=False,height=False)
        self.master.geometry('{}x{}'.format(900,700))
        self.master.title("File Transfer")
        self.master.config(bg='darkgray')
                          
        #Title
        self.lbl_titleLabel = Label(self.master,text="File Maker ",font=("Helvetica",16),fg='black',bg='lightgray')
        self.lbl_titleLabel.grid(row=0, column = 0,columnspan = 2,padx=(30,0),pady=(30,0))
        #Instructions
        self.lbl_title = Label(self.master,text="Create a new file or a modify an old one")
        self.lbl_title.grid(row=1, column = 0,columnspan = 3,padx=(30,0),pady=(30,0))                  


        #Create File BTN
        self.btn_createFile= ttk.Button(win, text="Create File", command=self.create_file)
        self.btn_createFile.grid(row = 2, column = 1,padx=(0,90),pady=(30,0))

        self.ipt_newBody = Text(master)
        self.ipt_newBody.grid(row = 3, column = 0, rowspan = 2, columnspan = 3)
        
        #Select File BTN
        self.btn_selFile= ttk.Button(win, text="Select File", command=self.select_file)
        self.btn_selFile.grid(row = 5, column = 1,padx=(0,90),pady=(30,0))

        #Modify File Button
        self.btn_selDest= ttk.Button(win, text="Modify Selected", command= self.modify_file)
        self.btn_selDest.grid(row = 5, column = 2,padx=(0,90),pady=(30,0))

        #Close the app
        self.btn_close = Button(self.master, text = 'Close', width=10, height = 2,command = self.close)
        self.btn_close.grid(row=5,column=3,padx=(0,90),pady=(30,0))


#### This function to create a new file works when ran in an isolated environment, but here it gives an error saying that I am giving an argument for its not existent parameters...

    #### Functions ####
    def create_file():#WORKING. this function creates a new file.#
        newPage = open("newpage.txt", "w")#Link a variable with a newly created file with the specified name, if it does not exist already..
        ##The following will write a basic HTML template into the new file
        newPage.write("""
        <!DOCTYPE html>
        <html lang ='en'>  
        <head>     
                        <title>Stay Tuned</title>
                        <meta charset = "utf-8">
        </head>  
        <body> 
                                <p>Stay tuned for more details!</p>
        </body>  
        </html>
        """)
        newPage.close()#Close the file we opened/created because were not changing it right now 
                
    def select_file():#Select a file to modify, not working.
        print("select file")
        #selectedFile = filedialog.askopenfilename(initialdir="/")
       
    def modify_file():#Add content to an existing file, not working
        print("Modify file")
        #def retrieve_input():
            #newBodyText = self.ipt_newBody.get("1.0",END)
        #Now insert this var into a specic point do I use SQLite?
         
    def close(self):#Close the program
        self.master.destroy()
        

if __name__ == "__main__":  #Loop the program                
    win = Tk()
    App = ParentWindow(win)
    win.mainloop()

