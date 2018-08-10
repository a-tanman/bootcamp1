import math

class Coordinate:
    pass

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def area_of_triangle(p1, p2, p3):
    
    x1 = p1.x
    y1 = p1.y
    x2 = p2.x
    y2 = p2.y
    x3 = p3.x
    y3 = p3.y
    
    length1 = calculate_distance(x1, y1, x2, y2)
    length2 = calculate_distance(x1, y1, x3, y3)
    length3 = calculate_distance(x2, y2, x3, y3)
    s = (length1 + length2 + length3) / 2
    return round((math.sqrt(s * (s-length1)*(s-length2)*(s-length3))), 2)

print("Test  Case 1")
p1=Coordinate()
p1.x=1.5
p1.y=-3.4
p2=Coordinate()
p2.x=4.6
p2.y=5
p3=Coordinate()
p3.x=9.5
p3.y=-3.4
ans=area_of_triangle(p1, p2 ,p3)
print(ans)
print("Test  Case 2")
p1=Coordinate()
p1.x=2.0
p1.y=-3.4
p2=Coordinate()
p2.x=4.6
p2.y=5
p3=Coordinate()
p3.x=9.5
p3.y=-1.4
ans=area_of_triangle(p1, p2 ,p3)
print(ans)
print("Test  Case 3")
p1=Coordinate ()
p1.x=1.5
p1.y=3.4
p2=Coordinate()
p2.x=4.6
p2.y=5
p3=Coordinate()
p3.x=-1.5
p3.y=3.4
ans=area_of_triangle(p1 ,p2 ,p3)
print(ans)
print("Test  Case 4")
p1=Coordinate()
p1.x=-1.5
p1.y=3.4
p2=Coordinate()
p2.x=4.6
p2.y=5
p3=Coordinate()
p3.x=4.3
p3.y=-3.4
ans=area_of_triangle(p1 ,p2 ,p3)
print(ans)

p1 = Coordinate()
p2 = Coordinate()
p3 = Coordinate()
p1.x = float(input('Enter x coordinate of the first point of a triangle: '))
p1.y = float(input('Enter y coordinate of the first point of a triangle: '))
p2.x = float(input('Enter x coordinate of the second point of a triangle: '))
p2.y = float(input('Enter y coordinate of the second point of a triangle: '))
p3.x = float(input('Enter x coordinate of the third point of a triangle: '))
p3.y = float(input('Enter y coordinate of the third point of a triangle: '))

print(area_of_triangle(p1, p2, p3))