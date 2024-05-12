"""
Ejercicio 10: Juego del Ahorcado 
Juego de Ahorcado: Crea un juego de ahorcado donde el jugador debe adivinar una palabra oculta antes de que se agoten los intentos. 
Puedes hacerlo con una lista predefinida de palabras.
"""
palabra = "australopithecus"
letras = list(palabra)
intentos = 6
cont = 0
letrasAdivinadas = ['_'] * len(palabra)

print("Es una palabra de:", len(letras), "letras.")

while cont < intentos:
    prueba = input("Adivine la letra: ")[0]
    if prueba in letras:
        print("Es una letra correcta")
        for i in range(len(palabra)):
            if letras[i] == prueba:
                letrasAdivinadas[i] = prueba
        print(" ".join(letrasAdivinadas))
        if "_" not in letrasAdivinadas:
            print("Adivinaste la palabra!!")
            break
    else:
        print("Letra incorrecta")
        cont = cont + 1
        print("Intentos restantes:", intentos - cont)
if cont == intentos:
    print("Se te acabaron los intentos, la palabra era:", palabra)

    