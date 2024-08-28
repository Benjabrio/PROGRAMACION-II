import tkinter as tk
from tkinter import messagebox
import random

ventana = tk.Tk()
ventana.title("Juego Matemático")
ventana.geometry("300x300")
ventana.config(bg="lightblue")

cont = 0
buenas = 0
malas = 0

signo_label = tk.Label(ventana,text="?",bg="lightblue")
signo_label.grid(row=0, column=1, padx = 10, pady=25)
juego_label = tk.Label(ventana,text="Juegos:",bg="lightblue")
juego_label.place(x=200,y=170)
buenos_label = tk.Label(ventana,text="Buenos:",bg="lightblue")
buenos_label.place(x=200,y=200)
malos_label = tk.Label(ventana,text="Malos:",bg="lightblue")
malos_label.place(x=200,y=230)
numjuego_label = tk.Label(ventana,text="",bg="lightblue")
numjuego_label.place(x=260,y=170)
numbueno_label = tk.Label(ventana,text="",bg="lightblue")
numbueno_label.place(x=260,y=200)
nummalo_label = tk.Label(ventana,text="",bg="lightblue")
nummalo_label.place(x=260,y=230)

def signos():
    operacion = opcion_seleccionada.get()
    if operacion == "Sumar":
        signo_label.config(text="+")
    elif operacion == "Restar":
        signo_label.config(text="-")
    elif operacion == "Multiplicar":
        signo_label.config(text="*")
    elif operacion == "Dividir":
        signo_label.config(text="/")
    else:
        signo_label.config(text="?")

opcion_seleccionada = tk.StringVar(value="")
opcion1 = tk.Radiobutton(ventana,text="Sumar",variable=opcion_seleccionada,value="Sumar",command=signos,bg="lightblue")
opcion1.place(x=50,y=100)
opcion2 = tk.Radiobutton(ventana,text="Restar",variable=opcion_seleccionada,value="Restar",command=signos,bg="lightblue")
opcion2.place(x=50,y=130)
opcion3 = tk.Radiobutton(ventana,text="Multiplicar",variable=opcion_seleccionada,value="Multiplicar",command=signos,bg="lightblue")
opcion3.place(x=50,y=160)
opcion4 = tk.Radiobutton(ventana,text="Dividir",variable=opcion_seleccionada,value="Dividir",command=signos,bg="lightblue")
opcion4.place(x=50,y=190)

def reset_contador():
    global cont,buenas,malas
    cont = 0
    buenas = 0
    malas = 0
    numjuego_label.config(text="0")
    numbueno_label.config(text="0")
    nummalo_label.config(text="0")

dificultad_seleccionada = tk.StringVar(value="")
dificultad_seleccionada.trace_add('write', reset_contador)

dif1 = tk.Radiobutton(ventana,text="Facil",variable=dificultad_seleccionada,value="Facil",command=reset_contador,bg="lightblue")
dif1.place(x=30,y=270)
dif2 = tk.Radiobutton(ventana,text="Medio",variable=dificultad_seleccionada,value="Medio",command=reset_contador,bg="lightblue")
dif2.place(x=100,y=270)
dif3 = tk.Radiobutton(ventana,text="Dificil",variable=dificultad_seleccionada,value="Dificil",command=reset_contador,bg="lightblue")
dif3.place(x=180,y=270)

primer_entry = tk.Entry(ventana, width=10, state='disabled')
primer_entry.grid(row=0, column=0, padx=5,pady=25)
segundo_entry = tk.Entry(ventana, width=10, state='disabled')
segundo_entry.grid(row=0, column=2, padx=5,pady=25)
tercer_entry = tk.Entry(ventana, width=10)
tercer_entry.grid(row=1, column=3, padx=5,pady=15)

def numero():
    dificultad = dificultad_seleccionada.get()
    if not dificultad:
        messagebox.showerror("ATENCIÓN", "Primero tenes que seleccionar una dificultad para jugar!")
    else:
        if dificultad == "Facil":
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)      
        elif dificultad == "Medio":
            num1 = random.randint(1,100)
            num2 = random.randint(1,100)
        elif dificultad == "Dificil":
            num1 = random.randint(1,1000)
            num2 = random.randint(1,1000)
        primer_entry.config(state='normal')
        primer_entry.delete(0,tk.END)
        primer_entry.insert(0,num1)
        primer_entry.config(state='disabled')
        segundo_entry.config(state='normal')
        segundo_entry.delete(0,tk.END)
        segundo_entry.insert(0,num2)
        segundo_entry.config(state='disabled')

def operacion():
    num1 = int(primer_entry.get())
    num2 = int(segundo_entry.get())
    operacion = opcion_seleccionada.get()
    if not operacion:
        messagebox.showerror("ATENCIÓN", "Primero tenes que seleccionar una operación para jugar!")
    else:
        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2
        elif operacion == "Dividir":
            resultado = num1 / num2
        global cont 
        cont = cont + 1 
        numjuego_label.config(text=cont)
        num3 = float(tercer_entry.get())
        global buenas
        global malas
        if num3 == resultado:
            buenas = buenas + 1
            numbueno_label.config(text=buenas)
        else:
            malas = malas + 1
            nummalo_label.config(text=malas)
        tercer_entry.delete(0,tk.END)
        
    

boton1 = tk.Button(ventana,text="Nuevo número", width= 12,command=numero)
boton1.grid(row=0, column=3,padx=5,pady=5)
boton2 = tk.Button(ventana,text="Resultado", width= 12, command=operacion)
boton2.grid(row=2, column=3,padx=5,pady=5)

ventana.mainloop()