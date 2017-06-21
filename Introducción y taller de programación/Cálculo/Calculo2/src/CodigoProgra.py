from __future__ import division
'''
Created on 23/09/2013

@author: Pedro
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def calculo(n, res=0):
    if n==0:
        res+=1
        return "El resultado es igual a "+str(res)
    else:
        return calculo(n-1, res+(1/factorial(n)))

def introduccion():
    n=input("Favor insertar numero: ")
    if n<=0:
        return "Error, datos invalidos"
    else:
        return calculo(n)