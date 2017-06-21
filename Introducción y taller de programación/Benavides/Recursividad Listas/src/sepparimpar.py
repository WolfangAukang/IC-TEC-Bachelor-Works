'''
Created on 25/04/2013

@author: Leeecher
'''
def separacion():
    condicion=False
    while not condicion:
        try:
            lista=list(input("Favor insertar lista de numeros: "))
            condicion=True
        except:
            return "Error"
    if lista!=[]:
        return separacionaux(lista, [], [])
    else:
        return "Error"

def separacionaux(lista, par, impar):
    if lista==[]:
        return [[], []]
    else:
        par=lambda x:x%2==0
        impar=lambda x:x%2!=0
        return (indicador(lista, par))+(indicador(lista,impar))
    
def indicador(lista, func):
    if lista==[]:
        return []
    elif func(lista[0]):
        return [lista[0]]+indicador(lista[1:], func)
    else:
        return indicador(lista[1:], func)