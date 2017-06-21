'''
Created on 26/09/2013

@author: Pedro
'''

#matrices e iteracion


i=1
while i <=20:
    print(i)
    i= i+2

def crearMatriz(f, c):
    m=[]
    #incluir f cantidad de filas
    while len(m) < f:
        m.append([])
    #llenar las filas con c cantidad de columnas cada una
    i=0
    while i < len(m):
        j=1
        while j<=c:
            dato = int (input("Dato"))
            m[i].append(dato)
            j= j+1
        i=i+1
    return m

def verMatriz(m):
    hilera =""
    i=0
    while i < len(m):
        j=0
        while j < len(m[i]):
            hilera += str(m[i][j]) + " "
            j= j+1
        i=i+1
        hilera += "\n"
    return hilera


def crearSopaLetras(hilera):
    m= [[]]
    cf=0
    i=0    # i lleva el simbolo actual dentro de la hilera
    while i < len(hilera):
        if hilera [i] != "\n":
            m[cf].append(hilera[i])
        else:
            m.append([])
            cf+=1
        i+=1
    return m


def crearSopa2(hilera):
    m=[]
    tiras = hilera.split("\n")
    i=0
    while i< len(tiras):
        m.append ( list(tiras[i]) )
        i+=1
    return m
                   
def horizontalID(m,palabra,a=0,e=0,i=0,w="", c=True):
    while a<len(m):
        if e==len(m[e]):
            a+=1
        if m[a][e]!=palabra[e]:
            e+=1
        else:
            while c==True:
                w=str(m[a][e:i+1])
                if w==palabra:
                    return str((a,i))
                else:
                    c==False
                    i-=0
    return False