import random
def mayores(lista, n):
    lista2 = []
    for i in lista:
        if i > n:
            lista2.append(i)
    return lista2

numRan = random.randint(1,20)
lista1 = []
cont = 0
while cont < 10:
    num = int(input("Ingrese 10 numeros del 1 al 20 para la lista:"))
    lista1.append(num)
    cont+= 1

print("La lista es:", lista1)
print("El numero es:", numRan)
resultado = mayores(lista1, numRan)
print("La nueva lista es:", resultado)