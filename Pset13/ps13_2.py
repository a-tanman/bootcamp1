def summation(n, term):
    i = 1
    sum = 0
    while i <= n:
        sum += term(i)
        i += 1
    
    return sum

def cube(x):
    return x**3

def add(x):
    return x

def pi(x):
    return 8 / (1.0 * ((4 * x) - 3) * ((4 * x) - 1))

print(summation(1000, cube))