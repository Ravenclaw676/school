class Triange:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height * 0.5

class Square:
    def __init__(self, size):
        self.size = size

    def get_area(self):
        return self.size**2


triange = Triange(5, 10)
square = Square(7)

print(triange.get_area())
print(square.get_area())
