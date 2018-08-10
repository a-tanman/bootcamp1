class Deque:

    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + item
        
    def append_left(self, item):
        new_list = []
        new_list.append(item)
        self.items = new_list + self.items
        
    def pop(self):
        return self.items.pop()

    def pop_left(self):
        p1 = self.items[0]
        self.items = self.items[1:]
        return p1

    def __len__(self):
        return len(self.items)

d1 = Deque()

d1.append([1,2,3])
d1.append([3,2,1])

print(d1)