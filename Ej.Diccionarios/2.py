"""Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
nuevo que invierta las claves y los valores."""

def inverso (diccionario):
    nuevoDic = {}
    for clave, valor in diccionario.items():
        nuevoDic[valor] = clave
    return nuevoDic


nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
años = int(input("Ingrese edad: "))

dic1 = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": años
}

print(dic1)
resultado = inverso(dic1)
print(resultado)