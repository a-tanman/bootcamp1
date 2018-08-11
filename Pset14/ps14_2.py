def logit(f):
    def output(*args):
        print(f)
        for arg in args:
            print(arg)
        return f(*args)
    return output

@logit
def test(*args):
    pass

test(5, 1, 4)