"""Intercambiar valores: Crea una función que tome un diccionario y dos claves, e
intercambie los valores de esas dos claves en el diccionario."""



def cambio(diccionario, clave1, clave2):
    if clave1 in diccionario and clave2 in diccionario:
        valor1 = diccionario[clave1]
        valor2 = diccionario[clave2]
        diccionario[clave1] = valor2
        diccionario[clave2] = valor1
    return diccionario
        
dic1 = {
    "nombre": "benjamin",
    "apellido": "briolini",
    "edad": 23,
    "pais":"Argentina"
}

clave1 = "nombre"
clave2 = "apellido"
resultado = cambio(dic1, clave1, clave2)
print(resultado)
        