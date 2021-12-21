class npc: #Non player characters
    hp = 100 #Health
    ap = 0 #Armour
    wpn = "none #Weapon
    team = "neutral" #Allegiance


    
#////////NEUTRALS//////////////
class farmer(npc):
    easilyFrightened = True
    
    
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
