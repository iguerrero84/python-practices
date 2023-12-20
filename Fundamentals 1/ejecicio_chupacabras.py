##
## Ejercicio del Chupacabra
##
import time

x = 0
while x==0:
    word =input('Ingrese una palabra: ')
    time.sleep(2)
    if word != 'chupacabra':
        time.sleep(2)
        continue
    else:
        break