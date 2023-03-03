"""the homework for task 3"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """an abstract class for animals"""

    @abstractmethod
    def move(self):
        """an abstract method for moving"""
        print("This animal walks")

    @abstractmethod
    def eat(self):
        """an abstract method for eating"""
        print("This animal can eat")

    @abstractmethod
    def birth(self):
        """an abstract method for birth"""
        print("This animal is born")

    @abstractmethod
    def hibernate(self):
        """an abstract method for hibernation"""
        print("This animal hibernates")

    @abstractmethod
    def get_info(self):
        """an abstract method for getting the class info"""
        if self._cold_blooded:
            print("This animal is cold-blooded")
        else:
            print("This animal is warm-blooded")

        if self._skin_type is not None:
            print("This animal is covered in " + self._skin_type)
        if self._tail:
            print("This animal has a tail")
        if self._legs > 0:
            print("This animal has " + str(self._legs) + " legs")
        if self._arms > 0:
            print("This animal has " + str(self._arms) + " arms")
        if self._wings > 0:
            print("This animal has " + str(self._wings) + " wings")

        self.move()
        self.eat()
        self.birth()

#---------------- reptiles -------------------------

class Reptile(Animal):
    """an child class of Animal for reptiles """
    def __init__(self):
        self._cold_blooded = True
        self._skin_type = "scales"
        self._tail = True

    def birth(self):
        print("this animal lays eggs")

    def move(self):
        print("this animal walks")

    def hibernate(self):
        print("this animal hibernates")

    def get_info(self):
        super().get_info()
        self.hibernate()
        print()

class Tortoise(Reptile):
    "a tortoise"
    def __init__(self):
        super().__init__()
        self._legs = 4
        self._arms = 0
        self._wings = 0

    def eat(self):
        print("This animal is a herbivore")

    def get_info(self):
        print("Tortoise: ")
        super().get_info()

class Turtle(Reptile):
    """a turtle"""
    def __init__(self):
        super().__init__()
        self._legs = 4
        self._arms = 0
        self._wings = 0

    def eat(self):
        print("This animal is a herbivore")

    def get_info(self):
        print("Turtle: ")
        super().get_info()

class Snake(Reptile):
    "a snake"
    def __init__(self):
        super().__init__()
        self._legs = 0
        self._arms = 0
        self._wings = 0

    def move(self):
        print("This animal slithers")

    def eat(self):
        print("This animial is a carnivore")

    def get_info(self):
        print("Snake: ")
        super().get_info()

# ------------------------- mammels ------------------------
class Mammal(Animal):
    "an child class of animal that objectifies mammals"
    def __init__(self):
        self._cold_blooded = False
        self._skin_type = "fur"

    def birth(self):
        print("this animal gives birth to live young")

    def move(self):
        print("This animal walks")

    def eat(self):
        print("This animal is an omnivore")

    def hibernate(self):
        print("This animal hibernates")

class Otter(Mammal):
    """an otter"""
    def __init__(self):
        super().__init__()
        self._tail = True
        self._legs = 4
        self._arms = 0
        self._wings = 0

    def move(self):
        print("This animal walks and swims")

    def get_info(self):
        print("Otter: ")
        super().get_info()
        print()

class Gorilla(Mammal):
    """a gorilla"""
    def __init__(self):
        super().__init__()
        self._tail =False
        self._legs = 2
        self._arms = 2
        self._wings = 0

    def move(self):
        print("This animal walks and climbs")

    def eat(self):
        print("This animal is a herbivore")

    def get_info(self):
        print("Gorilla: ")
        super().get_info()
        print()

class Bat(Mammal):
    "a bat"
    def __init__(self):
        super().__init__()
        self._tail = True
        self._legs = 2
        self._arms = 0
        self._wings = 2

    def move(self):
        print("This animal flies")

    def get_info(self):
        print("Bat: ")
        super().get_info()
        self.hibernate()
        print()

# ------------------ the main functions

def main():
    """the main function of the program"""
    tortoise = Tortoise()
    turtle = Turtle()
    snake = Snake()
    otter = Otter()
    gorilla = Gorilla()
    bat = Bat()

    tortoise.get_info()
    turtle.get_info()
    snake.get_info()
    otter.get_info()
    gorilla.get_info()
    bat.get_info()

if __name__ == "__main__":
    main()
