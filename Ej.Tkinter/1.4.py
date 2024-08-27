import tkinter as tk

ventana = tk.Tk()
ventana.title("Contador")

label = tk.Label(ventana, text="Contador")
label.grid(row=0, column=0, padx = 5)

cont_entry = tk.Entry(ventana, width=10)
cont_entry.grid(row=0, column=1, padx=5)
cont_entry.insert(0,"0")
cont_entry.config(state='disabled')

cont = 0
def aumentar():
    global cont
    cont += 1
    cont_entry.config(state='normal')
    cont_entry.delete(0,tk.END)
    cont_entry.insert(0,cont)
    cont_entry.config(state='disabled')

def decreciente():
    global cont
    cont = cont - 1
    cont_entry.config(state='normal')
    cont_entry.delete(0,tk.END)
    cont_entry.insert(0,cont)
    cont_entry.config(state='disabled')

def resetear():
    global cont
    cont = 0
    cont_entry.config(state='normal')
    cont_entry.delete(0,tk.END)
    cont_entry.insert(0,cont)
    cont_entry.config(state='disabled')

boton = tk.Button(ventana, text="Count Up",command=aumentar)
boton.grid(row=0, column=2,padx = 5)

boton = tk.Button(ventana, text="Count Down",command=decreciente)
boton.grid(row=0, column=3,padx = 5)

boton = tk.Button(ventana, text="Reset", command=resetear)
boton.grid(row=0, column=4,padx = 5)

ventana.mainloop()