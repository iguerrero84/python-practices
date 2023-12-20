
# paso 1
beatles=[]
print("Paso 1:", beatles)

# paso 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Paso 2:", beatles)

# paso 3
members=['Stu Sutcliffe',' Pete Best']
for m in members:
    beatles.append(m)
print("Paso 3:", beatles)

# paso 4
for m in members:
  for b in beatles:
      if m == b:
         idx = beatles.index(b) 
         del beatles[idx]
print("Paso 4:", beatles)
# paso 5
beatles.insert(0,'Ringo Starr')
print("Paso 5:", beatles)

# probando la longitud de la lista
print("Los Fav", len(beatles))

