#Python: 3.5.1
#
#Author: James Hannafin
#
#Purpose: Phonebook demo that demonstrates OOP, tkinter gui modulem and
#           parent child relationships.
#
#
#

from tkinter import*
import tkinter as tk

#be sure to import our other modules so we have acces to them

import phonebook_gui
import phonebook_func

#Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def _init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #Define our maste frame configuration
        self.master = master
        self.master.minsize(500,300)#(Height, Width)
        self.master.maxsize(500,300)
        #The following centerwindow method will center our app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg+"#F0F0F0")
        #This protocal method is a tkinter built in method to catch if the user clicks the upper corner exit button on windows
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the gui widgets from a seperate module keepping your code compartmentalizded
        phonebook_gui.load_gui(self)

        if __name__ == "__main__":
            root = tk.TK()
            App = ParentWindow(root)
            root.mainloop()
                        
    
