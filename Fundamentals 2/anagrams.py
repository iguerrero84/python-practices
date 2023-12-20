string1 = input('Ingresa primera palabra: ').lower()
string2 = input('Ingresa segunda palabra: ').lower()

isanagram = True

if len(string1) == len(string2):

    for ch in string1:
        if ch not in string2:
            isanagram = False
            # print(
            #    f'Es igual el valor? {string2[r_idx].lower()} con el valor {string1[i].lower()} ?')
else:
    isanagram = False
print('Es un anagrama' if isanagram else 'No es un anagrama')
