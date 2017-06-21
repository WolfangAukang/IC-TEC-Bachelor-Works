'''
Created on 04/11/2013

@author: Pedro
'''
from Tkinter import *
v0=Tk()

def cambio():
    botonvariable.config(text=entrada.get())

texto=""
entrada=StringVar()
entry=Entry(v0,textvariable=entrada).pack()
botoncambio=Button(v0,text="Cambio",command=cambio).pack()
botonvariable=Button(v0).pack()


v0.mainloop()