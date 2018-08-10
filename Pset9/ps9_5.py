class Deque:

    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)
        
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
for x in range(10):
    d1.append_left(x)


print(d1.items)

assert d1.pop() == 0
assert d1.pop_left() == 9
print(len(d1))
