from typing import Optional

class Node:
    def __init__(self, data: int, next: Optional['node']=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self, data: Optional[int]=None):
        if data:
            self.head = Node(data)
        else:
            self.head = None
    
    def __str__(self):
        output = ""
        curr = self.head
        while curr:
            output += f"{curr.data} -> "
            curr = curr.next
        return output + "None"

    def append(self, data: int):
        if self.head is None:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next 
        curr.next = Node(data)

    def prepend(self, data:int):
        self.head = Node(data, self.head)
    
    def insert_after_node(self, prev_node: Node, data: int):
        next = prev_node.next
        prev_node.next = Node(data, next)
    
    def delete(self, data:int):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next
    
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
print(linked_list)