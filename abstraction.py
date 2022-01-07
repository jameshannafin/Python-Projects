from abc import ABC, abstractmethod

#---------------------------------------------------------------------
#School Example
#---------------------------------------------------------------------

class car(ABC):#Makes the class abstract
    def paySlip(self,amount):
        print("Your purchase amount: ", amount)
    #This function is telling us to pass in an argument, but we wont tell you how or what kind of data it will be
    @abstractmethod#Tells the PC were making an abstaract method 
    def payment(self,amount):#Abstract method 
        pass #Nothing for this method right now, just aname, no defintion

class DebitCardPayment(car):
    #HEre we've defined how to implement the payment function from uts parent payslip class
    def payment(self,amount):#Normal Method
        print('your purchase amount of {} exceeded your $100 limit '.format(amount)) #Print this message with a filled in wild card 

print("Example 1")
obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")


#---------------------------------------------------------------------
#New Example
#---------------------------------------------------------------------


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Labtop(Computer):
    def process(self):
        print("It's running")

print("Example 2")
com1 = Labtop()
com1.process()
    
        
                
