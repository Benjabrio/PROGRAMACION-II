"""Contar palabras en frases: Escribe una función que reciba una lista de frases y
devuelva un diccionario donde las claves son las palabras y los valores son las
frecuencias de esas palabras en todas las frases"""

def contar(lista):
    dic = {}
    for frases in lista:
        palabras = frases.split()
        for palabra in palabras:
            if palabra in dic:
                dic[palabra] += 1
            else:
                dic[palabra] = 1
    return dic

lista1 = ["no todo lo que brilla es oro", "si puedes soñarlo, puedes hacerlo", "lo que no te mata, te hace mas fuerte", "no dejes para mañana lo que puedes hacer hoy"]
resultado = contar(lista1)
print(resultado)