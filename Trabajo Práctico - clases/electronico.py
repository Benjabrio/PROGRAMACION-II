from producto import Producto

class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        super().__init__(nombre,precio,cantidad,)
        self.modelo = modelo
        self.marca = marca

    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo
    
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        #print(info) Devolvía "none" este print
        print("Marca: ", str(self.getMarca()))
        print("Modelo: ", str(self.getModelo()))