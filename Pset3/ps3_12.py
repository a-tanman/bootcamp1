numbers_with_3 = (x for x in range(1001) if '3' in str(x))

type(numbers_with_3)

print(numbers_with_3)

for num in numbers_with_3:
    print(num, end = ', ')

