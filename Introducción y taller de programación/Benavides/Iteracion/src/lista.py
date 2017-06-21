'''
Created on 16/05/2013

@author: Pedro
'''
def largo_lista(lista):
    lista=list(lista)
    cont=0
    while lista!=[]:
        cont+=1
        lista=lista[1:]
    return cont

def largo_listafor(lista):
    lista=list(lista)
    cont=0
    for n in lista:
        cont+=1
    return cont

def pares_lista(lista):
    lista=list(lista)
    cont=0
    for n in lista:
        if n%2==0:
            cont+=1
    return cont