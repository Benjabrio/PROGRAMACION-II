import tkinter as tk
from tkinter import messagebox
import random 

ventana = tk.Tk()
ventana.title("Generador de números")

num1_label = tk.Label(ventana,text="Número 1",)
num1_label.grid(row=0, column=0, padx = 10, pady=10)
num2_label = tk.Label(ventana,text="Número 2",)
num2_label.grid(row=1, column=0, padx = 10, pady=10)
resultado_label = tk.Label(ventana,text="Número Generado",)
resultado_label.grid(row=2, column=0, padx = 10, pady=10)

spinbox1 = tk.Spinbox(ventana, from_=0, to=100,width=10)
spinbox1.grid(row=0, column=1, padx = 10, pady=10)
spinbox2 = tk.Spinbox(ventana, from_=0, to=100,width=10)
spinbox2.grid(row=1, column=1, padx = 10, pady=10)

entry = tk.Entry(ventana,width=10, state='disabled')
entry.grid(row=2, column=1, padx = 10, pady=10)

def generar():
    num1 = int(spinbox1.get())
    num2 = int(spinbox2.get())
    if num1 > num2:
        messagebox.showerror("ERROR","El primer número tiene que ser menor que el segundo")
    else:
        num3 = random.randint(num1,num2)
        entry.config(state='normal')
        entry.delete(0,tk.END)
        entry.insert(0,num3)
        entry.config(state='disabled')

boton = tk.Button(ventana,text="Generar", width= 10,command=generar)
boton.grid(row=3,column=1,padx = 10, pady=10)
ventana.mainloop()