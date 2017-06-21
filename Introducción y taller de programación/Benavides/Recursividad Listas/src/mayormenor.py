'''
Created on 25/04/2013

@author: Leeecher
'''
def mayormenor():
    condicion=False
    while not condicion:
        try:
            lista=list(input("Favor insertar lista de numeros: "))
            funcion=input("Deseas buscar el mayor (0) o menor (1) numero?: ")
            if funcion not in [0,1]:
                return "Error"
            else:
                condicion=True
        except:
            return "Error"
    if lista!=[]:
        if funcion==0:
            return mayoraux(lista[1:], lista[0])
        else:
            return menoraux(lista[1:], lista[0])
    else:
        return "Error"

def mayoraux(lista, num):
    if lista==[]:
        return num
    if num>lista[0]:
        return mayoraux(lista[1:], num)
    else:
        return mayoraux(lista[1:],lista[0])

def menoraux(lista, num):
    if lista==[]:
        return num
    if num<lista[0]:
        return menoraux(lista[1:], num)
    else:
        return menoraux(lista[1:],lista[0])