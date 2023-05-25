base = int(input("ingrese la base: "))
exponente = int(input("ingrese el exponente: "))
if exponente <= 0:
    print("no ingresa un numero entero")
else:
    resultado = base ** exponente
print ("el resultado es: " + str(resultado))
