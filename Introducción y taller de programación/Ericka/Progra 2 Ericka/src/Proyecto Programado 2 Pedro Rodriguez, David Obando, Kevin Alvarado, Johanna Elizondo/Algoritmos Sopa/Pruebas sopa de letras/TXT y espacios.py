from Tkinter import *
from random import *

j=[['', '', '', '', '', '', '', '', '', ''],\
   ['', '', '', '', 'a', '', '', '', '', ''],\
   ['', '', '', '', 'c', '', '', '', '', ''],\
   ['', '', '', 'j', 'o', 'r', 'c', 'o', '', ''],\
   ['', '', '', '', 'l', '', '', '', '', ''],\
   ['', '', '', '', 'i', '', '', '', '', ''],\
   ['', '', '', '', 't', '', '', '', '', ''],\
   ['', '', '', '', 'o', '', '', '', '', ''],\
   ['', '', '', '', '', '', '', '', '', ''],\
   ['', '', '', '', '', '', '', '', '', '']]


#Llena espacios vacios de la sopa
def llenarespacios(m):
    m=j
    c=0
    f=0
    while f!=10:
        if m[c][f]=="":
            letra=randint(97,122)
            m[c][f]=chr(letra)
        else:
            pass
        c+=1
        if c==10:
            c=0
            f+=1
    return m

#Guarda la sopa en archivo txt
def creasopas(nombre,matriz,palabras):
    f=open("leer.txt","a")
    f.write(str(nombre)+"\n")
    f.write(str(matriz)+"\n")
    f.write(str(palabras)+"\n")
    f.write("-------------------------------------")
    f.close()

#busca si la sopa esta guardada (todavia no la carga)
def buscarensopa(nombresopa):
    nombresopa+="\n"
    f=open("leer.txt","r")
    texto=f.readlines()
    if nombresopa not in texto:
        return "Error, no existe tal sopa"
    else:
        pos=texto.index(nombresopa)
        m=texto[pos+1]
        pal=texto[pos+2]
        print m
        print pal
