'''
Created on 25/04/2013

@author: Leeecher
'''
'''Entrada: Una lista la cual se contara sus elementos
Salida: Un numero indicando la cantidad de elementos en la lista
Restriccion: Ninguna'''
def lenlista():
    condicion=False
    while not condicion:
        try:
            lista=input("Favor insertar lista de numeros: ")
            condicion=True
        except:
            return "Error"
    lista=list(lista)
    return lenlistaaux(lista)

def lenlistaaux(list):
    if list==[]:
        return 0
    else:
        return 1+lennumericolistaaux(list[1:])   