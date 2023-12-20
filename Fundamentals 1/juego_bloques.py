#
# Juego de bloques del niño con su padre programador.
#
blocks = int(input("Ingresa el número de bloques: "))

height = 0
blocks_by_level = 1
while blocks > 1:
    height += 1
    level = blocks_by_level * height
    blocks -= level
    print('| ' * level, end="\n")


print("La altura de la pirámide:", height, blocks)
