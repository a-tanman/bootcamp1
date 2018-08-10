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

class MixedFraction(Fraction):

    def __init__(self, *args):
        if len(args) == 2:
            self.whole_num = 0
            Fraction.__init__(self, args[0], args[1])
        elif len(args) == 3:
            self.whole_num = args[0]
            Fraction.__init__(self, args[1], args[2])
        
        self.get_three_numbers()
        
    def get_three_numbers(self):
        if self.numerator > self.denominator:
            self.whole_num += self.numerator // self.denominator
            self.numerator = self.numerator % self.denominator
        
                  
        
        # return self.whole_num, self.numerator, self.denominator

    def __str__(self):
        if self.numerator == 0:
            return '{}'.format(self.whole_num)
        elif self.whole_num > 0:
            return '{} {}/{}'.format(self.whole_num, self.numerator, self.denominator)
        else:
            return Fraction.__str__(self)

mf = MixedFraction(4,2)
print(mf)