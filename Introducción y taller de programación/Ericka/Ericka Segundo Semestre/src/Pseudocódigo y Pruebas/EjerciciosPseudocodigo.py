from __future__ import division
'''
Created on 11/08/2013

@author: Pedro
'''
import math

def menu():
    print "Menu:\n1. Menor numero\n2. Menor distancia\n3. Reloj\n4. Vuelto"
    opcion=0
    while opcion not in [1,2,3,4]:
        opcion=input("Cual opcion desea probar? ")
    if opcion==1:
        return menornum()
    elif opcion==2:
        return rectanumerica()
    elif opcion==3:
        return hora()
    elif opcion==4:
        return vuelto()
    
'''1. Programa que identifica el menor de tres numeros
Entrada: Tres numeros enteros
Salida: El menor de estos tres numeros
Restriccion: Ninguna'''
def menornum():
    a=input("Favor insertar el primer numero: ")
    b=input("Favor insertar el segundo numero: ")
    c=input("Favor insertar el tercer numero: ") 
    minus=a
    if minus>b:
        b=minus
    elif minus>c:
        c=minus
    print "El menor numero es", minus

'''2. Programa que identifica la menor distancia a un numero de referencia
Entrada: Cuatro numeros, uno de referencia y tres de comparacion
Salida: La respuesta indicando el(los) numero(s) mas cercanos al de referencia
Restriccion: Ninguna'''
def rectanumerica():
    #RECOLECCION DE DATOS
    ref=input("Favor insertar numero de referencia: ")
    a=input("Favor insertar primer numero: ")
    b=input("Favor insertar segundo numero: ")
    c=input("Favor insertar tercer numero: ")
    #CALCULO DE DISTANCIAS
    ad=abs(ref-a)
    bd=abs(ref-b)
    cd=abs(ref-c)
    #COMPARACION DE DISTANCIAS
    md=ad
    if ad>bd:
        md=bd
    elif ad>cd:
        md=cd
    #IMPRESION DE RESULTADOS
    if md==ad:
        print "El numero %d es mas cercano a %d" % (ref, a)
    if md==bd:
        print "El numero %d es mas cercano a %d" % (ref, b)
    if md==cd:
        print "El numero %d es mas cercano a %d" % (ref, c)

'''3. Programa para contar los minutos faltantes para terminar el dia
Entrada: Dos numeros, indicando la hora y los minutos
Salida: Un numero indicando la cantidad de minutos faltantes para terminar el dia
Restriccion: La hora debe estar entre el 0 y 23 y los minutos entre el 0 y 59'''
def hora():
    #CREAR VARIABLES PARA WHILE
    hora=-1
    minuto=-1
    while not 0<=hora<=23 or not 0<=minuto<=59:
    #PEDIR DATOS
        hora=input("Favor insertar la hora: ")
        minuto=input("Favor insertar los minutos: ")
    #OPERACIONES FUNDAMENTALES
    hora*=60
    mintot=1439-(hora+minuto)
    #IMPRESION RESULTADO
    print "Faltan %d minutos para terminar el dia" % (mintot)

'''4. Programa para indicar la forma de entregar el vuelto con las denominaciones de la moneda de Colon
Entrada: Dos numeros, que indican el precio y la cantidad de dinero con la cual ha pagado el cliente
Salida: Una lista que indica la manera en la cual se puede entregar el vuelto
Restriccion: Lo pagado por el cliente debe ser mayor al valor del producto'''
def vuelto():
    precio=1
    pago=0
    while precio>pago:
        precio=input("Valor total: ")
        pago=input("Con cuanto paga el cliente: ")
    vuelto=pago-precio
    print "El vuelto seria de %d. Se puede devolver de la siguiente manera:" % (vuelto)
    if math.trunc(vuelto/50000)>0:
        cincuemil=math.trunc(vuelto/50000)
        vuelto%=50000
        print "%d billete(s) de 50000 (cincuenta mil colones)" % (cincuemil)
    if math.trunc(vuelto/20000)>0:
        veintemil=math.trunc(vuelto/20000)
        vuelto%=20000
        print "%d billete(s) de 20000 (veinte mil colones)" % (veintemil)
    if math.trunc(vuelto/10000)>0:
        diezmil=math.trunc(vuelto/10000)
        vuelto%=10000
        print "%d billete(s) de 10000 (diez mil colones)" % (diezmil)
    if math.trunc(vuelto/5000)>0:
        cincomil=math.trunc(vuelto/5000)
        vuelto%=5000
        print "%d billete(s) de 5000 (cinco mil colones)" % (cincomil)
    if math.trunc(vuelto/2000)>0:
        dosmil=math.trunc(vuelto/2000)
        vuelto%=2000
        print "%d billete(s) de 2000 (dos mil colones)" % (dosmil)
    if math.trunc(vuelto/1000)>0:
        mil=math.trunc(vuelto/1000)
        vuelto%=1000
        print "%d billete(s) de 1000 (mil colones)" % (mil)
    if math.trunc(vuelto/500)>0:
        quin=math.trunc(vuelto/500)
        vuelto%=500
        print "%d moneda(s) de 500 (quinientos colones)" % (quin)
    if math.trunc(vuelto/100)>0:
        cien=math.trunc(vuelto/100)
        vuelto%=100
        print "%d moneda(s) de 100 (cien colones)" % (cien)
    if math.trunc(vuelto/50)>0:
        cincue=math.trunc(vuelto/50)
        vuelto%=50
        print "%d moneda(s) de 50 (cincuenta colones)" % (cincue)
    if math.trunc(vuelto/25)>0:
        veintcinc=math.trunc(vuelto/25)
        vuelto%=25
        print "%d moneda(s) de 25 (veinticinco colones)" % (veintcinc)
    if math.trunc(vuelto/10)>0:
        diez=math.trunc(vuelto/10)
        vuelto%=10
        print "%d moneda(s) de 10 (diez colones)" % (diez)
    if math.trunc(vuelto/5)>0:
        cinc=math.trunc(vuelto/5)
        vuelto%=5
        print "%d moneda(s) de 5 (cinco colones)" % (cinc)
    print "Gracias por su visita :)"