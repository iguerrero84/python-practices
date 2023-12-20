'''
vowels=['a','A','e','E','i','I','o','O','u','U']
resp = ''

for letter in user_word:
    if letter in vowels:
        continue
    else:
        resp += letter
'''

# print('Fundamentos', 'Programacion', 'en', sep='***')
# print('end','Python', sep='...')
# print(type(21.9))

##
# Ejercicio del Chupacabra
##
import time

x = 0
while x == 0:
    word = input('Ingrese una palabra: ')
    time.sleep(10)
    if word != 'chupacabra':
        time.sleep(5)
        continue
    else:
        x = 1

###
# EL FEO DEVORADOR DE VOCALES
##
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consons = []
user_word = input('Ingrese la palabra: ')
# Completa el cuerpo del bucle for.
for letter in user_word:
    if letter in vowels:
        continue
    else:
        consons.append(letter.upper())

for letter in consons:
    print(letter, end="\n")

###
# EL BONITO DEVORADOR DE VOCALES
##
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consons = []
user_word = input('Ingrese la palabra: ')
# Completa el cuerpo del bucle for.
for letter in user_word:
    if letter in vowels:
        continue
    else:
        consons.append(letter.upper())

for letter in consons:
    print(letter, end="")


# QUIZ DEL MODULO

# Question 1
for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# Question 2
i = 1
while i < 10:
    if i % 2 != 0:
        print(i)
    i += 1

# Question 3
for ch in "john.smith@pythoninstitute.org":

    if ch == "@":
        break
    print(ch, end='')

# Question 4
for digit in "0165031806510":
    if digit == "0":
        print('X', end='')
        continue
    print(digit, end='')
