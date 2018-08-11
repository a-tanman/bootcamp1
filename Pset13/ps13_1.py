def sum_naturals(n):
    i = 0
    sum = 0
    while i <= n:
        sum += i
        i += 1

    return sum

def sum_cubes(n):
    i = 0
    sum = 0
    while i <= n:
        sum += i**3
        i += 1

    return sum

def pi_sum(n):
    i = 1
    pi = 0.0
    while i <= n:
        pi += 8 / (1.0 * ((4 * i) - 3) * ((4 * i) - 1))
        i += 1
    
    return pi

print(sum_naturals(10))
print(sum_cubes(10))
print(pi_sum(10000))




