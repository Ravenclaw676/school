def hash(string: str, length: int) -> int:
    total = 0
    for char in string:
        total += ord(char)

    total = total % length
    return total

class hash_table(object):
    def __init__(self, length: int):
        self.length = length
        self.table = [None]*length
    
    def add_to_table(self, string: str):
        hashed = hash(string, self.length)
        if self.table[hashed] == None or -1:
            self.table[hashed] = string
        else:
            i = 1
            while self.table[hashed + i] != None or -1:
                i += 1
            self.table[hashed + i] = string

    def search_table(self, string: str) -> bool:
        hashed = hash(string, self.length)
        if self.table[hashed] == string:
            return True
        elif self.table[hashed] == -1:
            i = 1
            while self.table[hashed + i] != -1:
                i += 1


string = input("enter a string: ")

