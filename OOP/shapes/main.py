from math import sqrt

class Triange:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height * 0.5

    def get_perimeter(self):
        hypotenuse = self.width**2 + self.height**2
        hypotenuse = sqrt(hypotenuse)
        return self.width + self.height + hypotenuse

class Square:
    def __init__(self, size):
        self.size = size

    def get_area(self):
        return self.size**2

    def get_perimeter(self):
        return self.size*4


triange = Triange(5, 10)
square = Square(7)

print(triange.get_area())
print(triange.get_perimeter())
print(square.get_area())
print(square.get_perimeter())
