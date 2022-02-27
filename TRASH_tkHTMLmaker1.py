
#### #### Section 1: Imports #### ####
#from doctest import master
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile


### #### Section 2: Root/Main Window Creation #### ####
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self) #***
        txt_addBody = "Add body content here"
        self.master = master #***
        self.master.resizable(width=False,height=False) #Cannot resize the window
        self.master.geometry('{}x{}'.format(900,600)) #Window Size
        self.master.title("File Transfer") #App title
        self.master.config(bg='darkgray') #Window Background Color


        #### #### Section 3: Main Labels #### ####

        ##Label 1
        self.lbl_newPage = Label(btn_createFile = Button(self.master,text="Create File"),text="Create a new web page")#Create a label with this text
        self.lbl_newPage.grid(row=1, column = 0,columnspan = 3,padx=(30,0),pady=(30,0))

        #lbl_addBody = tk.Label(root,text="Add Content to an existing file")#Create a label with this text
        #lbl_addBody.grid(row=3, column = 2,padx=(30,0),pady=(30,0))

        #### #### Section 4: Buttons #### ####

        ##Add Body Button
        self.txt_addBody = StringVar()
        self.btn_addBody = Button(btn_createFile = Button(self.master,text="Create File"), textvariable=txt_addBody)
        #btn_addBody.grid(columnspan = 3, column = 1, row = 1)
        self.txt_addBody.set("Add Body")
        self.btn_addBody.grid(row=3, column = 3,padx=(30,0),pady=(30,0))

        ##Create New File Button ***Not showing up
        self.btn_createFile = Button(self.master,text="Create File")
        self.btn_createFile.grid(row=3, column = 1,padx=(30,0),pady=(30,0))

       # self.newBodyText = text(root)
       # self.newBodyText.grid(row=2, column = 2,padx=(30,0),pady=(30,0))

        #### #### Section 5: Button Functions #### ####

#         ## Open the file upon clicking.
#         def open_file():
#             file = filedialog.askfile()
#             print("Opening a file...")
#         ##This will be the button used to submit the new body text into the document
#         def add_body():
#             file = open("newpage.html", "a")#Open the file using"a" to append the file/ add to it
#             file.write("{}".format(newBodyText))#add in the new body text. *** But how do I specidy where its added
#             file.close()

#         #### #### Section 6: Create a new html file #### #### #Works
#         def create_file():  
#             newPage = open("newpage.html", "w")#Link a variable with a newly created file with the specified name, if it does not exist already..
#             ##The following will write a basic HTML template into the new file
#             newPage.write("""

#             <!DOCTYPE html>
#             <html lang ='en'>  
#             <head>     
#                             <title>Stay Tuned</title>
#                             <meta charset = "utf-8">
#             </head>  
#             <body> 
#                                     <p>Stay tuned for more details!</p>
#             </body>  
#             </html>

#             """)

#             newPage.close()#Close the file we opened/created because were not changing it right now 

# #### #### Section 7: Open The newly created file #### ####

# newPage = open("newpage.txt")
# print(newPage.read()) 

# webbrowser.open_new_tab(newpage.txt)#Open the new file in browser.. But how do i get the URL of a newly created page


#### #### Section 9: Other #### ####
if __name__ == "__main__":                  
    win = Tk()#Create initial window
    App = ParentWindow(win)#***
    win.mainloop()#Loop the program
