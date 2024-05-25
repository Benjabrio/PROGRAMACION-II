import random
def contar(lista,n):
    contador = 0
    for i in lista:
        if i == n:
            contador += 1
    return contador

lista1 = []
nro = random.randint(1,10)
cont = 0
while cont < 15:
    num = random.randint(1,10)
    lista1.append(num)
    cont+= 1

print("La lista es:", lista1)
print("El numero es:", nro)
resultado = contar(lista1,nro)
print("La cantidad de veces que se repite", nro, "en la lista es:", resultado)
        