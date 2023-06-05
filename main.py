class Animal:
    def __init__(self, name="Animal"):
        self.name = name


class Ownercharter:
    def __init__(self, charecter_of_the_owner ):
        self.charecter_of_the_owner = charecter_of_the_owner
        self.pets = []

    def add_pet(self, animal):
        self.pets.append(animal)

    def print_pets_name(self):
        if self.pets != []:
            print(F"Charter of owner for first two pets is {self.charecter_of_the_owner} : ")
            for pet in self.pets:
                print(pet.name)
        else:
            print(F"There are no good charter in {self.charecter_of_the_owner}")

snow = Animal("Snow is cat")
amanda = Animal("Amanda is dog")

car = Ownercharter("Good")

car.add_pet(snow)
car.add_pet(amanda)
car.print_pets_name()

class Animal:
    def __init__(self, name="Animal"):
        self.name = name


class Ownercharter:
    def __init__(self, charecter_of_the_owner ):
        self.charecter_of_the_owner = charecter_of_the_owner
        self.pets = []

    def add_pet(self, animal):
        self.pets.append(animal)

    def print_pets_name(self):
        if self.pets != []:
            print(F"Charter of owner for second two pets is {self.charecter_of_the_owner} : ")
            for pet in self.pets:
                print(pet.name)
        else:
            print(F"There are no good charter in {self.charecter_of_the_owner}")

rosa = Animal("Rosa is pig")
cola = Animal("Cola is goat")

car = Ownercharter("Bad")

car.add_pet(rosa)
car.add_pet(cola)
car.print_pets_name()

class Animal:
    def __init__(self, name="Animal"):
        self.name = name


class Ownercharter:
    def __init__(self, charecter_of_the_owner ):
        self.charecter_of_the_owner = charecter_of_the_owner
        self.pets = []

    def add_pet(self, animal):
        self.pets.append(animal)

    def print_pets_name(self):
        if self.pets != []:
            print(F"Charter of owner for last two pets is {self.charecter_of_the_owner} : ")
            for pet in self.pets:
                print(pet.name)
        else:
            print(F"There are no good charter in {self.charecter_of_the_owner}")

red = Animal("Red is python")
blue = Animal("Blue is parrot")

car = Ownercharter("Exacting")

car.add_pet(red)
car.add_pet(blue)
car.print_pets_name()