from __future__ import division
'''
Created on 16/05/2013

@author: Pedro
'''
import sys
sys.setrecursionlimit(5000)
def biseccion(y,err):
    if y >=0:
        return biseccion_aux(y,err,0,y,y/2)
    else:
        return "Error: y debe ser real prositivo"


def biseccion_aux(y,err,li,ls, aprox):
    if abs(y - aprox **2)<=err:
        return aprox
    if aprox ** 2 >y :
        return biseccion_aux(y,err,li,aprox,(li +ls)/2)
    else:
        return biseccion_aux(y,err,aprox,ls,(li+ls)/2)