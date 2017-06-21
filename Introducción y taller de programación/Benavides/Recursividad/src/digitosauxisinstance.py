'''
Created on 14/03/2013

@author: Leeecher
'''
def digito(num):
    if isinstance(num, float):
        num=int(num)
    if num<0:
        num=abs(num)
    if num<10:
        return 1
    else:
        return digitosprofe(num)
    
def digitosprofe(num):
    if num < 10:
        return 1
    else:
        return 1 + digitosprofe(num/10)
    
def digitos_aux(num):
    if num == 0:
        return 0
    else:
        return 1 +digitos_aux(num//10)