class npc: #Non player characters
    hp = 100 #Health
    ap = 0 #Armour
    wpn = "none" #Weapon
    team = "neutral" #Allegiance


    
#////////NEUTRALS//////////////
class farmer(npc):#Child Object
    easilyFrightened = False #Is this characte easily frightened ?
    gold = 50 #How much gold do they have?
    specialGift = 'amulet' #<ore unique variables
    firstname = 'Willard'
    def inView(self): #define a function that passes information from where it was instantiated to print the complete data 
        print("I am {}, a mere farmer, will you help me?".format(firstname) # Use {} as a wildcard to fill in with the self's rewuested variable (firstname)
        

class nobleman(npc):#Child Object
    easilyFrightened = True #Is this characte easily frightened ?
    gold = 250 #How much gold do they have?
    lastname = "Pendolton"
    specialResponse = "Ah you prove yourself worthy of a heroes reward, I talk praise of you to my family at the " + lastname + " Estate.:
    def inView(self):
        print("You there! Stop galavanting and come to the great {}'s aid!".format(lastname))
    
    
#////////ENEMIES//////////////
class enemy(npc): #PARENT
    team = 'evil'

class skeleton(enemy):
    ap = 20
    wpn = "bow"

#////////FRIENLIES//////////////
class friendly(npc):#PARENT
    team = 'good'

class knight(friendly):
    ap = 50
    wpn = sword
    hasShield = True
