import math
class Coordinate:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

p = Coordinate()
print(p.x, p.y)

print(p.magnitude())

p.x = 3
p.y = 4
print(p.magnitude())

q = Coordinate(3,4)
print(p == q)

q.translate(1,2)
print(q.x)

print(p == q)



        
