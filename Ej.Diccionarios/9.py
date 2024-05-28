"""Actualizar diccionario: Escribe una función que tome un diccionario y una lista de
tuplas (clave, valor) y actualice el diccionario con esas tuplas."""

def actualizar(diccionario, tupla):
    for clave, valor in tupla:
        diccionario[clave] = valor
    return diccionario

dic1 = {
    "nombre": "benjamin", "apellido": "briolini"
}
tupla = [("edad", 23), ("pais", "Argentina")]
resultado = actualizar(dic1, tupla)
print(resultado)