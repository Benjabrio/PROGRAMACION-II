import tkinter as tk

ventana = tk.Tk()
ventana.title("ContCreciente")


label = tk.Label(ventana, text="Contador")
label.grid(row=0, column=0,padx = 5)

cont_entry = tk.Entry(ventana, width=10)
cont_entry.grid(row=0, column=1,padx = 5)
cont_entry.insert(0, "88")
cont_entry.config(state='disabled')

cont = 88
def decreciente():
    global cont
    cont = cont - 1
    cont_entry.config(state='normal')
    cont_entry.delete(0,tk.END)
    cont_entry.insert(0,cont)
    cont_entry.config(state='disabled')

boton = tk.Button(ventana, text="-", command=decreciente,)
boton.grid(row=0, column=2,padx = 5)

ventana.mainloop()