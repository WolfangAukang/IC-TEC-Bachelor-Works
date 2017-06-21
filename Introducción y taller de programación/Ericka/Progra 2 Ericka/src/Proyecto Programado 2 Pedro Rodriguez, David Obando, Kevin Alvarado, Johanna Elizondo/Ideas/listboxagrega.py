# -*- coding: cp1252 -*-
from Tkinter import *
from tkMessageBox import *

palabras=[]

def insertar():
    global palabras
    inserte=str(Entr.get())
    if len(inserte)<11:
        if inserte in palabras:
            showinfo("Error","Palabra ya está en la lista")
        else:
            listbox.insert(END,inserte)
            palabras+=[inserte]
            print palabras
    else:
        showinfo("Error","Datos no validos")

def borrar():
    global palabras
    palabra=str(Entr.get())
    if palabra in palabras:
        pos=palabras.index(palabra)
        palabras.remove(palabra)
        listbox.delete(pos)
        print palabras
    else:
        showinfo("Error","Dicha palabra no se encuentra en la lista")
    
    
v0=Tk()
frame= Frame(v0, bd=2, relief=SUNKEN, width=100, height=50)
yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)
listbox=Listbox(frame, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=50, height=10)
listbox.grid(row=0, column=0, sticky=N+S+E+W)
yscrollbar.config(command=listbox.yview)
frame.grid(row=1, column=1, columnspan=3)
Entr=StringVar()
Entrad=Entry(v0, textvariable=Entr,bd=3).grid(row=2,column=1)
Boton1=Button(v0, text="Insertar", command=insertar,bd=3).grid(row=2,column=2)
Boton2=Button(v0, text="Borrar", command=borrar,bd=3).grid(row=2,column=3)

v0.mainloop()
