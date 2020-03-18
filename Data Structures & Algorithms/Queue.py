
class Queue:
    def __init__(self):
        self.items = []

    def enque(self,items):
        return self.items.insert(0,items)

    def deque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items==[]

    def show_queue(self):
        return self.items

q = Queue()
q.enque('A')
q.enque('F')
q.enque('H')
print(q.show_queue())
q.deque()
print(q.show_queue())