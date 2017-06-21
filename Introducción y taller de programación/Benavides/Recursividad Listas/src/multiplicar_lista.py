'''
Created on 25/04/2013

@author: Leeecher
'''
'''Entrada: Una lista la cual se multiplicara sus elementos entre si
Salida: Un numero indicando el resultado de la multiplicacion
Restriccion: Ninguna'''
def multiplicacionlista():
    condicion=False
    while not condicion:
        try:
            lista=list(input("Favor insertar lista de numeros: "))
            condicion=True
        except:
            return "Error"
    if lista!=[]:
        return multiplicacionlistaaux(lista)
    else:
        return "Error"

def multiplicacionlistaaux(lista):
    if lista==[]:
        return 1
    else:
        return lista[0]*multiplicacionlistaaux(lista[1:])