# -*- coding: cp1252 -*-
from __future__ import division
'''
Created on 13/08/2013

@author: Pedro
'''
import math
import sys
sys.setrecursionlimit(1000000)

def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def primo(n):
    if n==2:
        return True
    elif n%2==0:
        return False
    else:
        return primoaux(n, 2)

def primoaux(n, div):
    if div>(n//2):
        return True
    else:
        if n%div==0:
            return False
        else:
            return primoaux(n, div+1)

'''Ejercicio 1
Entrada: Un numero al cual se revisara si es capicua
Salida: Un booleano indicando si es verdadero o falso
Restriccion: Ninguna'''
def capicua(num, factor):
    if num<10**factor:
        return capicuares(num, capicuaaux(factor-1, num, 0))
    else:
        return capicua(num, factor+1)

def capicuaaux(factor, num, inv):
    if num==0:
        return inv
    else:
        return capicuaaux(factor-1, num//10, inv+(num%10)*10**factor)

def capicuares(num, inv):
    if num==inv:
        return True
    else:
        return False
    
'''Ejercicio 2
Entrada: Un numero el cual sera analizado a ver si es perfectto
Salida: Un booleano indicando si es verdadero o falso
Restriccion: Ninguna'''
def perfecto(num,div,perf):
    if div==0:
        return perfectores(num,perf)
    else:
        if num%div==0:
            return perfecto(num, div-1, perf+div)
        else:
            return perfecto(num, div-1, perf)
    
def perfectores(num,perf):
    if num==perf:
        return True
    else:
        return False
    
'''Ejercicio 3
Entrada: Dos numeros a los cuales se les calculara el mcd
Salida: El maximo comun divisor entre los dos primeros numeros
Restriccion: Ninguna'''
def mcd(num1, num2):
    mini=abs(num1)
    if mini>abs(num2):
        mini=abs(num2)
    return mcdaux(abs(num1),abs(num2),2,1,mini//2)

def mcdaux(num1,num2,div,res,maxdiv):
    if div==maxdiv:
        return res
    else:
        if num1%div==0 and num2%div==0:
            return mcdaux(num1/div,num2/div,div,res*div, maxdiv)
        else:
            return mcdaux(num1,num2,div+1,res,maxdiv)

'''Ejercicio 4
Entrada: Un numero correspondiente a la cantidad de filas de la piramide
Salida: Una piramide
Restriccion: Ninguna'''
def triangulo(num):
    num=abs(num)
    return trianguloaux(num,1,1,"")

def trianguloaux(totalfil,filac,numact,triang):
    if totalfil==filac and numact==0:
        return triang
    else:
        if numact>0:
            return trianguloaux(totalfil,filac,numact-1,triang+str(numact))
        else:
            return trianguloaux(totalfil,filac+1,filac+1,triang+"\n")
        
'''Ejercicio 5
Entrada: Dos numeros: El primero es el numero a modificar y el segundo es el digito que se retirara al primer numero
Salida: El primer numero sin los digitos que corresponda al segundo numero
Restriccion: Si el primer numero es negativo y si el digito es mayor a 10 o menor a 0, el programa lanzara un mensaje de error.'''
def meQuitaron(num, digito):
    if num<0:
        num=abs(num)
    if 0>digito or digito>9:
        return "Error, datos erroneos"
    else:
        return meQuitaronaux(num, digito, 0, 0)

def meQuitaronaux(num, digito, factor, nuevo):
    if num==0:
        return nuevo
    else:
        if num%10==digito:
            return meQuitaronaux(num//10, digito, factor, nuevo)
        else:
            return meQuitaronaux(num//10, digito, factor+1, nuevo+((num%10)*10**factor))

'''Ejercicio 6
Entrada: Un numero, el cual se analizara si es libre de cuadrado
Salida: Un booleano indicando si es verdadero o falso
Restriccion: Ninguna'''
def libreDeCuadrados(num,div):
    if div>num:
        return True
    else:
        if num%div==0 and math.log(div,2)%1==0:
            return False
        else:
            return libreDeCuadrados(num,div+1)

'''Ejercicio 7
Entrada: un numero el cual sera modificado de acuerdo a los digitos en las posiciones pares.
Salida: El numero insertado, pero sin los digitos de las posiciones pares.
Restriccion: Ninguna'''
def numeroDePosPares(num, pos, factor, nuevo):
    if num==0:
        return nuevo
    else:
        if pos%2!=0:
            return numeroDePosPares(num//10,pos+1,factor,nuevo)
        else:
            return numeroDePosPares(num//10,pos+1,factor+1,nuevo+(num%10)*(10**factor))

'''Ejercicio 8
Entrada: Un numero el cual se analizara si es cuadrado perfecto
Salida: Un booleano indicando si es verdadero o falso
Restriccion: Ninguna'''
def cuadradoPerfecto(num, base):
    if num<base**2:
        return False
    else:
        if num==base**2:
            return True
        else:
            return cuadradoPerfecto(num,base+1)

'''Ejercicio 9
Entrada: Un numero el cual se le analizara si es semiprimo
Salida: Un booleano indicando si es verdadero o falso
Restriccion: Si es numero no es mayor a 3, se imprimira mensaje de error'''
def semiPrimo(num):
    if abs(num)<4:
        return "Error, datos erroneos"
    else:
        return semiPrimoaux(abs(num),0,0,2)
    
def semiPrimoaux(num,factor1,factor2,div):
    if div>num:
        return False
    if num%div==0 and factor1!=0:
        if num//div==1:
            return semiPrimores(primo(factor1),primo(div))
        else:
            return False
    else:
        if num%div==0 and factor1==0:
            return semiPrimoaux(num//div,div,factor2,div)
        else:
            return semiPrimoaux(num,factor1,factor2,div+1)

def semiPrimores(factor1,factor2):
    if factor1 and factor2:
        return True
    else:
        return False

'''Ejercicio 10
Entrada: Dos numeros naturales, los cuales se les calculara la funcion de Ackermann
Salida: Un numero natural
Restriccion: Ninguna'''
def ackermann(m,n):
    if m==0:
        return n+1
    else:
        if m>0 and n==0:
            return ackermann(m-1,1)
        else:
            return ackermann(m-1,ackermann(m,n-1))

'''Hormiguitas
Entrada: Un numero indicando el ciclo deseado de reproduccion
Salida: Un numero indicando la cantidad de hormigas reproducidas
Restriccion: Ninguna'''
def hormiguitas(num,hormiguita,cont):
    if num==cont:
        return hormiguita
    else:
        return hormiguitas(num,(hormiguita//2*3),cont+1)
    
'''Practica Diego Mora (A.K.A. Kill Ricardo, now!)
Ejercicio 1
Entrada: Un numero el cual se analizara la potencia positiva mas cercana
Salida: La potencia de 10 mas cercana
Restriccion: Ninguna'''
def diezcercano(num):
    if num<0:
        return "Error, datos invalidos"
    else:
        if math.log10(num)%1==0:
            return num
        else:
            return diezcercanoaux(abs(num), 10**(factor(abs(num),0)-1), 10**factor(abs(num),0))

def diezcercanoaux(num, factorbajo, factoralto):
    if abs(num-factoralto)>abs(num-factorbajo) or abs(num-factoralto)==abs(num-factorbajo):
        return factorbajo
    else:
        return factoralto
    
def factor(num, fac):
    if num<10**fac:
        return fac
    else:
        return factor(num,fac+1)

'''Ejercicio 2
Entrada: Un numero el cual se le contara sus digitos antes y despues del punto flotante.
Salida: Un numero indicando la cantidad de digitos disponibles
Restriccion: Ninguna'''
def cuentadigitos(num):
    if num==0:
        return 0
    else:
        return 1+cuentadigitos(num//10)

'''Ejercicio 3
Entrada: Un numero el cual se analizara sus digitos distintos
Salida: Un numero indicando la cantidad de digitos distintos que contiene
Restriccion: Ninguna'''
def cuentadigitosdis(num,dig):
    if num<10 and num>=0:
        return 1
    else:
        return cuentadigitosdisaux(abs(num),0)

def cuentadigitosdisaux(num,dig):
    if num==0:
        return dig
    else:
        return compar(abs(num%10),num//10,num,dig)

def compar(numcom, numana, numor, dig):
    if numana==0:
        return cuentadigitosdisaux(numor//10, dig+1)
    else:
        if numcom==(numana%10):
            return cuentadigitosdisaux(numor//10, dig)
        else:
            return compar(numcom,numana//10,numor, dig)

'''Ejercicio 4
Entrada: Un numero el cualse determinara si es palindromo
Salida: Un booleano indicando si verdadero o falso
Restriccion: Ninguna'''
def palindromo(num,inv,numinm):
    if num==0:
        return palindromores(numinm, inv)
    else:
        return palindromo(num//10,(inv*10)+(num%10),numinm)

def palindromores(num,inv):
    if num==inv:
        return True
    else:
        return False

'''Ejercicio 5
Entrada: dos numeros los cuales se hara una division por medio de sumas y restas
Salida: Un numero, resultado de la division truncada
Restriccion: Ninguna'''
def divtrunc(num1,num2):
    if num1<num2:
        return 0
    else:
        return 1+divtrunc(num1-num2,num2)

'''Ejercicio 6
Entrada: Dos numeros, un numero de consulta y el otro un digito el cual debe compararse en el numero de consulta
Salida: Un numero indicando la posicion del digito en el numero de consulta (leyendose de derecha a izquierda)
Restriccion: Si el digito es mayor a 9 o menor a 0, se retornamra mensaje de error'''
def OcurreEn(num,dig,pos):
    if num==0:
        return 0
    else:
        if num%10==dig:
            return pos
        else:
            return OcurreEn(num//10,dig,pos+1)

'''Ejercicio 7
Entrada: Dos numeros, un numero de consulta y el otro un digito el cual debe compararse en el numero de consulta
Salida: Un numero indicando la posicion del digito en el numero de consulta (leyendose de izquierda a derecha)
Restriccion: Si el digito es mayor a 9 o menor a 0, se retornamra mensaje de error'''
def OcurreEn2(num,dig,factor):
    if num<10**factor:
        return OcurreEn2aux(num,dig,factor)
    else:
        return OcurreEn2(num,dig,factor+1)

def OcurreEn2aux(num,dig,pos):
    if num==0:
        return 0
    else:
        if num%10==dig:
            return pos
        else:
            return OcurreEn2aux(num//10,dig,pos-1)

'''Ejercicio 8
Entrada: Un numero el cual se analizara sus digitos
Salida: Un numero indicando el digito mas alto
Restriccion: ninguna'''
def DigitAlto(num):
    if num<10:
        return num
    else:
        return DigitAltoaux(num//10,num%10,num)

def DigitAltoaux(num,dig,numinm):
    if dig<num%10:
        return DigitAlto(numinm//10)
    else:
        if num==0:
            return dig
        else:
            return DigitAltoaux(num//10,dig,numinm)

'''Ejercicio 9
Entrada: Un numero el cual se le analizara sus digitos
Salida: Un numero indicando el digito que sale maas veces
Restriccion: Ninguna'''
def MasDigito(num,digiactu,candigiactu,digigana,candigigana,numinm):
    if num==0:
        return MasDigitores(candigiactu,digigana,candigigana)
    else:
        return MasDigitoaux(num,num%10,0,digigana,candigigana,num)

def MasDigitoaux(num,digiactu,candigiactu,digigana,candigigana,numinm):
    if num==0:
        if candigiactu>candigigana:
            candigigana=candigiactu
            digigana=digiactu
            return MasDigito(numinm//10,digiactu,candigiactu,digigana,candigigana,numinm)
        else:
            if candigiactu==candigigana:
                digigana="Empate"
                return MasDigito(numinm//10,digiactu,candigiactu,digigana,candigigana,numinm)
            else:
                return MasDigito(numinm//10,digiactu,candigiactu,digigana,candigigana,numinm)
    else:
        if num%10==digiactu:
            return MasDigitoaux(num//10,digiactu,candigiactu+1,digigana,candigigana,numinm)
        else:
            return MasDigitoaux(num//10,digiactu,candigiactu,digigana,candigigana,numinm)

def MasDigitores(candigiactu,digigana,candigigana):
    if digigana=="Empate":
        return "Nadie ocurre mas veces"
    else:
        return digigana

'''Ejercicio 10
Entrada: Dos numeros, uno que se modificara y otro que sera usado como base para la suma
Salida: Un numevo numero, que corresponde a la suma de los digitos del primero mas el segundo
Restriccion: Ninguna'''
def digisuma(num,dig):
    if num==0:
        return 0
    else:
        return digisumaaux(invertirnum(num,0),dig,0)

def invertirnum(num,inv):
    if num==0:
        return inv
    else:
        return invertirnum(num//10,((inv*10)+num%10))

def digisumaaux(num,dig,nuev):
    if num==0:
        return nuev
    else:
        if (num%10+dig)>10:
            return digisumaaux(num//10,dig,((nuev%10)*10+((num%10+dig)%10)))
        else:
            return digisumaaux(num//10,dig,((nuev)*10+(num%10+dig)))

    
'''Ejercicio 31
Entrada: Un numero indicando los ciclos a los que debe llegar el numero
Salida: Resultado del acertijo del rey
Restriccion: Ninguna'''
def ajedrezrey(n=0):
    if n==64:
        return 0
    else:
        return 2**n+ajedrezrey(n+1)

'''Examen 3'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def calcPascal(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))

def trianguloPascal(na,pa,pll,res):
    if na==pll:
        return res*10+1
    else:
        if na==pa:
            print res*10+1
            return trianguloPascal(0,pa+1,pll,0)
        else:
            return trianguloPascal(na+1,pa,pll,(res*10**factor(calcPascal(pa,na),0))+calcPascal(pa,na))
        
'''Recursion hileras'''
def conVocales(hilera, n=0):
    if len(hilera)==n:
        return False
    else:
        if hilera[n].lower() in "aeiouáéíóú":
            return True
        else:
            return conVocales(hilera, n+1)
    
def conVocales2(hilera):
    if hilera=="":
        return False
    else:
        if hilera[0].lower() in "aeiouáéíóú":
            return True
        else:
            return conVocales2(hilera[1:])

def cuentVocales(hilera):
    if hilera=="":
        return 0
    else:
        if hilera[0].lower() in "aeiouáéíóú":
            return 1+cuentVocales(hilera[1:])
        else:
            return cuentVocales(hilera[1:])
    
def eliminarVocales(hilera):
    if hilera=="":
        return ""
    else:
        if hilera[0].lower() in "aeiou":
            return eliminarVocales(hilera[1:])
        else:
            return hilera[0]+eliminarVocales(hilera[1:])

'''Programa para calcula cual palabra es mayor
Entrada: Cinco cadenas las cuales seran comparadas
Salida: Una lista indicando el orden de las palabras
Restriccion: Ninguna'''
def comparapalabras(p1,p2,p3):
    universo="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    pn1=universo.find(p1[0])
    pn2=universo.find(p2[0])
    pn3=universo.find(p3[0])
    menor=pn1