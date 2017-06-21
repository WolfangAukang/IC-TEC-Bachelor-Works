# -*- coding: cp1252 -*-
'''
Created on 15/10/2013

@author: Pedro
'''
#Variable inv indica si es inverso por medio de booleano
def diagonalesizq(palabra,m,inv=False):
    if inv==True:
        m.reverse()
    total=len(palabra)
    totalfil=len(m)-1
    totalcol=len(m[0])-1
    if total>totalcol or total>totalfil:
        return "Error, palabra más grande que sopa de letras"
    norig=0
    res=False
    while norig<=(totalfil-total+1) and res==False:
        try:
            busqueda=m[norig].index(palabra[0])
            if total-1+busqueda>totalcol:
                norig+=1
            else:
                resp=[]
                n=norig
                for i in range(busqueda, busqueda+total):
                    resp+=m[n][i]
                    n+=1
                n=0
                if resp==list(palabra):
                    res=True
                else:
                    norig+=1
        except:
            norig+=1
    if res==False:
        return res
    else:
        return "("+str(abs(norig-totalfil))+","+str(busqueda)+")"

def diagonalesder(palabra,m,inv=False):
    total=len(palabra)
    totalfil=len(m)-1
    totalcol=len(m[0])-1
    if total>totalcol or total>totalfil:
        return "Error, palabra más grande que sopa de letras"
    norig=0
    res=False
    while norig<=(totalfil-total+1) and res==False:
        try:
            busqueda=m[norig].index(palabra[0])
            if busqueda+1-total<0:
                norig+=1
            else:
                resp=[]
                n=norig
                for i in range(busqueda, busqueda-total,-1):
                    resp+=m[n][i]
                    n+=1
                n=0
                if resp==list(palabra):
                    res=True
                else:
                    norig+=1
        except:
            norig+=1
    if res==False:
        return res
    else:
        return "("+str(abs(norig-totalfil))+","+str(abs(norig-totalcol))+")"