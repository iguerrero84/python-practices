number = input('Ingrese la cifra de su fecha de nacimiento: ')

suma_total = 0


def sum_cifra(cifra):
    suma = 0
    for n in str(cifra):
        suma += int(n)
    if len(str(suma)) > 1:
        sum_cifra(sum)
    return suma


for n in number:
    suma_total += int(n)
    if len(str(suma_total)) > 1:
        suma_total = sum_cifra(suma_total)

print(suma_total)
