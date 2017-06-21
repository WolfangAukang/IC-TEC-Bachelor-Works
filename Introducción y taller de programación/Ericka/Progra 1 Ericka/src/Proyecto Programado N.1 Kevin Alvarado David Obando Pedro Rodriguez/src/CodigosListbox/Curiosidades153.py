from math import sqrt
#---------------------------------------------------------------
def cubos153(lista1=digitosdel153(), lista2=[]):
    if lista1==[]:
        return str(sum(lista2))+" es igual a la suma de los cubos de sus dígitos:\n1exp(3) + 5exp(3) + 3exp(3)=\n 1 + 125 + 27="+str(sum(lista2))
    else:    
        return cubos153(lista1[:-1],lista2 + [lista1[-1]**3])
#---------------------------------------------------------------
def digitosdel153(n=153,digitos153=[]):
    if n<=0:
        return digitos153
    else:
        return digitosdel153(n//10,[n%10] + digitos153)
#---------------------------------------------------------------    
def sumadigitos153(lista1=digitosdel153(),lista2=[]):
    if lista1==[]:
        num=sum(lista2)
        if sqrt(num)==int(sqrt(num)) and isinstance(sqrt(num),float):
            return "La suma de los digitos de 153 es: " +  str(num) + " y el " + str(num) + " es un numero cuadrado perfecto" 
    else:
        return sumadigitos153(lista1[:-1],lista2 + [lista1[-1]])
#---------------------------------------------------------------
def sumaenteros153(n=1):
    if n==17:
        return n 
    else:
        return n + sumaenteros153(n+1)
#---------------------------------------------------------------
def sumaenteros351(n=1):
    if n==26:
        return n
    else:
        return n + sumaenteros351(n+1)
#---------------------------------------------------------------
def numerotriangular153(n=1):    
    if sumaenteros153()==153 and sumaenteros351()==351:
        return "La suma de los enteros del 1 al 17 es: 153 y del 1 al 26 es: 351"
    else:
        pass
