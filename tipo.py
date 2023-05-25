def determinar_tipo_dato(dato):
    if isinstance(dato, str):
        return "Texto"
    elif isinstance(dato, int):
        return "Entero"
    elif isinstance(dato, float):
        return "Float"
    else:
        return "Tipo de dato desconocido"

dato_usuario = input("Ingresa un dato: ")

try:
    dato_convertido = eval(dato_usuario)
    tipo_dato = determinar_tipo_dato(dato_convertido)
    print("El tipo de dato ingresado es:", tipo_dato)
except:
    print("No se pudo determinar el tipo de dato ingresado")