def factor(num, fac=0):
    if num<10**fac:
        return fac
    else:
        return factor(num,fac+1)
#Funcion de factorial, crucial para la formula del calculo de combinaciones
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
#Funcion de la formula del calculo de combinaciones, la cual nos ayuda a insertar los numeros correspondientes del escalon del triangulo de Pascal
def calcPascal(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))
#Funcion principal del triangulo de Pascal, orientado a imprimir el triangulo de acuerdo a los datos insertados por el usuario
def trianguloPascal(numact, posact, poslleg, impr):
    if numact==poslleg:
        return impr*10+1
    else:
        if numact==posact:
            print impr*10+1
            return trianguloPascal(0, posact+1, poslleg, 0)
        else:
            return trianguloPascal(numact+1, posact, poslleg, impr*10**factor(calcPascal(posact,numact),0)+calcPascal(posact,numact))
