from electronico import Electronico
from alimento import Alimento

def elegir():
    print("Seleccione el tipo de producto que desea elegir:")
    print("1. Electrónico")
    print("2. Alimento")
    print("3. Salir")
    
    opcion = input("Ingrese su opción (1,2 o 3 para salir.): ")
    return opcion


def llamar():
    while True:
        opcion = elegir()

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            marca = input("Ingrese la marca del producto: ")
            modelo = input("Ingrese el modelo del producto: ")
            
            electronico = Electronico(nombre, precio, cantidad, marca, modelo)
            electronico.mostrar_informacion()
        
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            fecha_expiracion = input("Ingrese la fecha de expiración del producto: ")
            
            alimento = Alimento(nombre, precio, cantidad, fecha_expiracion)
            alimento.mostrar_informacion()

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

resultado = llamar()
