'''
Created on 25/04/2013

@author: Leeecher
'''
def elimina():
    condicion=False
    while not condicion:
        try:
            numero=input("Favor insertar posicion para eliminar: ")
            lista=list(input("Favor insertar lista de numeros: "))
            condicion=True
        except:
            return "Error"
    if lista!=[] and numero<len(lista):
        return eliminaaux(numero, lista)
    else:
        return "Error"

def eliminaaux(numero, lista):
    if lista==[]:
        return []
    elif lista[0]==numero:
        return lista[1:]
    else:
        return [lista[0]]+eliminaaux(numero, lista[1:])