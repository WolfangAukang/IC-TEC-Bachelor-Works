'''
Created on 24/09/2013

@author: Pedro
'''
def crearMatriz(corig,c,cedit,f,m=[],ins=[]):
    while f>0:
        dato=input("Favor insertar dato: ")
        ins+=[dato]
        if cedit==1:
            cedit=corig
            f-=1
            c-=1
            m+=[ins]
            ins=[]
        else:
            cedit-=1    
    return m
        

def pedirDatosMatriz():
    try:
        c=input("De cuantas columnas desea la matriz? ")
        f=input("De cuantas filas desea la matriz? ")
        return crearMatriz(c,c,c,f)
    except ValueError:
        return "Error, datos invalidos"
    
def sopadeletras(f,c,m=[]):
    i=f
    while i>0:
        m.append([])
        i-=1
    i=c
    e=0
    while i>0 and e==c:
        if e==0:
            i-=1
        else:
            m[e].append("")

sopadeletras(8,8)
            
        
        