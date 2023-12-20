def fun(x, y, z):
    return x(y) * x(z) - z + y


print(fun(lambda x: x**2, 3, 2))
