"""Diccionario de cuadrados: Escribe una función que reciba un número n y devuelva un
diccionario con los números de 1 a n como claves y sus cuadrados como valores."""

def cuadrado(num):
    dic = {}
    for numero in range(1,num + 1):
        dic[numero] = numero * numero
    return dic

nro = int(input("Ingrese un numero del 1 al 10: "))
resultado = cuadrado(nro)
print(resultado)