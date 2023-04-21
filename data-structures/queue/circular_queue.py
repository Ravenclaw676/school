class CircularQueue(object):
    def __init__(self, size) -> None:
        self.queue = [None]*size
        self.front = 0
        self.rear = -1
        self.size = 0
        self.max_size = size

    def is_empty(self) -> bool:
        return self.size == 0
    
    def is_full(self) -> bool:
        return self.size == self.max_size
    
    def enqueue(self, item):
        if self.is_full():
            print("the queue is full")
        elif self.rear == -1:
            self.queue[1] = item
            self.rear += 1
            self.size -= 1
        else:
            self.queue[self.rear] = item
            self.rear += 1
            self.size -= 1

    def dequeue(self):
        if self.is_empty():
            print("the queue is already empty")
        else:
            self.queue[self.front] = None
            self.front += 1
            self.size -= 1

queue = CircularQueue(5)
queue.enqueue(5)
queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(1)
queue.dequeue()
queue.enqueue(6)
print(queue.queue)

