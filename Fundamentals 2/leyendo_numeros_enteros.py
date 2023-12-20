def read_int(value, min, max):

    if not value.isdigit():
        print('Error: entrada incorrecta')
    elif not (int(value) >= min and int(value) <= max):
        print(
            f'Error: el valor no está dentro del rango permitido ({min}..{max})')


value = input("Ingresa un número entre -10 a 10: ")

v = read_int(value, -10, 10)

print("El número es:", v)
