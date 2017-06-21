# -*- coding: cp1252 -*-
from Tkinter import *
from tkMessageBox import *
from ttk import *
'''
Created on 15/09/2013

@author:Pedro
'''

#--------------------------------------------
#Comandos generales
#--------------------------------------------
def salir():
    salida=askokcancel("Está seguro?", "Deseas salir del programa?")
    if salida==True:
        v0.destroy()

def creditos():
    credito=showinfo("Créditos", "Este programa fue realizado por:\nKevin Alvarado\nDavid Obando\nPedro Rodríguez\n"\
                     "nEstudiantes del Instituto Teconlógico de Costa Rica")

#--------------------------------------------
#Interfaz general
#--------------------------------------------

v0=Tk()
v0.geometry("1200x600")
v0.config(bg="red")
v0.resizable(0,0)
v0.title("Curiosdades matemáticas")

#Menu principal
menubarra = Menu(v0)
opcionmenu = Menu(menubarra, tearoff=0)
opcionmenu.add_command(label="Créditos", command=creditos)
opcionmenu.add_separator()
opcionmenu.add_command(label="Salir", command=salir)
menubarra.add_cascade(label="Opciones", menu=opcionmenu)

#Titulo del proyecto
titulo=Label(v0, text="Curiosidades Matemáticas", font=("Verdana",36), height=2, \
             bg="dark slate grey", relief="raised", justify="center").grid(row=1, column=4)

#Espacio de entrada
EntradaNumero=IntVar()
indicaciones=Label(v0, text="Favor insertar número:").grid(row=5, column=1)
txtEntrada=Entry(v0, textvariable=EntradaNumero).grid(row=5, column=2)

#Cuadros de información
'''Variable para datos string'''
SalidaString=StringVar()

'''Cuadro 1'''
textoindic1=Message(v0, textvariable=SalidaString, relief="sunken", bg="ghost white")
SalidaString.set("Holi banani")

#Botones
botonresolv=Button(v0, text="Resolver!", cursor="pirate").grid(row=5, column=3)

#Imagen por varas
imagen=PhotoImage(file="fffuuu.gif")
imageni=Label(v0, image=imagen).grid(row=6, column=4)

v0.config(menu=menubarra)
v0.mainloop()