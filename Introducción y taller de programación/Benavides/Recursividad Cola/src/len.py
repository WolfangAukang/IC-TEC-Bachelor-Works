'''
Created on 25/04/2013

@author: Leeecher
'''
def len(lista):
    if lista==[]:
        return "error"
    else:
        valor=0
        return lenaux(lista, valor)

def lenaux(lista, valor):
    if lista==[]:
        return valor
    else:
        return lenaux(lista[1:], valor+1)