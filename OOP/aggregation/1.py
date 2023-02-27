from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        print("h")

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides ")

class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")

class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")

class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have 4 sides")

jesus = Polygon()
jesus.noofsides()

R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()