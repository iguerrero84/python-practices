x = 11
y = 4
print('initial values: ', x, y)
x = x % y
print('first x value: ', x, y)
x = x % y
print('second x value: ', x, y)
y = y % x
print('third x value: ', x, y)
print(y)


#-----------------------------------------------

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
hora_culminacion = hour*60 + mins + dura# Escribe tu código aquí.
hora = hora_culminacion // 60
hora = hora % 24
minus = hora_culminacion % 60
print(hora, minus, sep=':')
