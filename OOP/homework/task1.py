class animal:
    def __init__(self, s):
        self.state = s
        self.size = 0

    def feed(self):
        self.size += 1
        print(self.state + ' fed')

    def getState(self):
        return self.state

    def getSize(self):
        return self.size


class fish(animal):
    def __init__(self, s, m):
        self.maxSize = m
        super().__init__(s)

    def setMaxSize(self, m):
        self.maxSize = m

    def feed(self):
        self.size += 2
        print(self.state + ' fed')
        if self.size >= self.maxSize:
            self.state = 'big fish'


class duck(animal):
    def feed(self):
        if self.size == 5:
            self.state = 'big duck'

thisFish = fish('little fish', 3)
thisFish.setMaxSize(3)
thisDuck = duck('little duck')
for x in range (1,3):
    thisDuck.feed()
    print(thisDuck.getState())
    thisFish.feed()
    print(thisFish.getState())
