def outer(x):
    a = x - 1

    def inner(y):
        print(y, a)
        return y ** a

    return inner


var = outer(1)

print(var(2))
