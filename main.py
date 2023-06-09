import random
class Human:
    def __init__(self, name="Human", case=None, cave=None, dinosaur=None):
        self.name = name
        self.reputation = 100
        self.gladness = 50
        self.satiety = 50
        self.case = case
        self.dinosaur = dinosaur
        self.cave = cave

    def get_cave(self):
        self.cave = Cave()

    def get_dinosaur(self):
        self.dinosaur = Dinosaur(types_of_dinosaurs)

    def get_case(self):
        if self.dinosaur.drive():
            pass
        else:
            self.to_heal()
            return
        self.case = Case(case_list)

    def eat(self):
        if self.cave.food <=0:
            self.hunting("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.cave.food -= 5

    def work(self):
        if self.dinosaur.drive():
            pass
        else:
            if self.dinosaur.satiety < 20:
                self.hunting("dinosaur_food")
                return
            else:
                self.to_heal()
                return
        self.reputation += self.case.salary
        self.gladness -= self.case.gladness_less
        self.satiety -= 4

    def hunting(self, manage):
        if self.dinosaur.drive():
            pass
        else:
            if self.dinosaur.satiety < 20:
                manage = "dinosaur_food"
            else:
                self.to_heal()
                return

        if manage == 'dinosaur_food':
            print("I hunt for dinosaur_food")
            self.reputation -= 100
            self.dinosaur.satiety += 100
        elif manage == 'food':
            print("I hunt for food")
            self.reputation -= 50
            self.cave.food += 50
        elif manage == 'delicacies':
            print("Yay! First-class meat!")
            self.gladness += 10
            self.satiety += 2
            self.reputation -= 15
    def chill(self):
        self.gladness += 10
        self.cave.mess += 5

    def clean_cave(self):
        self.gladness -= 5
        self.cave.mess += 0

    def to_heal(self):
        self.dinosaur.health +=100
        self.reputation -= 50

    def days_indexes(self, day):
        day = f"Today {day} of {self.name}'s life"
        print(f"{day:^50}","\n")
        human_indexes = self.name + "`s indexes"
        print (f"{human_indexes:^50}","\n")
        print(f"Reputation - {self.reputation}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        human_indexes = "Human_indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Food - {self.cave.food}")
        print(f"Mess - {self.cave.mess}")
        dinosaur_indexes = f"{self.dinosaur.type} car indexes"
        print(f"{dinosaur_indexes:^50}", "\n")
        print(f"Dinosaur_satiety - {self.dinosaur.satiety}")
        print(f"Dinosaur_health - {self.dinosaur.health}")

    def is_alive(self):
        if self.gladness < 0:
            print("I tired...")
            return False
        if self.satiety < 0:
            print("Desd...")
            return False
        if self.reputation < -500:
            print("I dont have reputation...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.cave is None:
            print("Settled in the cave")
            self.get_cave()
        if self.dinosaur is None:
            self.get_dinosaur()
            print(f"I take a dinosaur{self.dinosaur.type}")
        if self.case is None:
            self.get_case()
            print(f"I dont have a case,going to get a case{self.case} with salary {self.case.salary}")
        self.days_indexes(day)
        dice = random.randint(1,4)

        if self.satiety <20:
            print("I'll go eat")
            self.eat()
        elif self.gladness <20:
            if self.cave.mess >15:
                print("I want to chill,but there is so much mess... \n So I will clean the cave")
                self.clean_cave()
            else:
                print("Let's chill")
                self.chill()
        elif self.reputation <0:
            print("I will start working")
            self.work()
        elif self.dinosaur.health <15:
            print("I need to heal my dinosaur")
            self.to_heal()
        elif dice == 1:
            print("Lets chill")
            self.chill()
        elif dice == 2:
            print("I will start working")
            self.work()
        elif dice == 3:
            print("I have Cleaning time")
            self.clean_cave()
        elif dice == 4:
            print("Time to treats!")
            self.hunting(manage='delicacies')













class Dinosaur:
    def __init__(self, type_list):
        self.type = random.choice(list(type_list))
        self.satiety = type_list[self.type]["satiety"]
        self.health = type_list[self.type]["health"]
        self.consumption = type_list[self.type]["consumption"]

    def drive(self):
        if self.health >0 and self.satiety >= self.consumption:
            self.satiety -= self.consumption
            self.health -= 1
            return True
        else:
            print("The dinosaur cannot move")
            return False

class Cave:
    def __init__(self):
        self.mess = 0
        self.food = 0

case_list = {
    "Hunter": {"salary": 50, 'gladness_less': 3},
    "Fisherman": {"salary": 40, 'gladness_less': 1},
    "Farmer": {"salary": 45, 'gladness_less': 10},
    "Miner": {"salary": 70, 'gladness_less': 25},
}
types_of_dinosaurs = {
    "Raptor": {"satiety": 50, "health": 40, "consumption": 6},
    "Direwolf": {"satiety": 70, "health": 100, "consumption": 8},
    "Tyrannosaurus rex": {"satiety": 80, "health": 120, "consumption": 10},
    "Gigantosaurus": {"satiety": 100, "health": 150, "consumption": 14},
}

class Case:
    def __init__(self, case_list):
        self.case = random.choice(list(case_list))
        self.salary = case_list[self.case]["salary"]
        self.gladness_less = case_list[self.case]["gladness_less"]


yga = Human(name="Yga")

for day in range(1, 20):
    if yga.live(day) == False:
        break
