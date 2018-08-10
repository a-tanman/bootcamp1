from collections import defaultdict, Counter

def coin_change(x):

    d = Counter()
    if x in [10, 20, 50, 100]:
        d[x] += 1
        return(d)
    else:
        for every_coin in [100, 50, 20, 10]:
            while x >= every_coin:
                d[every_coin] += 1
                x = x - every_coin
                coin_change(x)
        return(d)


assert coin_change (50) == {50:1}
assert coin_change (80) == {50:1 , 20:1 , 10:1}
assert coin_change (120) == {100:1 , 20:1}
assert coin_change (90) == {50:1 , 20:2}