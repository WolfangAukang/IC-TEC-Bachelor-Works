'''
Created on 14/03/2013

@author: Leeecher
'''
'''Entrada: Un numero entero
Salida: Los digitos, del ultimo al primero, colocados por renglon
Restriccion: que no sea negativo
'''
def descompone(numero):
    while numero>=10:
        digito=numero%10
        numero/=10
        print digito
    print numero