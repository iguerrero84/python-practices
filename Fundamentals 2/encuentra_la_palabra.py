seed_letter = input('Ingrese la palabra a buscar: ')
palabra = input('Ingrese la palabra o frase a evaluar: ')

validation_flag = True
idx = 0

for ch in seed_letter:
    try:
        idx = palabra.index(ch)
    except:
        validation_flag = False
        break

print('Si' if validation_flag else 'No')
