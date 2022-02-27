

class Protected:
    def __init__(self):
        self._protectedVar = 15 #Set a protected Variable
        self.__privateVar = 8 #Set a Private variable

    def getPrivate(self):
        print(self.__privateVar) #Print the private var 

    def setPrivate(self, private):
        self.__privateVar = private #Function th change the private var

obj = Protected() # this var is eqaul to the assigned class
obj.getPrivate() # print the privateVar
obj.setPrivate(23) # change the privateVar
obj.getPrivate() # repring the privateVar
obj.getProtected() #get the protected var
