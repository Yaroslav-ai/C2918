import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.reputation = 0
        self.alive = True


    def to_trevel(self):
        print('time to explore my territory')
        self.reputation += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('I need to go sleep after hard day')
        self.gladness += 3

    def to_break(self):
        print('Time to break something')
        self.gladness += 5
        self.reputation -= 0.1

    def is_alive(self):
        if self.reputation < -0.5:
            print('I have no reputation, all cats disrespect me')
            self.alive = False
        elif self.gladness <= 0:
            print('Hello depresion, I am tired')
        elif self.reputation > 5:
            print('I am boried, no one fight me')
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Reputation = {round(self.reputation, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life."
        print(f"{day :=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_trevel()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_break()
        self.end_of_day()
        self.is_alive()
snow = Cat(name="Snow")

for day in range(365):
    if snow.alive == False:
        break
    snow.live(day)
