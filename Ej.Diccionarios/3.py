"""
Merge de diccionarios: Crea una función que tome dos diccionarios y devuelva uno
nuevo que combine ambos (en caso de conflicto, usa los valores del segundo
diccionario).
"""
def combinar(dic1, dic2):
    for clave in dic2:
        if clave in dic1:
            dic1[clave].update(dic2[clave])
        else:
            dic1[clave] = dic2[clave]
    return dic1
    

dic1 = {
    "Benjamin": {"Edad": 23, "país": "Argentina"},
    "George": {"Edad": 18, "país": "Inglaterra"},
    "John": {"Edad": 30, "país": "Canada"}
}
dic2 = {
    "Benjamin": {"profesión": "Estudiante"},
    "George": {"profesión": "Carpintero"},
    "John": {"profesión": "Ingeniero"}
}
resultado = combinar(dic1, dic2)
print(resultado)