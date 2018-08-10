import random

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


s1 = Stack()
for x in range(10):
    s1.push(x)

assert s1.pop() == 9
assert s1.top() == 8
assert s1.is_empty() == False