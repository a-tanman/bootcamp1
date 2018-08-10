
class Fraction:

    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def gcd(self, a, b):
    
        while b:
            a, b = b, a%b
        return a

    def reduce(self):
        greatest_common_divisor = self.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // greatest_common_divisor
        self.denominator = self.denominator // greatest_common_divisor
        
    def __add__(self, other):
        new_fraction = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, 
        self.denominator * other.denominator)
        return new_fraction

    def __str__(self):
        return '{}/{}'.format(int(self.numerator),int(self.denominator))

f1 = Fraction(1, 4)
print(f1)

f2 = Fraction(1, 2)
print(f2)

print(f1 + f2)