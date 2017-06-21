'''
Created on 02/10/2013

@author: Pedro
'''
def espacio(n):
    if n==0:
        return ""
    else:
        return " "+espacio(n-1)
    
def demostracion(n,posorig=0,norig=1,res=""):
    if n==posorig:
        return res
    else:
        if posorig==0:
            res+=str(espacio(n-norig))
        if norig==posorig:
            return demostracion(n,0,norig+1,res+"\n")
        else:
            return demostracion(n,posorig+1,norig,res+"*")