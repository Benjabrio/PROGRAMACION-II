import tkinter as tk

ventana = tk.Tk()
ventana.title("Factorial")


label = tk.Label(ventana, text="n")
label.grid(row=0, column=0, padx = 5)

label = tk.Label(ventana, text="Factorial (n) = ")
label.grid(row=0, column=2, padx = 5)

n = 1

cont_entry = tk.Entry(ventana, width=10)
cont_entry.grid(row=0, column=1,padx = 5)
cont_entry.insert(0,n)
cont_entry.config(state='disabled')

fact_entry = tk.Entry(ventana, width=10)
fact_entry.grid(row=0, column=3,padx = 5)
fact_entry.insert(0,"1")
fact_entry.config(state='disabled')

def factorial(x):
    resultado = 1
    for i in range(2, x + 1):
        resultado = resultado * i
    fact_entry.config(state='normal')
    fact_entry.delete(0,tk.END)
    fact_entry.insert(0,resultado)
    fact_entry.config(state='disabled')

def siguiente():
    global n
    n = n + 1
    cont_entry.config(state='normal')
    cont_entry.delete(0,tk.END)
    cont_entry.insert(0,n)
    cont_entry.config(state='disabled')
    factorial(n)

boton = tk.Button(ventana, text="Siguiente", command=siguiente)
boton.grid(row=0, column=4,padx = 5)

ventana.mainloop()