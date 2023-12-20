class MyClass:
    def __init__(self, numero, texto):
        self.__numero = numero
        self.__texto = texto

    def __str__(self):
        return self.__texto


my_object = MyClass(10, "Este es mi objeto cuyo numero es:")

my_object.__numero = 100

print(my_object, my_object._MyClass__numero)

print(my_object, my_object.__numero)

print(my_object.__dir__())
