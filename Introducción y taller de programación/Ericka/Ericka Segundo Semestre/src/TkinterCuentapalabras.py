# -*- coding: cp1252 -*-
from Tkinter import *
from tkMessageBox import *
'''
Created on 12/09/2013

@author: Pedro
'''
v0=Tk()

v0.title("Ordena Palabras")
v0.geometry("120x200")

titulo=Label(v0,text="Ordena Palabras").grid(row=1,column=1)

texto1=Label(v0,text="Palabra 1").grid(row=2,column=1)
texto2=Label(v0,text="Palabra 2").grid(row=4,column=1)
texto3=Label(v0,text="Palabra 3").grid(row=6,column=1)

valorHilera1=StringVar()
txtEntrada=Entry(v0,textvariable=valorHilera1).grid(row=3, column=1)

valorHilera2=StringVar()
txtEntrada=Entry(v0,textvariable=valorHilera2).grid(row=5, column=1)

valorHilera3=StringVar()
txtEntrada=Entry(v0,textvariable=valorHilera3).grid(row=7, column=1)

def salir():
    avisosalida=askyesno("¿Desea salir?", "¿Está seguro de que deseas salir? Eso no es bueno :(")
    if avisosalida:
        v0.destroy()

def compara(p1, p2):
    universo="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVxXyYzZ"
    if p1 == "" and p2== "":
        return 0   # las hileras son iguales
    elif len(p1) > 0 and len (p2) > 0:
        ordP1 = universo.find(p1[0])
        ordP2 = universo.find(p2[0])
        if ordP1 == ordP2:
            return compara(p1[1:], p2[1:])
        elif ordP1 < ordP2:
            return -1
        else:
            return 1
    elif len(p1) > 0:
        return 1
    else:
        return -1
    
def comparagen():
    p1=str(valorHilera1.get())
    p2=str(valorHilera2.get())
    p3=str(valorHilera3.get())
    if compara(p1,p2)==1:
        if compara(p1,p3)==1:
            if compara(p2,p3)==1:
                return showinfo("Respuesta","La respuesta sería "+str(p3)+", "+str(p2)+" y "+str(p1))
            else:
                return showinfo("Respuesta","La respuesta sería "+str(p2)+", "+str(p3)+" y "+str(p1))
        else:
            return showinfo("Respuesta","La respuesta sería "+str(p2)+", "+str(p1)+" y "+str(p3))
    else:
        if compara(p2,p3)==1:
            if compara(p1,p3)==1:
                return showinfo("Respuesta","La respuesta sería "+str(p3)+", "+str(p1)+" y "+str(p2))
            else:
                return showinfo("Respuesta","La respuesta sería "+str(p1)+", "+str(p3)+" y "+str(p2))
        else:
            return showinfo("Respuesta","La respuesta sería "+str(p1)+", "+str(p2)+" y "+str(p3))

                                   
bot1=Button(v0, text="Calcular!", command= comparagen, bd=3, width=10).grid(row=8,column=1)

bot2=Button(v0, text="Salir :(", command= salir, bd=3, width=10).grid(row=9,column=1)


v0.mainloop()