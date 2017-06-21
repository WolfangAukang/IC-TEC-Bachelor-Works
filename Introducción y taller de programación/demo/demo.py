from __future__ import division
import math
'''
Created on Mar 7, 2013

@author: rajcbc

entradas
salidas
restricciones
'''
def CelFah(celsius):
    fahr=9/5*celsius+32
    return fahr

def FahCel(fahren):
    cel=(fahren-32)/(9/5)
    return cel

def EcuCuadratica(a,b,c):
    denominador=2*a
    discriminante=b**2-(4*a*c)
    if discriminante <=0:
        print ("La solucion implica numeros complejos...")
    else:
        x1=((-b)+math.sqrt(discriminante))/denominador
        x2=((-b)-math.sqrt(discriminante))/denominador
    return (x1,x2)

def imprimecondicion():
    nota=input("digite una nota de un estudiante para saber su condicion... ")
    print "la condicion del estudiante es", condicion(nota)
    
def condicion(nota=0):
    if nota>=90:
        return "excelente..."
    else:
        if nota>=70:
            return "bueno... "
        else:
            if nota>=60:
                return "regular... "
            else:
                if nota>=30:
                    return "malo... "
                else:
                    return "pesimo... "

def condicion1(nota):
    if nota>=90:
        return "excelente..."
    elif nota>=70:
        return "bueno... "
    elif nota>=60:
        return "regular... "
    elif nota>=30:
        return "malo... "
    else:
        return "pesimo... "
