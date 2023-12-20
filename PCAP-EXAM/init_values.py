import platform


class A:
    x = 1

    def __init__(self):
        x = 10
        self.x = 100


obj = A()
print(obj.x)
print(obj.__dict__)

print(platform.platform())
print(platform.system())
