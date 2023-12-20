class A:
    pass


class B:
    pass


class C(B):
    pass


class D(C):
    pass


c = C()

print(isinstance(c, A))
print(isinstance(c, D))
print(isinstance(c, (B, D)))
