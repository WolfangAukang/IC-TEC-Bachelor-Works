from __future__ import division
import math
import random
'''
Created on 26/08/2013

@author: Pedro
'''
def calculo():
    print ("Bienvenido a la calcula límite de x^2-2 cuando x tiende a 3")
    try:
        epsilon=input("Favor insertar valor epsilon (mayor a 0): ")
        n=input("Favor insertar cantidad de resultados deseados (mayor a 0): ")
    except:
        return "Error, datos no son válidos"
    if n<0 or epsilon<0:
        return "Error, datos no son válidos"
    else:
        izq=-(epsilon/7)+3
        der=(epsilon/7)+3
        return calculoaux(izq,der,n,[],0)
    
def calculoaux(valizq,valder,n,res,incres):
    if n==0:
        print "La lista de resultado(s) sería: " +str(res)
    else:
        incres=random.uniform(valizq,valder)
        if incres not in res and incres!=valizq and incres!=valder:
            return calculoaux(valizq,valder,n-1,res+[incres],0)
        
calculo()
        
calculo()