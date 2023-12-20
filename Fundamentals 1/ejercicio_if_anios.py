anio = int(input('Ingrese el año: '))

respuesta = ''

if anio % 4 > 0:
    respuesta = 'Año comun'

if anio % 100 == 0:
    respuesta = 'Año bisiesto'

if anio % 400 == 0:
    respuesta = 'Año comun'

print(respuesta)
