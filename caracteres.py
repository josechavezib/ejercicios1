nombre = input("ingresa tu nombre completo:")
print (nombre)

contador = 0

for i in nombre:
    if (i.isalpha()):
        contador += 1
print("tu nombre tiene " + str(contador) + " caracteres")