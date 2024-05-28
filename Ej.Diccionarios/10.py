"""Valores únicos: Escribe una función que reciba un diccionario y devuelva una lista de
valores únicos en el diccionario."""

def unicos(diccionario):
    lista = []
    for valor in diccionario.values():
        if valor not in lista:
            lista.append(valor)

    return lista

dic1 = {
    "a": 1,
    "b": 5,
    "c": 1,
    "d": 3,
    "e": 2,
    "f": 1,
    "g": 2,
    "h": 3,
    "i": 8,
    "j": 2
}

resultado = unicos(dic1)
print(resultado)


