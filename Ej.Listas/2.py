def maxymin(lista):
    max = lista[0]
    min = lista[0]
    for i in lista:      
        if i > max:
            max = i
        if i < min:
            min = i
    return (max, min)
        

lista2 = []
cont = 0
while cont < 5:
    num = int(input("Ingrese 5 numeros para la lista:"))
    lista2.append(num)
    cont+= 1

print(lista2)
resultado = maxymin(lista2)
print("El máximo es:", resultado[0], "y el minimo es:", resultado[1])