class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getCantidad(self):
        return self.cantidad

    def mostrar_informacion(self):
        print("Los datos del producto son:" + "\n" + "Nombre: " + str(self.getNombre()) + "\n" + "Precio: " + str(self.getPrecio()) + "\n" + "Cantidad: " + str(self.getCantidad()))