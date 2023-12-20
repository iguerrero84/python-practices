list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

# COMPACTO Y ELEGANTE
list_3 = [1 if x % 2 == 0 else 0 for x in range(10)]


print(list_1)
print(list_2)
print(list_3)
