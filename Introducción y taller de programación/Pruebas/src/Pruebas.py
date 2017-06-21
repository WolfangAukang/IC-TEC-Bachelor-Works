from __future__ import division
import math
'''
Created on 11/09/2013

@author: Pedro
'''
def convierteaint(lista,n=0,listanueva=[]):
    if n==len(lista):
        return listanueva
    else:
        try:
            int(lista[n])
            return convierteaint(lista,n+1,listanueva+[int(lista[n])])
        except ValueError:
            return convierteaint(lista,n+1,listanueva+[lista[n]])

def quitacomascrealista(stringo,n=0,inse="",lista=[]):
    if n==len(stringo):
        if inse=="":
            a=input("Deseas cambiar los numeros de string a int? (True o False) ")
            if a:
                return convierteaint(lista)
            else:
                return lista
        else:
            a=input("Deseas cambiar los numeros de string a int? (True o False) ")
            if a:
                return convierteaint(lista)
            else:
                return lista+[inse]
    else:
        if stringo[n]==" " or stringo[n]==",":
            return quitacomascrealista(stringo,n+1,"",lista+[inse])
        else:
            return quitacomascrealista(stringo,n+1,inse+stringo[n],lista)