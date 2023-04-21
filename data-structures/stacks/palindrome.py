class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
string = list(input("enter a pallindrome: "))
stack = Stack()
for letter in string:
    stack.push(letter)

list2 = []
while stack.size() != 0:
    list2.append(stack.pop())

if string == list2:
    print("palindrome")
else:
    print("funny")