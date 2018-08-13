class myproperty:

    def __init__(self, f_get, f_set):
        self.fget = f_get
        self.fset = f_set
    
    def __get__(self, obj, objType = None):
        print('getting...')
        return self.fget(obj)

    def __set__(self, obj, value):
        print('setting...')
        self.fset(obj, value)

class Fraction:

    def __init__(self, numerator = 0, denominator = 1):
        self._numerator = numerator
        self._denominator = denominator
        self.reduce()

    def gcd(self, a, b):
    
        while b:
            a, b = b, a%b
        return a

    def reduce(self):
        greatest_common_divisor = self.gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // greatest_common_divisor
        self._denominator = self._denominator // greatest_common_divisor
        
    def __add__(self, other):
        new_fraction = Fraction(self._numerator * other._denominator + other._numerator * self._denominator, 
        self._denominator * other._denominator)
        return new_fraction

    def __str__(self):
        return '{}/{}'.format(int(self._numerator),int(self._denominator))

    # @property
    # def numerator(self):
    #     return self._numerator

    # @numerator.setter
    # def numerator(self, value):
    #     self._numerator = value

    # this is equivalent to
    def get_numerator(self):
        return self._numerator

    def set_numerator(self, value):
        self._numerator = value
    
    def get_denominator(self):
        return self._denominator

    def set_denominator(self, value):
        self._denominator = value

    numerator = myproperty(get_numerator, set_numerator)
    denominator = myproperty(get_denominator, set_denominator)
    # @property
    # def denominator(self):
    #     return self._denominator

    # @denominator.setter
    # def denominator(self, value):
    #     self._denominator = value

f1 = Fraction(1, 4)
print(f1)

f2 = Fraction(1, 2)
print(f2)

print(f1 + f2)

print(f1.numerator)
print(f1.denominator)

f1.numerator = 2
f1.numerator
f1.numerator = 3
f1.denominator
f1.denominator = 2
f1.denominator
print(f1)