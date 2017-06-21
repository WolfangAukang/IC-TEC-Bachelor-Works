'''
Created on 14/03/2013

@author: Leeecher
'''
def Pedirdatos():
    a=input('Digite numero 1')
    b=input('Digite numero 2')
    NumMayor=mayor(a,b)
    if NumMayor==0:
        print "No hay mayor"
    else:
        print "El mayor es", NumMayor

def mayor(num1,num2):
    if num1==num2:
        return 0
    elif num1>num2:
        return num1
    else:
        return num2