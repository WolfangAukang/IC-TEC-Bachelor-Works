# -*- coding: cp1252 -*-
'''Estudiante: Pedro Rodriguez de Oliveira
Carnet:2013086585
Curso: Introduccion a la Programacion
Examen 2
II Semestre
2013'''

'''Ejercicio 1
Entrada: Una lista con elementos de igual tipo.
Salida: Un booleano indicando True si los elementos estan ordenados o False si sucede lo contrario
Restriccion:La lista no puede combinar elementos de diferentes tipos ni tener elementos similares juntos'''
#Algoritmo principal que determina si los elementos dentro de la lista son int o string
def estaOrdenada(L):
        if isinstance(L[0],int):
            return estaOrdenadaint(L)
        else:
            return estaOrdenadastr(L)

#Algoritmo para revisar orden de lista si lista contiene int's
def estaOrdenadaint(L):
    if len(L)==1:
        return True
    else:
        if L[0]<L[1]:
            return estaOrdenada(L[1:])
        else:
            return False

#Algoritmo para revisar orden de lista si lista contiene strings
def estaOrdenadastr(L,n=0):
    if len(L)==1:
        return True
    else:
        universo="aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ"
        if L[0]==L[1]:
            return estaOrdenadastr(L[1:],0)
        else:
            primer=universo.find(L[0][n])
            segundo=universo.find(L[1][n])
            if primer!=segundo:
                if primer<segundo:
                    return estaOrdenadastr(L[1:],0)
                else:
                    return False
            else:
                return estaOrdenadastr(L,n+1)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

'''Ejercicio 2
Entrada: Una lista a la cual se le uniran los elementos que sean iguales a sublistas
Salida:Una lista con todos los elementos de las sublistas incluidos dentro de la lista principal
Restriccion: Todos los elementos deben ser strings, sea dentro de la lista o sublistas'''
#Algoritmo principal, el cual lee el tipo del primer elemento en la lista y los une a una lista de respuesta
def desanida(L):
    if L==[]:
        return []
    else:
        if isinstance(L[0],list):
            return unelista(L[0])+desanida(L[1:])
        else:
            return [L[0]]+desanida(L[1:])

#Algoritmo que en caso de que la funcion principal haya leido una sublista, este la convierte en una lista extra para ser agregada a la lista principal 
def unelista(L):
    if L==[]:
        return L
    else:
        return [L[0]]+unelista(L[1:])

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
'''Ejercicio 3
Entrada: Cualquier elemento el cual se le contara la profundidad de sublistas que contiene dicho elemento
Salida: Si se mete una lista, se mostrará un "gráfico" mostrando sus listas y sublistas contenidas. En caso de ser otra cosa, se retorna comillas vacías
Restricción: Ninguna'''
#Algoritmo que confirma el tipo de lo insertado (string, entero, lista,...)
def mprof(L):
    if isinstance(L,list):
        return mprofaux(L)
    else:
        return " (No es una lista)"

#Algoritmo encargado de la impresión del gráfico y revisión de los elementos 
def mprofaux(L,res="["):
    if L==[]:
        return res+"]"
    else:
        if isinstance(L[0],list):
            if L[0]==[]:
                return mprofaux(L[1:],res+"[]")
            else:
                res=res+mprofaux(L[0],"[")
                return mprofaux(L[1:],res)
        else:
            return mprofaux(L[1:],res)


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
'''Ejercicio 4
Entrada: Una lista la cual se ordenara en sublistas, la cual en cada sublista habra un grupo ordenado ascendientemente
Salida: La lista con sublistas de grupos ordenados de manera ascendiente
Restriccion: Los elementos de la lista deben ser enteros'''

