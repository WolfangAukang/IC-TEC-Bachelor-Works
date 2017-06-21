from __future__ import division
'''
Created on 16/05/2013

@author: Pedro
'''
import sys
sys.setrecursionlimit(5000)
def newton_raphson_roy(y,err):
    if y >=0:
        return newton_raphson_aux(y,err,0,y,1)
    else:
        return "Numero invalido"


def newton_raphson_aux(y,err,li,ls, aprox):
    if abs(y - aprox **2)<=err:
        return aprox
    if aprox ** 2 >y :
        return newton_raphson_aux(y,err,li,aprox,1/2*(aprox+(y/aprox)))
    else:
        return newton_raphson_aux(y,err,aprox,ls,1/2*(aprox+(y/aprox)))

def newton_raph(y,err):
    if y >=0:
        return newton_aux(y,err,1)
    else:
        return "Numero invalido"


def newton_aux(y,err,aprox):
    if abs(y - aprox **2)<=err:
        return aprox
    else:
        return newton_aux(y,err,1/2*(aprox+y/aprox))
