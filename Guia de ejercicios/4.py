frase = input("Ingrese una frase: ")
cont = 1

for i in frase: 
    if i == " ":
        cont = cont + 1
    
print("La cantidad de palabras que tiene es:", cont)