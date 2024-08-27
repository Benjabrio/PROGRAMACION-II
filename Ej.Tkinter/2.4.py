import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora 2")

v1_label = tk.Label(ventana,text="Valor 1",)
v1_label.grid(row=1, column=0, padx = 10, pady=10)
v2_label = tk.Label(ventana,text="Valor 2",)
v2_label.grid(row=2, column=0, padx = 10, pady=10)
resultado_label = tk.Label(ventana,text="Resultado")
resultado_label.grid(row=3, column=0, padx = 10, pady=10)
op_label = tk.Label(ventana,text="Operaciones")
op_label.grid(row=0,column=2,padx=10,pady=10)

primer_entry = tk.Entry(ventana, width=10)
primer_entry.grid(row=1, column=1, padx=5)
primer_entry.insert(0,0)
segundo_entry = tk.Entry(ventana, width=10)
segundo_entry.grid(row=2, column=1, padx=5)
segundo_entry.insert(0,0)
resultado_entry = tk.Entry(ventana, width=10, state='disabled')
resultado_entry.grid(row=3, column=1, padx=5)

opcion_seleccionada = tk.StringVar(value="Sumar")
opcion1 = tk.Radiobutton(ventana,text="Sumar",variable=opcion_seleccionada,value="Sumar")
opcion1.grid(row=1, column=2, padx = 10, pady=10)
opcion2 = tk.Radiobutton(ventana,text="Restar",variable=opcion_seleccionada,value="Restar")
opcion2.grid(row=2, column=2, padx = 10, pady=10)
opcion3 = tk.Radiobutton(ventana,text="Multiplicar",variable=opcion_seleccionada,value="Multiplicar")
opcion3.grid(row=3, column=2, padx = 10, pady=10)
opcion4 = tk.Radiobutton(ventana,text="Dividir",variable=opcion_seleccionada,value="Dividir")
opcion4.grid(row=4, column=2, padx = 10, pady=10)

def calcular():
    try:
        num1 = float(primer_entry.get())
        num2 = float(segundo_entry.get())
        operacion = opcion_seleccionada.get()
        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2
        elif operacion == "Dividir":
            if num2 == 0:
                messagebox.showerror("Error","No se puede dividir por 0")
                return
            else:
                resultado = num1 / num2
        resultado_entry.config(state='normal')
        resultado_entry.delete(0,tk.END)
        resultado_entry.insert(0,resultado)
        resultado_entry.config(state='disabled')
    except:
        messagebox.showerror("Error", "Complete las casillas con números")

boton = tk.Button(ventana,text="Calcular", width= 8, command=calcular)
boton.grid(row=4,column=1,padx = 10, pady=10)

ventana.mainloop()

