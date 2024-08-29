import tkinter as tk

ventana = tk.Tk()
ventana.title("Peliculas")


titulo_label = tk.Label(ventana,text="Escribe el título de la película",)
titulo_label.grid(row=0, column=0, padx = 10, pady=10)
pelicula_label = tk.Label(ventana,text="Películas",)
pelicula_label.grid(row=0, column=1, padx = 10, pady=10)

entrada = tk.Entry(ventana, width=16)
#entrada.grid(row=1, column=0, padx = 10, pady=10)
entrada.place(x=40, y=60)

lista = tk.Listbox(ventana, width= 20, height=8)
lista.grid(row=1,column=1, padx = 10, pady=10)

def agregar():
    pelicula = entrada.get()
    lista.insert(0,pelicula)
    entrada.delete(0,tk.END)

boton = tk.Button(ventana,text="Añadir", width= 10,command=agregar)
boton.place(x=50, y=100)

ventana.mainloop()