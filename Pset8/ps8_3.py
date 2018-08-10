def is_palindrome(x):
    x = str(x)
    if len(x) < 2:
        return True
    
    if x[0] != x[-1]:
        return False
    
    return is_palindrome(x[1:-1])

assert is_palindrome(123321) == True
assert is_palindrome(123241324123521321) == False