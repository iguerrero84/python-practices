# LAB de Listas con unicos elementos

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

tmp_list = []
index = 0
for number in my_list:
    if number not in tmp_list:
        tmp_list.append(number)

my_list = tmp_list
del tmp_list


print("La lista con elementos únicos:")
print(my_list)
