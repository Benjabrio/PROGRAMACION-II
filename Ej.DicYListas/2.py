"""Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
un diccionario donde las claves son las longitudes de las palabras y los valores son
listas de palabras con esa longitud."""

def long(lista):
    dic = {}
    for palabra in lista:  
        cantidad = len(palabra)
        if cantidad in dic:      
            dic[cantidad].append(palabra) 
        else: 
            dic[cantidad] = [palabra]
    return dic



lista1 = ["perejil", "aceitunas", "queso", "manteca", "casa", "robot", "tucanes"]
resultado = long(lista1)
print(resultado)