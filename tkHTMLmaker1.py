
#### #### Section 1: Imports #### ####
import webbrowser
import tkinter as tk
from tkinter.filedialog import askopenfile



#### #### Section 2: Root/Main Window Creation #### ####
root = tk.Tk()#Create the canvas
canvas = tk.Canvas(root, width = 900, height = 900)#Set the size of the canvas


#### #### Section 3: Main Labels #### ####

##Label 1
lbl_newPage = tk.Label(root,text="Create a new web page")#Create a label with this text
lbl_newPage.pack(root, side = LEFT )

lbl_addBody = tk.Label(root,text="Add Content to an existing file")#Create a label with this text
lbl_addBody.pack(root, side = LEFT )

#### #### Section 4: Buttons #### ####

##Add Body Button
txt_addBody = tk.StringVar()
btn_addBody = tk.Button(root, textvariable=txt_addBody)
#btn_addBody.grid(columnspan = 3, column = 1, row = 1)
txt_addBody.set("Add Body")
btn_addBody.pack()#***

##Create New File Button ***Not showing up
btn_createFile = tk.Button(root,text="Create File")
btn_createFile.pack()
btn_createFile.pack( side = LEFT )#***

newBodyText = text(root)
newBodyText.pack(side = BOTTOM)

#### #### Section 5: Button Functions #### ####

## Open the file upon clicking.
def open_file()
    print("Opening a file...")
##This will be the button used to submit the new body text into the document
def add_body():
    file = open("newpage.txt", "a")#Open the file using"a" to append the file/ add to it
    file.write("{}".format(newBodyText))#add in the new body text. *** But how do I specidy where its added
    file.close()



#### #### Section 6: Create a new html file #### ####
def create_file():  
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


#### #### Section 7: Open The newly created file #### ####

newPage = open("newpage.txt")
print(newPage.read()) 

webbrowser.open_new_tab(newpage.txt)#Open the new file in browser.. But how do i get the URL of a newly created page



#### #### Section 9: Other #### ####
root.mainloop() #**I beleive this just keeps the code looping to allow constant interaction..
