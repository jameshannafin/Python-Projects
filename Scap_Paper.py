#### #### #### ####
    # HTML MAKER 
#### #### #### ####
    # By James Hannafin
#### #### #### ####

#### #### IMPORTS #### ####
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from webbrowser import open_new_tab

#Main Parent Frame Window
class ParentWindow(Frame):
    def __init__ (self, master):#*** Question1 
        Frame.__init__ (self)#***
        self.master = master #***
        selectedFile = "Select a file or create one to modify it" #Var for where the selected file to modify is stored 
        self.master.resizable(width=False,height=False)#Window nonchangeable
        self.master.geometry('{}x{}'.format(1200,700))#Window size
        self.master.title("File Transfer") #App Title
        self.master.config(bg='darkgray')#BG Color
                          
        #Title Label - top left
        self.lbl_titleLabel = Label(self.master,text="File Maker ",font=("Helvetica",16),fg='black',bg='lightgray') #Create a text label with the given parameters
        self.lbl_titleLabel.grid(row=0, column = 0,columnspan = 2,padx=(0,0),pady=(0,0)) # Position that label on the grid 

        #Instructions Label
        self.lbl_title = Label(self.master,text="Create a new file and modify it or select another basic HTML file to modify.")
        self.lbl_title.grid(row=1, column = 0,columnspan = 3,padx=(50,0),pady=(0,0))

        #Selected File Label *** I want this to update if a file is selected.. Question 2
        self.lbl_selectedFile = Label(self.master,text=selectedFile)
        self.lbl_selectedFile.grid(row=1, column = 4,padx=(0,0),pady=(0,0))

        #Modify File Text Input Box ** I am trying to center this on screen, but I cannot get the grid system to cooperate 
        self.ipt_newBody = Text(master)
        self.ipt_newBody.grid(row = 3, column = 1, rowspan = 2, columnspan = 3)
            
        #Spacer
        self.lbl_spacer = Label(self.master,text=" ")
        self.lbl_spacer.grid(row = 6, column = 0,padx=(0,0),pady=(0,0))
        #Spacer
        self.lbl_spacer = Label(self.master,text=" ")
        self.lbl_spacer.grid(row = 5, column = 0,padx=(0,0),pady=(0,0))

        
        #Create File BTN 
        self.btn_createFile= ttk.Button(win, text="Create File", command=self.create_file) #create a button. Trigger a function on click 
        self.btn_createFile.grid(row = 6, column = 1,padx=(0,0),pady=(0,0))

        #Select File BTN
        self.btn_selFile= ttk.Button(win, text="Select File", command=self.select_file)#create a button. Trigger a function on click 
        self.btn_selFile.grid(row = 6, column = 2,padx=(0,0),pady=(0,0))

        #Modify File Button
        #if selectedFile != "Select a file to modify one":
        self.btn_selDest= ttk.Button(win, text="Modify Selected", command= self.modify_file)#create a button. Trigger a function on click 
        self.btn_selDest.grid(row = 6, column = 3,padx=(0,0),pady=(0,0))

        #Close the app
        self.btn_close = Button(self.master, text = 'Close', width=10, height = 2,command = self.close)#create a button. Trigger a function on click 
        self.btn_close.grid(row=6,column=4,padx=(0,0),pady=(0,0))

    #### Functions ####
    def create_file(self):# this function creates a new file.#
        newPage = open("newpage.html", "w")#Link a variable with a newly created file with the specified name, if it does not exist already..
        self.selectedFile = "newpage.html"#SelectedFile var is equal to the new page
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
        open_new_tab("newpage.html")  #Open the new page 

    def select_file(self):#Select a file to modify, not working.
        print("select file") #Debug
        self.selectedFile = filedialog.askopenfilename(initialdir="/") #open a file dialog
       
    def modify_file(self):#Add content to an existing file, not working
        print("Modify file")
        def retrieve_input(self):
            newBodyText = self.ipt_newBody.get("1.0",END)
            newPage = open("newpage.html", "a")#Append the file created before to get rid of "Stat tuned for more details and add body."
            newPage.write("""
                <!DOCTYPE html>
                <html lang ='en'>  
                <head>     
                                <title>Stay Tuned</title>
                                <meta charset = "utf-8">
                </head>  
                <body> 
                        <p>"""
                        + newBodyText + 
                        """</p>
                </body>  
                </html>
                """)
            newPage.close()#Close the file we opened/created because were not changing it right now 
        retrieve_input(self)#Run the retrieveInput function
            
    def close(self):#Close the program
        self.master.destroy()
        
if __name__ == "__main__":  #Loop the program                
    win = Tk()#*** question 4
    App = ParentWindow(win)#***
    win.mainloop()# Loop the program