#Algoritmo principal, el cual crea las sublistas y compara los elementos (mayor o menor)
def natural(L):
    if isinstance(L[0],list):
        return L
    else:
        if isinstance(L[-1],list):
            if L[-1][-1]<L[0]:
                L[-1]=L[-1]+[L[0]]
                return natural(L[1:])
            else:
                return natural(L[1:]+[[L[0]]])
        else:
            if L[0]<L[1]:
                return natural(L[2:]+[[L[0]]+[L[1]]])
            else:
                return natural(L[2:]+[L[0]]+[L[1]])
            
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
'''Opcional Solo Palabras
Entrada: Una hilera (string) con palabras adentro
Salida: Una lista con las palabras incluidas dentro de la hilera insertada
Restriccion: Solo se puede insertar una hilera'''
def soloPalabras(Hilera):
    if isinstance(Hilera,str):
        return soloPalabrasaux(Hilera)
    else:
        return "Error, no es una hilera"
                             
def soloPalabrasaux(Hilera):
    n=False
    res=[]
    palab=""
    while not n:
        if Hilera=="":
            if palab!=0 and palab not in res and palab!="":
                res+=[palab]
            else:
                pass
            n=True
            return res
        else:
            universo="aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZ"
            if Hilera[0]==" " or Hilera[0] not in universo:
                if Hilera[0]==" ":
                    if palab not in res and palab!="":
                        res+=[palab]
                        palab=""
                        Hilera=Hilera[1:]
                    else:
                        palab=""
                        Hilera=Hilera[1:]
                else:
                    Hilera=Hilera[1:]
            else:
                palab=palab+Hilera[0]
                Hilera=Hilera[1:]

#-------------------------------------------------------
#ARCHIVO DE PRUEBA
#-------------------------------------------------------
def prueba():
    print("Pruebas con estaOrdenada(L)")
    print ("L=[Marquillos,Palito,Jota,Mermelada,Somnoliento,Zebra]")
    L=["Marquillos","Palito","Jota","Mermelada","Somnoliento","Zebra"]
    print estaOrdenada(L)
    print("L=[Manolo,Pringles,queso,Queso,Somnoliento,Torremolinos]")
    L=["Manolo","Pringles","queso","Queso","Somnoliento","Torremolinos"]
    print estaOrdenada(L)
    print("L=[1,2,3,4,5,6,7,89,54]")
    L=[1,2,3,4,5,6,7,89,54]
    print estaOrdenada(L)
    print("L=[2,4,6,8,12,15,18,34,67]")
    L=[2,4,6,8,12,15,18,34,67]
    print estaOrdenada(L)
    print("\nPruebas con desanida(L)")
    print("L=[1,2,3,[5,6,7], 4]")
    L=[1,2,3,[5,6,7], 4]
    print desanida(L)
    print("L=[1,[2,45],3,[5,6],[4,8]]")
    L=[1,[2,45],3,[5,6],[4,8]]
    print desanida(L)
    print("\nPruebas con mprof(L)")
    print("L=[[2,3,[[]]],7]")
    L=[[2,3,[[]]],7]
    print mprof(L)
    print("L=Jaime")
    L="Jaime"
    print mprof(L)
    print("L=[1,2,[],[1,2,[2],[[]]],[]]")
    L=[1,2,[],[1,2,[2],[[]]],[]]
    print mprof(L)
    print("\nPruebas con natural(L)")
    print("L=[1,4,6,78,90,54,3,2,4,6,7]")
    L=[1,4,6,78,90,54,3,2,4,6,7]
    print natural(L)
    print("L=[4,2,1,6,5,4,6,7,8,9,10]")
    L=[4,2,1,6,5,4,6,7,8,9,10]
    print natural(L)
    print("\nPruebas con soloPalabras(L) (Opcional)")
    print("hilera=Anita lava la tina")
    hilera="Anita lava la tina"
    print soloPalabras(hilera)
    print("Juan es un muy buen amigo mio d9ee8e me buen")
    hilera="Juan es un muy buen amigo mio d9ee8e me buen"
    print soloPalabras(hilera)
    return "Gracias por su atención"

prueba()
