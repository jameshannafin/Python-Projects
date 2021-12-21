
class Organism:#Parent Class
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = "Sequence A"
    origin = 'Unknown'
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs:{}\nArms: {}\nDNA: {}\nOrigin: {} \nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# child class instance
class Human(Organism):
    name = 'Michael'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = '\nCreates a deadly weapon using a paper clip'
        return msg

#another child class instance
class Dog(Organism):
    name = 'spot'
    species = 'canine'
    legs = 4
    arms = 0
    dna = "Seqience B"

    def bite(self):
        msg = "\nEmits a growl and bits its target"
        return msg
#child
class Bacteria(Organism):
    name = 'X'
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = 'Mars'

    def replication(self):
        msg = "\nCellds multiply and divide"
        return msg
    


if __name__ == '__main__':
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacteria()
    print(bacteria.information())
    print(bacteria.replication())





    
