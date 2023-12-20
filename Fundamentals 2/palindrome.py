phr = input('Ingresa frase a revisar: ')  # Ten animals I slam in a net


def get_string_from_chain(strng_piece):
    strng = ''
    for ch in strng_piece:
        if ch != ' ':
            strng += ch
    return strng


string1 = get_string_from_chain(phr[:phr.index('I'):].strip())
string2 = get_string_from_chain(phr[phr.index('I')+1:].strip())

ispalindrome = True
r_idx = len(string2)
if len(string1) == len(string2):

    for i in range(len(string2)):
        r_idx -= 1
        if string2[r_idx].lower() != string1[i].lower():
            ispalindrome = False
            # print(
            #    f'Es igual el valor? {string2[r_idx].lower()} con el valor {string1[i].lower()} ?')
else:
    ispalindrome = False
print('Es un palindromo' if ispalindrome else 'No es un palindromo')
