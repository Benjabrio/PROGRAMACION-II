"""Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y
devuelva la suma de todos los valores."""

def suma(diccionario):
    sumatoria = 0
    for valor in diccionario.values():
        sumatoria += valor
    return sumatoria
    


dic1 = {
    "clave1": 6,
    "clave2": 16, 
    "clave3": 13,
    "clave4": 8,
    "clave5": 5,
}
resultado = suma(dic1)
print("La suma de estas claves es:", resultado)