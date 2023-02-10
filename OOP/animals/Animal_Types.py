from Animal import Animal

class Mouse(Animal):
    def get_animal_type(self):
        print("This is a mouse")

    def chew(self, amount):
        self.happiness += amount
        if self.happiness > 10:
            self.happiness = 10

class Dog(Animal):
    def __init__(self, name, breed, gender, owner):
        self.owner = owner
        super().__init__(name, breed, gender)

    def get_animal_type(self):
        print("This is a dog")

    def dig(self, time):
        self.happiness += time
        if self.happiness > 10:
            self.happiness = 10

class Cat(Animal):
    def get_animal_type(self):
        print("This is a cat")
