class priority_queue(object):
    def __init__(self, size: int) -> None:
        self.main_queue = []*size
        self.priority_queue = []*size
    
    def is_priority_queue_empty(self) -> bool:
        return len(self.priority_queue) == 0
    
    def is_main_queue_empty(self):
        return len(self.main_queue) == 0

    def add_data_to_main_queue(self, data) -> None:
        self.main_queue.append(data)
    
    def add_data_to_priority_queue(self, data) -> None:
        self.priority_queue.append(data)

    def remove_from_queue(self):
        if not self.is_priority_queue_empty():
            data = self.priority_queue[0]
            del self.priority_queue[0]
            return data
        elif not self.is_main_queue_empty():
            data = self.main_queue[0]
            del self.main_queue[0]
            return data
