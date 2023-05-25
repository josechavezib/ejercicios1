numero = int(input("ingrese el numero: "))
binario = ""
while numero > 0:
    if numero % 2 == 0:
        binario = "0" + str(binario)
    else:
        binario = "1" + str(binario) 
    numero = numero // 2 

print(binario)