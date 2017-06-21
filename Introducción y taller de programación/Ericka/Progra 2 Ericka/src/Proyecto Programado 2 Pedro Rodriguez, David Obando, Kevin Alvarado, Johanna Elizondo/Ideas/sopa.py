# -*- coding: cp1252 -*-

#importando modulos
from Tkinter import *
from tkMessageBox import *

#cargando venta principal
master = Tk()
master.withdraw()

def cerrar():
    juego.withdraw()
    master.destroy()

matriz=[["","","","","","","","","",""],\
       ["","","","","","","","","",""],\
       ["","","","","","","","","",""],\
       ["","","","","","","","","",""],\
       ["","","","","","","","","",""],\
       ["","","","","","","","","",""],\
       ["","","","","","","","","",""],\
       ["","","","","","","","","",""],\
       ["","","","","","","","","",""],\
       ["","","","","","","","","",""]]

listabotones=[]

palabras=[]

def nombrebotones():
    global listabotones
    n=0
    while n!=100:
        listabotones.append("b"+str(n))
        n+=1

def crearbotones():
    global listabotones
    posx=620
    posy=33
    botx=1
    boty=1
    f=0
    c=0
    for i in listabotones:
        i=Button(juego,text=matriz[f][c], relief=RAISED, width=7,height=3,bg="yellow").place(x=posx, y=posy)
        botx+=1
        posx+=60
        c+=1
        if botx==11:
            botx=1
            f+=1
            c=0
            boty+=1
            posx=620
            posy+=57

def buscarsopa():
    global matriz
    global palabras
    nombresopa="rostipollos"
    nombresopa+="\n"
    f=open("Sopas Guardadas/Sopas Guardadas.txt","r")
    texto=f.readlines()
    if nombresopa not in texto:
        showerror("Error","Error, no existe tal sopa")
    else:
        pos=texto.index(nombresopa)
        matrizacrear=list(texto[pos+1])
        can=0
        lineamatriz=[]
        matriz=[]
        for i in range(0,100):
            lineamatriz+=matrizacrear[i]
            can+=1
            if can%10==0 and can!=0:
                matriz+=[lineamatriz]
                lineamatriz=[]
        cantidadpalabras=int(texto[pos+2])
        i=0
        linea=3
        palabras=[]
        while i!=cantidadpalabras:
            agregar=str(texto[pos+linea])
            palabras+=[agregar[:-1]]
            i+=1
            linea+=1
            agregar=""
        print palabras

def agregarpalabraslistbox():
    for i in palabras:
        listbox.insert(END,i)
    
#Ventana de juego
juego=Toplevel(bg="black")
juego.attributes('-fullscreen', True)
framelistbox=Frame(juego, bd=2, relief=SUNKEN, width=120, height=70)
yscrollbar = Scrollbar(framelistbox)
yscrollbar.grid(row=0, column=1, sticky=N+S)
listbox=Listbox(framelistbox, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=60, height=15)
listbox.grid(row=0, column=0, sticky=N+S+E+W)
yscrollbar.config(command=listbox.yview)
framelistbox.place(x=60,y=300)
Entr=StringVar()
Entrad=Entry(juego, textvariable=Entr,bd=3,width=40).place(x=60,y=550)
Boton1=Button(juego, text="Comenzar búsqueda",activebackground="orange",bd=3,bg="dark orange").place(x=320,y=548)
Botoncerrar=Button(juego, text="Regresar al menú principal",command=cerrar,activebackground="orange", bd=6, width=25, bg="dark orange").place(x=1100,y=725)

'''Matriz de botones'''
framematriz=Frame(juego, bd=2, bg="dark orange",relief=SUNKEN, width=603, height=573).place(x=618,y=31)

buscarsopa()
agregarpalabraslistbox()
nombrebotones()
print matriz
crearbotones()
mainloop()