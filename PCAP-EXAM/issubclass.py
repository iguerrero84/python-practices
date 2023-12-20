class A:
    pass


class B:
    pass


class C(A):
    pass


class D(C):
    pass


print(issubclass(D, C), end=" ")
print(issubclass(D, A), end=" ")
print(issubclass(A, A), end=" ")
print(issubclass(D, B), end=" ")
print(issubclass(D, (A, B)))
