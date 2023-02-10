class Animal(object):
    def __init__(self, name, breed, gender):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.hunger = 0
        self.energy = 10
        self.happiness = 10

    def get_animal_type(self):
        print("This is an animal")

    def eat(self, amount_of_food):
        self.hunger -= amount_of_food
        if self.hunger < 0:
            self.hunger = 0

    def sleep(self, time):
        self.energy += time
        if self.energy > 10:
            self.energy = 10

    def play(self, time):
        self.happiness += time
        if self.happiness > 10:
            self.happiness = 10
