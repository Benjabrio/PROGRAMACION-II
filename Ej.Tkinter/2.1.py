import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora")

label = tk.Label(ventana, text="Primer número")
label.grid(row=0, column=0, padx = 5, pady=5)

label = tk.Label(ventana, text="Segundo número")
label.grid(row=1, column=0, padx = 5, pady=5)

label = tk.Label(ventana, text="Resultado")
label.grid(row=2, column=0, padx = 5, pady=5)

primer_entry = tk.Entry(ventana, width=10)
primer_entry.grid(row=0, column=1, padx=5)
primer_entry.insert(0,0)
segundo_entry = tk.Entry(ventana, width=10)
segundo_entry.grid(row=1, column=1, padx=5)
segundo_entry.insert(0,0)
resultado_entry = tk.Entry(ventana, width=10, state='disabled')
resultado_entry.grid(row=2, column=1, padx=5)

def sumar():
    num1 = float(primer_entry.get())
    num2 = float(segundo_entry.get())
    resultado = num1 + num2
    resultado_entry.config(state='normal')
    resultado_entry.delete(0,tk.END)
    resultado_entry.insert(0,resultado)
    resultado_entry.config(state='disabled')
def restar():
    num1 = float(primer_entry.get())
    num2 = float(segundo_entry.get())
    resultado = num1 - num2
    resultado_entry.config(state='normal')
    resultado_entry.delete(0,tk.END)
    resultado_entry.insert(0,resultado)
    resultado_entry.config(state='disabled')
def multiplicar():
    num1 = float(primer_entry.get())
    num2 = float(segundo_entry.get())
    resultado = num1 * num2
    resultado_entry.config(state='normal')
    resultado_entry.delete(0,tk.END)
    resultado_entry.insert(0,resultado)
    resultado_entry.config(state='disabled')
def dividir():
    num1 = float(primer_entry.get())
    num2 = float(segundo_entry.get())
    if num2 == 0:
        messagebox.showerror("Error","No se puede dividir por 0")
        return
    else:
        resultado = num1 / num2
    resultado_entry.config(state='normal')
    resultado_entry.delete(0,tk.END)
    resultado_entry.insert(0,resultado)
    resultado_entry.config(state='disabled')
def porcentaje():
    num1 = float(primer_entry.get())
    num2 = float(segundo_entry.get())
    resultado = (num1 * num2) / 100
    resultado_entry.config(state='normal')
    resultado_entry.delete(0,tk.END)
    resultado_entry.insert(0,resultado)
    resultado_entry.config(state='disabled')
def limpiar():
    primer_entry.delete(0,tk.END)
    segundo_entry.delete(0,tk.END)
    resultado_entry.config(state='normal')
    resultado_entry.delete(0,tk.END)
    resultado_entry.config(state='disabled')



boton1 = tk.Button(ventana, text="+",command=sumar)
boton1.grid(row=3, column=0,padx = 5,pady=5,)
boton2 = tk.Button(ventana, text="-",command=restar)
boton2.grid(row=3, column=1,padx = 5,pady=5)
boton3 = tk.Button(ventana, text="*",command=multiplicar)
boton3.grid(row=4, column=0,padx = 5,pady=5)
boton = tk.Button(ventana, text="/",command=dividir)
boton.grid(row=4, column=1,padx = 5,pady=5)
boton = tk.Button(ventana, text="%",command=porcentaje)
boton.grid(row=5, column=0,padx = 5,pady=5)
boton = tk.Button(ventana, text="CLEAR",command=limpiar)
boton.grid(row=5, column=1,padx = 5,pady=5)



ventana.mainloop()