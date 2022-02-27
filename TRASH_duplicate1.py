


#### #### Section 1: Imports #### ####
import webbrowser
import tkinter
from tkinter import *

#### #### Section 2: Root/Main Window Creation #### ####
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)#***
        self.master = master #***
        self.master.resizable(width=False,height=False)#Cant resize the window
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title("Webpage Generator!")#Title
        self.master.config(bg='darkgray')#BG Color

#### #### Section 3: Labels/Text #### ####                  
        self.varNewBody = StringVar()#Says this var will be text 

        ##Labels With text, font colors and positioning 
        self.lblNewBody = Label(self.master,text="new body content here.. ",font=("Helvetica",16),fg='black',bg='lightgray')
        self.lblNewBody.grid(row=1, column = 0,padx=(30,0),pady=(30,0))
        self.lblNewFile = Label(self.master,text="Click here to create a new file ",font=("Helvetica",16),fg='black',bg='lightgray')
        self.lblNewFile.grid(row=2, column = 0,padx=(30,0),pady=(30,0))

        ##The text entry field
        self.txtNewBody = Entry(self.master,text=self.varNewBody, font=("Helvetica",16),fg='black',bg='lightblue')
        self.txtNewBody.grid(row=1,column=1,padx=(30,0),pady=(30,0))


#### #### Section 4: Buttons #### ####
        self.btnCreate = Button(self.master, text = 'Create', width=10, height = 2, command = self.create)
        self.btnCreate.grid(row=0,column=1,padx=(0,0),pady=(30,0),sticky=NE)

        self.btnSubmit = Button(self.master, text = 'Add Body Content', width=10, height = 2, command = self.addNewBodyText)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0),sticky=NE)

        self.btnCancel = Button(self.master, text = 'Close', width=10, height = 2,command = self.close)
        self.btnCancel.grid(row=3,column=2,padx=(0,90),pady=(30,0),sticky=NE)

#### #### Section 5: Functions #### ####
    def addNewBodyText(self):
        ##This will be the button used to submit the new body text into the document
        newBodyText = self.varNewBody
        file = open("newpage.txt", "a")#Open the file using"a" to append the file/ add to it
        file.write("{}".format(newBodyText))#add in the new body text. *** But how do I specidy where its added
        file.close()
        
    def close(self):
        self.master.destroy()#Close the app 

    def create(self):  
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
        webbrowser.open_new_tab(newpage.txt)


#### #### Section 6: Other #### ####
if __name__ == "__main__":                  
    root = Tk()
    App = ParentWindow(root)#***
    root.mainloop()#Keep the app running
    
