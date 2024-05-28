"""Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
devuelva un diccionario con la frecuencia de cada palabra."""

def frecuencia(lista):
    dic = {}
    for palabra in lista:
        if palabra in dic:
            dic[palabra] += 1
        else:
            dic[palabra] = 1
    return dic



lista1 = ["cafe", "doctor", "salamin", "cafe"]
resultado = frecuencia(lista1)
print(resultado)