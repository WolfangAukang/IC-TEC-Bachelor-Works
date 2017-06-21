'''
Created on 14/03/2013

@author: Leeecher
'''
def digitoAux(numero):
    numero=abs(numero)
    if numero<10:
        return 1
    else:
        return digito(numero)
    
def digito(numero):
    if numero < 10:
        return 1
    else:
        return 1 + digito(numero/10)