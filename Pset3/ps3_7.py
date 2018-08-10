def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    
    return True

print ("is_prime (2)")
ans= is_prime (2)
print (ans)
print ("is_prime (3)")
ans= is_prime (3)
print (ans)
print ("is_prime (7)")
ans= is_prime (7)
print (ans)
print ("is_prime (9)")
ans= is_prime (9)
print (ans)
print ("is_prime (21) ")
ans= is_prime (21)
print (ans)