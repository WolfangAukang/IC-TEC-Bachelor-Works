'''
Created on 25/04/2013

@author: Leeecher
'''
def parlista():
    condicion=False
    while not condicion:
        try:
            lista=list(input("Favor insertar lista de numeros: "))
            condicion=True
        except:
            return "Error"
    if lista!=[]:
        return parlistaaux(lista)
    else:
        return "Error"
        
def parlistaaux(list):
    if list==[]:
        return 0
    if list[0]%2==0:
        return 1+parlistaaux(list[1:])
    else:
        return parlistaaux(list[1:])

def cantparlista():
    condicion=False
    while not condicion:
        try:
            lista=list(input("Favor insertar lista de numeros: "))
            condicion=True
        except:
            return "Error"
    if lista!=[]:
        return cantparlistaaux(lista)
    else:
        return "Error"
        
def cantparlistaaux(lista):
    if lista==[]:
        return []
    if lista[0]%2==0:
        return [lista[0]]+cantparlistaaux(lista[1:])
    else:
        return cantparlistaaux(lista[1:])
    
def ifparlista():
    condicion=False
    while not condicion:
        try:
            lista=list(input("Favor insertar lista de numeros: "))
            condicion=True
        except:
            return "Error"
    if lista!=[]:
        return ifparlistaaux(lista)
    else:
        return "Error"
        
def ifparlistaaux(lista):
    if lista==[]:
        return False
    if lista[0]%2==0:
        return True
    else:
        return ifparlistaaux(lista[1:])

def todosparlista():
    condicion=False
    while not condicion:
        try:
            lista=list(input("Favor insertar lista de numeros: "))
            condicion=True
        except:
            return "Error"
    if lista!=[]:
        return todosparlistaaux(lista)
    else:
        return "Error"
        
def todosparlistaaux(lista):
    if lista==[]:
        return True
    if lista[0]%2==0:
        return todosparlistaaux(lista[1:])
    else:
        return False