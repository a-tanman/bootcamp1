import random

class Queue:

    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.append(item)
    
    def get(self):
        item = self.items[0]
        del self.items[0]
        return item

    def is_empty(self):
        return len(self.items) == 0

    def qsize(self):
        return len(self.items)



q1 = Queue()
for x in range(random.randint(1,10)):
    q1.put(x)
print(q1.get())
print(q1.qsize())