def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance = 1e-15):
    return abs(x - y) < tolerance

def newton_update(f, df):

    return lambda x: x - f(x) / df(x)

def find_zero(f, df):
    
    return improve(newton_update(f, df), lambda x: approx_eq(f(x), 0))

def square_root_newton(a):

    return find_zero(lambda x: x*x-a, lambda x: 2*x)

print(square_root_newton(64))