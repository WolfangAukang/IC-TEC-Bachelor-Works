'''
Created on 14/03/2013

@author: Leeecher
'''
def digitosprofe(numero):
    if numero < 10:
        return 1
    else:
        return 1 + digitosprofe(numero/10)
    
def digitoslibro(numero):
    if numero == 0:
        return 0
    else:
        return 1 + digitoslibro(numero/10)