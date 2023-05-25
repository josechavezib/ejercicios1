valor = float(input(" valor del producto: "))
iva = float(19)
valoriva = float(valor * iva)/100
print ("el valor del iva es:" + str(valoriva))
descuento = (valor - valoriva)
print("el valor del prodcuto con descuento es de: " + str(descuento))