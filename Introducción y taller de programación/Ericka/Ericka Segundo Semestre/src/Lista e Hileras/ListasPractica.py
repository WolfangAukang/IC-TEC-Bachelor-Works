import random
'''
Created on 19/09/2013

@author: Pedro
'''
'''Ejercicio 1: Histograma
Entrada: Una lista con digitos
Salida: Un gráfico indicando las veces con las cuales han salidos dichos dígitos
Restriccion: Si se inserta un numero menor a 0 o mayor a 9, este no se contara'''
def grafica(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,numcorr,res):
    if numcorr==0:
        print "--------------------------------"
        print "  | 0  1  2  3  4  5  6  7  8  9"
        return "Gracias por usar el grafico"
    else:
        res+=str(numcorr)
        res+=" | "
        if l0==numcorr:
            res+="*  "
        else:
            res+="   "
        if l1==numcorr:
            res+="*  "
        else:
            res+="   "
        if l2==numcorr:
            res+="*  "
        else:
            res+="   "
        if l3==numcorr:
            res+="*  "
        else:
            res+="   "
        if l4==numcorr:
            res+="*  "
        else:
            res+="   "
        if l5==numcorr:
            res+="*  "
        else:
            res+="   "
        if l6==numcorr:
            res+="*  "
        else:
            res+="   "
        if l7==numcorr:
            res+="*  "
        else:
            res+="   "
        if l8==numcorr:
            res+="*  "
        else:
            res+="   "
        if l9==numcorr:
            res+="*  "
        else:
            res+="   "
        print res
        return grafica(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,numcorr-1,"")

def histogramaalgo(lista):
    l0=lista.count(0)
    l1=lista.count(1)
    l2=lista.count(2)
    l3=lista.count(3)
    l4=lista.count(4)
    l5=lista.count(5)
    l6=lista.count(6)
    l7=lista.count(7)
    l8=lista.count(8)
    l9=lista.count(9)
    return grafica(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9,max(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9), "")

'''Ejercicio 2: Entrecruza listas
Entrada: Dos listas las cuales se entrecruzaran
Salida: Dos listas entrecruzadas
Restriccion: Ninguna'''
def Entrecruzamiento(lista1,lista2,lista1mod=[],lista2mod=[], cont=0):
    if lista1==[] or lista2==[]:
        if lista1==lista2:
            return [lista1mod,lista2mod]
        elif lista1==[]:
            return [lista1mod,(lista2mod+lista2)]
        else:
            return [(lista1mod+lista1),lista2mod]
    else:
        if cont%2==0:
            return Entrecruzamiento(lista1[1:], lista2[1:], lista1mod+[lista1[0]], lista2mod+[lista2[0]],cont+1)
        else:
            return Entrecruzamiento(lista1[1:], lista2[1:], lista1mod+[lista2[0]], lista2mod+[lista1[0]],cont+1)


'''Ejercicio 3: Fusionar listas ordenadas
Entrada: Dos listas, las cuales seran fusionadas
Salida: Una lista ordenada, que corresponde a la fusion de las dos  listas insertadas
Restriccion: No es valido insertar hileras (strings) dentro de las listas'''
def EliminaRepet(lista,listanueva=[]):
    if lista==[]:
        return listanueva
    else:
        if lista.count(lista[0])>0:
            listanueva=listanueva+[lista[0]]
            lista=RemoverElemento(lista, lista[0])
        return EliminaRepet(lista,listanueva)
                    
def RemoverElemento(lista, elemento):
    if lista.count(elemento)==0:
        return lista
    else:
        lista.remove(elemento)
        return RemoverElemento(lista, elemento)

def ListasOrdenadas(lista1, lista2,listares=[]):
    if lista1==[] or lista2==[]:
        if lista1==lista2:
            return listares
        elif lista1==[]:
            return listares+EliminaRepet(lista2)
        else:
            return listares+EliminaRepet(lista1)
    else:
        if lista1[0]<lista2[0]:
            menor=lista1[0]
        else:
            menor=lista2[0]
        return ListasOrdenadas(RemoverElemento(lista1, menor),RemoverElemento(lista2, menor),listares+[menor])
        
def comprobacionyorden(lista1,lista2):
    return ListasOrdenadas(EliminaRepet(lista1),EliminaRepet(lista2))

'''Ejercicio 4
Entrada: Dos listas, las cuales en una se contiene la palabra y en la otra su significado
Salida: Una lista que relaciona cada palabra de la lista de palabra con al menos un significado
Restriccion: Ninguna'''

def Sortirdef(listadef, listasig, compledef=0):
    nran=int(random.uniform(0,len(listasig)))
    if compledef==len(listadef):
        return ("Lol")
    else:
        print str(listadef[compledef])+" => "+ str(listasig[nran])
        return Sortirdef(listadef, listasig, compledef+1)
