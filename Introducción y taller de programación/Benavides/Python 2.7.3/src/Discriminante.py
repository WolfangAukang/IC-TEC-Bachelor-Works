'''
Created on 07/03/2013

@author: Leeecher
'''
from __future__ import division
from math import sqrt
def Discriminante(a,b,c):
    d=(b**2)-(4*a*c)           
    if a == 0:
        print ("Error, se dividiria entre 0 y se indefiniria") 
    else:
        if d < 0:
            print("No hay discriminante")  
        else:
            x=(-b+sqrt(d))/(2*a)
            x1=(-b-sqrt(d))/(2*a)
            return(x,x1)
