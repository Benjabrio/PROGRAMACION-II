"""
Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
con la frecuencia de cada letra en la cadena.
"""

def frec(cadena):
    dic = {}
    for letra in cadena:
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1
    return dic

cadena = input("Ingrese la cadena: ")
resultado = frec(cadena)
print(resultado)

