def is_palindrome(x):
    x = str(x)
    for i in range(len(x)//2):
        if x[i] != x[len(x)-1-i]:
            return False

    return True

print ("Test case 1: 1")
ans= is_palindrome (1)
print (ans)
print ("Test case 2: 22")
ans= is_palindrome (22)
print (ans)
print ("Test case 3: 12321 ")
ans= is_palindrome (12321)
print (ans)
print ("Test case 4: 441232144 ")
ans= is_palindrome (441232144)
print (ans)
print ("Test case 5: 441231144 ")
ans= is_palindrome (441231144)
print (ans)
print ("Test case 6: 144")
ans= is_palindrome (144)
print (ans)
print ("Test case 7: 12")
ans= is_palindrome (12)
print (ans)