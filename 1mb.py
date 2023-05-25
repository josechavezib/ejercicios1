mb = 1
bits = 8388608
bytes = 1048576
kb = 1024
gb = 0.000976563

unidad = int(input("ingresa una unidad. "))

a = unidad * mb
b = unidad * bits
c = unidad * bytes
d = unidad * kb
#e = unidad * gb
print(unidad, "equivale a: ")
print(a, "mb")
print(b, "bits")
print(c, "bytes")
print(d, "kb")
#print(d, "gb")