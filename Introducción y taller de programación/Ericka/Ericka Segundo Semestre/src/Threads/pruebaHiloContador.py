from Tkinter import *
import thread
import time

def registrar():
    print("aqui debe cambiar lo que dice la etiqueta")
    pass
    
def activaContador(inicio, final):
    global contador
    for i in range(inicio, final, 1):
        contador.set(str(i))
        time.sleep(0.5)
    print("termine de contar")
    
        
ventana = Tk()

etContador=Label(ventana,text="contador").pack()
contador=StringVar()
contador.set("")   # aqui aparece en la ventana
txtContador= Entry(ventana, textvariable=contador).pack()


etNombre=Label(ventana,text="Nombre").pack()
nombre=StringVar()
nombre.set("cosita")   # aqui aparece en la ventana
txtNombre= Entry(ventana, textvariable=nombre).pack()
lblResultado = Label(ventana, text="").pack()


btnIngresar=Button(ventana,text="Registrar Nombre", command=registrar).pack() 
# Lanzamos un hilo
thread.start_new_thread(activaContador, (1,100))

mainloop()
