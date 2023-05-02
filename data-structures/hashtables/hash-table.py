class HashTable:
    def __init__(self):
        self.keys = [None for _ in range(10)]
        self.values = [None for _ in range(10)]

    def hash(self, value):
        return value % 10
    
    def append(self, key, value):
        hashed_key = self.hash(key)

        if len(self.keys) <= 10:
            self.keys.append(hashed_key)
        else: 
            print("Too many values in hash table")
            return

        self.values.append(value)

    def get(self, key):
        self.kets.index(self.hash)

table = HashTable()
table.append(402, 1)
