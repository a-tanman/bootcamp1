def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    return 1 + 1.0/guess

def square_close_to(guess):
    lhs = guess**2
    rhs = guess + 1
    return approx_eq(lhs, rhs)


def approx_eq(x, y, tolerance = 1e-25):
    return abs(x - y) < tolerance

def calculate_phi(tolerance):
      
    def golden_update(guess):
        return 1 + 1.0/guess

    def square_close_to(guess):
        lhs = guess**2
        rhs = guess + 1
        return approx_eq(lhs, rhs, tolerance)

    return improve(golden_update, square_close_to)


print(calculate_phi(1e-15))