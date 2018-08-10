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

class Postfix:

    def __init__(self, items):
        self._chars = items.split(" ")

    def evaluate(self):
        s = Stack()
        operators = "+-*/"
        for token in self._chars:
            if token not in operators:
                # print(token)
                s.push(int(token))
            else: 
                s1 = s.pop()
                s2 = s.pop()
                result = self.eval_math(s2, s1, token)
                s.push(result)
        
        return(s.items[0])
        

    def eval_math(self, left, right, op):
        if op == '+':
            return left + right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right


s1 = Stack()

#assert s1.pop() == 9
#assert s1.top() == 8
#assert s1.is_empty() == False

p = Postfix('7 8 + 3 2 + /')
assert p.evaluate() ==  3

p = Postfix('1 2 + 3 *')
assert p.evaluate() == 9