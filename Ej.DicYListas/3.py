"""
Diccionario de listas: Escribe una función que tome un diccionario donde los valores
son listas y devuelva una lista que contenga todos los elementos de las listas del
diccionario.
"""

def union(diccionario):
    lista = []
    """for clave, valor in diccionario.items():
        lista.append(valor)"""
    for valores in diccionario.values():
        for palabra in valores:
            lista.append(palabra)       
    return lista

dic1 = {
    "nombres": ["Benjamin", "Jose", "Gabriel", "Gustavo"],
    "apellido": ["Briolini", "Lopez", "Gonzales", "Morales"],
    "edades": [23, 18, 25, 28]
}
resultado = union(dic1)
print(resultado)