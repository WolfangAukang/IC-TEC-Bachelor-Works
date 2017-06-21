'''
Created on 14/03/2013

@author: Leeecher
'''
'''Entrada: Un numero natural
Salida: Un booleano, indicando False si no tiene ceros y True si tene ceros
Restriccion: El numero sea real
'''
def ceros(num):
    if num<10:
        return False
    elif num%10==0:
        return True
    else:
        return ceros(num/10)

def cerosaux(num):
    len=digitosAux(numero)
    numero-numero
    for i in len:
        numero/=10
    if numero==0:
        return True
    else:
        return ceros(num)