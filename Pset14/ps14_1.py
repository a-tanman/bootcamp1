def add_powers(n):
    
    def raise_pow(x, power = n):
        sum = 0
        for i in x:
            sum += i**n
        
        return sum

    return raise_pow

series1 = [0, 1, 2, 3, 4, 5]
series2 = [2, 4, 8, 16, 32]

power_reducer = add_powers(2)

power_reducer(series1)

power_reducer = add_powers(3)

power_reducer(series1)

power_reducer(series2)