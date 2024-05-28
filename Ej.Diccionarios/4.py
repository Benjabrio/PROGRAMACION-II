"""Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves,
y devuelva un nuevo diccionario solo con las claves especificadas."""

dic1 = {
    "nombre": "benjamin",
    "apellido": "briolini",
    "edad": 23,
    "pais":"Argentina"
}

def filtro(diccionario, claves):
    dic = {}
    for clave in claves:
        if clave in diccionario:
            dic[clave] = diccionario[clave]
    return dic

claves = ["nombre", "apellido"]

resultado = filtro(dic1,claves)
print(resultado)


