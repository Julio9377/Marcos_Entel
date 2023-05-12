from tkinter import *

ventana = Frame(height=500,width=400)
ventana.pack(padx=20,pady=20)

etiqueta = Label(text="Nombre: ", font=("Chiller",15)).place(x=0,y=0)
etiqueta2 = Label(text="Alex").place(x=100,y=0)
ventana.mainloop()