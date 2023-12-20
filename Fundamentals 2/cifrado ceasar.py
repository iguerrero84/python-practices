# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if char.isspace() or char.isdigit():
        cipher += char
    else:
        if char != 'y' and char != 'z':
            code = ord(char) + 2
        elif char == 'y':
            cipher += 'a'
            continue
        elif char == 'z':
            cipher += 'b'
            continue

        cipher += chr(code)


print(cipher)
