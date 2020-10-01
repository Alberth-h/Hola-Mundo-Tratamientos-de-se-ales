from tkinter import *

ventana = Tk()
ventana.title("Mi ventana")
ventana.geometry("800x600")

etiqueta1 = Label(ventana, text="Primera etiqueta")
etiqueta1.pack()

etiqueta2 = Label(ventana, text="Segunda etiqueta")
etiqueta2.pack()

ingresoTexto = Entry(ventana)
ingresoTexto.pack()

boton = Button(ventana, text="Boton")
boton.pack()

ventana.mainloop()