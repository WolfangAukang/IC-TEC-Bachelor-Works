'''
Created on 25/04/2013

@author: Leeecher
'''
def mayor(lista):
    if lista==[]:
        return "Error, lista esta vacia"
    else:
        return mayor_aux(lista)

def mayor_aux(lista):
    if lista [1:]==[]:
        return lista[0]
    else:return compara(lista[0], mayor_aux(lista[1:]))
    
def compara(x, y):
    if x>y:
        return x
    else:
        return y