x = 9
y = 2
cadena = ""
while x >=1:
    print( x, "/", y, " = ", x%y )
    cadena = str(x%y) + cadena
    x = x // y
print(cadena)