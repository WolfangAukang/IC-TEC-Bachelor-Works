#ver 3.x
from Tkinter import *
import time
import threading


#carga el archivo en una lista de trabajo LInstruccion y tambien
#en el componente visual
def cargaMueve(LInstruccion):
    LInstruccion = cargaLista(LInstruccion)
    for linact in range ( len(LInstruccion) ):
        hilo = (threading.currentThread(), LInstruccion[linact])
        time.sleep (1)
        lb1.selection_set(linact)
        time.sleep (0.5)
        lb1.selection_clear(linact)
        salida.insert(END, "Calculo "+str(linact)+"\n")
    salida.insert(END,"Fin de la ejecucion")

        
#cargando el archivo en el lisbox y en una lista...
def cargaLista(LInstruccion):
    f=open("CodigosListbox/Golbach.py", mode="r")
    contador = 0
    linea = f.readline()
    while linea != "":
        lb1.insert(contador, linea)
        LInstruccion.append(linea)
        linea = f.readline()
        contador = contador+1
    f.close()
    return LInstruccion
    
#Creando la ventana
global LInstruccion
LInstruccion=[]  #lista global donde queda la carga del archivo..

top = Tk()
lb1 = Listbox(top,bg="white", fg="blue", selectbackground="red", highlightbackground="yellow",  activestyle="dotbox",width=100, height=25)
salida = Text(top, width=40, height=15)
btn = Button(top, text="Go", command=lambda:cargaMueve(LInstruccion))

btn.pack()
lb1.pack()
salida.pack()
w=threading.Thread(target=lambda:cargaMueve(LInstruccion), name="cc")
w.start()

top.mainloop()
