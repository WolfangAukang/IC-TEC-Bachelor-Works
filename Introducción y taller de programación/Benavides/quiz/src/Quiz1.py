import math
'''
Created on 02/05/2013

@author: Pedro
'''
'''1. Entrada: Un numero el cual se le contara sus digitos
Salida: Un numero que indica la cantidad de digitos que contiene el numero de entrada 
Restriccion: Ninguna'''
def cantdigitos():
    condicion=False
    while not condicion:
        try:
            num=input("Favor insertar numero: ")
            condicion=True
        except:
            return "Error"
    numAux=num
    if numAux<0:
        numAux=abs(numAux)
    if isinstance(numAux,float):
        numAux=math.trunc(numAux)
    return cantdigitosaux(numAux, 0)

def cantdigitosaux(num, factor):
    if num==0:
        return factor
    else:
        return cantdigitosaux(num/10, factor+1)

'''2. Entrada: Un numero el cual se le buscaran sus digitos impares
Salida: Un numero compuesto por todos los digitos impares del numero insertado 
Restriccion: Ninguna'''    
def digitosimpar():
    condicion=False
    while not condicion:
        try:
            num=input("Favor insertar numero: ")
            condicion=True
        except:
            return "Error"
    numAux=num
    if numAux<0:
        numAux=abs(numAux)
    if isinstance(numAux,float):
        numAux=math.trunc(numAux)
    factor=0
    forma=0
    return digitosimparaux(numAux, forma, factor)

def digitosimparaux(num, forma, factor):
    if num==0:
        return forma
    if num%2==0:
        return digitosimparaux(num/10, forma, factor)
    else:
        return digitosimparaux(num/10, forma+num%10*10**factor, factor+1)

'''3. Entrada: Un numero el cual se le indicara el factorial
Salida: Un numero que indica el factorial del numero insertado 
Restriccion: Ninguna'''
def factorial():
    condicion=False
    while not condicion:
        try:
            num=input("Favor insertar numero: ")
            condicion=True
        except:
            return "Error"
    numAux=num
    if numAux<0:
        numAux=abs(numAux)
    if isinstance(numAux,float):
        numAux=math.trunc(numAux)
    return factorialaux(numAux, 1)

def factorialaux(num, factor):
    if num==0:
        return factor
    else:
        return factorialaux(num-1, num*factor)

'''4. Entrada: Un numero el cual se le sacara su fibonnacci
Salida: Un numero que indica el fibonacci del numero insertado 
Restriccion: Ninguna'''
def fibonacci():
    condicion=False
    while not condicion:
        try:
            num=input("Favor insertar numero: ")
            condicion=True
        except:
            return "Error"
    numAux=num
    if numAux==0:
        return 1
    if isinstance(numAux,int):
        if numAux>0:
            return fibonacciaux(numAux, 1, 1, 1)
        else:
            return "Numero debe ser mayor a 0"
    else:
        return "Numero debe ser entero"
    
def fibonacciaux(num, contador, f1, f2):
    if num==contador:
        return f2
    else:
        return fibonacciaux(num, contador+1, f2, f1+f2)
    
'''5. Entrada: Dos numeros indicando el inicio y fin de la sumatoria
Salida: Un numero que indica el resultado de la sumatoria del numero insertado 
Restriccion: Ninguna'''
def sumatoria(inicio, fin):
    if inicio==fin:
        return fin
    else:
        return sumatoriaaux(inicio, fin, 0)
    
def sumatoriaaux(num1, num2, result):
    if num1==num2:
        return result+num2
    else:
        return sumatoriaaux(num1+1, num2, result+num1)

'''6. Entrada: Un numero en binario al cual se convertiraen decimal
Salida: Un numero decimal, que es la conversion del numero insertado 
Restriccion: Ninguna'''
def bin_dec(num):
    if comprobacion(num):
        return bin_decaux(num, 0, 0)
    else:
        return 'error'

def comprobacion(num):
    if num==0:
        return True
    if num%10 in [0,1]:
        return comprobacion(num/10)
    else:
        return False

def bin_decaux(num, factor, result):
    if num==0:
        return result
    else:
        return bin_decaux(num/10, factor+1, result+num%10*2**factor)

'''7. Entrada: Un numero al cual se convertira en binario
Salida: Un numero en binario, la conversion del numero insertado 
Restriccion: Ninguna'''
def dec_bin():
    condicion=False
    while not condicion:
        try:
            num=input("Favor insertar numero: ")
            condicion=True
        except:
            return "Error"
    numAux=num
    if numAux<0:
        numAux=abs(numAux)
    if isinstance(numAux,float):
        numAux=math.trunc(numAux)
    return dec_binaux(numAux, 0, 0)

def dec_binaux(num, result, factor):
    if num==0:
        return result
    else:
        return dec_binaux(num//2,result+num%2*10**factor, factor+1)

'''8. Entrada: Un numero y una lista, donde numero multilpicara a todos los elementos de una lista 
Salida: Una lista con el resultado de las multiplicaciones del primer numero con la lista anterior
Restriccion: Ninguna'''
def multi():
    condicion=False
    while not condicion:
        try:
            lista=input("Favor insertar lista: ")
            condicion=True
        except:
            return "Error"
    lista=list(lista)
    if lista==[]:
        return 0
    else:
        return multiaux(lista, 1)

def multiaux(lista, result):
    if lista==[]:
        return result
    else:
        return multiaux(lista[1:], result*lista[0])

'''9. Entrada: Una lista la cual se separan sus numeros pares e impares 
Salida: Una lista con dos sublistas, una indicando los numeros pares y otra con los numeros impares
Restriccion: Ninguna'''
def parimparlistas():
    condicion=False
    while not condicion:
        try:
            lista=input("Favor insertar lista: ")
            lista=list(lista)
            condicion=True
        except:
            return "Error"
    return parimparlistasaux(lista, [], [])

def parimparlistasaux(lista, par, impar):
    if lista==[]:
        return par,impar
    if lista[0]%2==0:
        return parimparlistasaux(lista[1:], par+[lista[0]], impar)
    else:
        return parimparlistasaux(lista[1:], par, impar+[lista[0]])