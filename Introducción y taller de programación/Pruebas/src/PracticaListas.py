# -*- coding: cp1252 -*-

'''
Created on 30/09/2013

@author: Pedro
'''
def contarelementos(lista):
    if lista==[]:
        return 0
    else:
        return 1+contarelementos(lista[1:])
    
def multiplicarelementos(multi,lista,resp=[]):
    if lista==[]:
        return resp
    else:
        return multiplicarelementos(multi,lista[1:],resp+[lista[0]*multi])
    
def obtenerelementospares(lista,resp=[]):
    if lista==[]:
        return resp
    else:
        if lista[0]%2==0:
            return obtenerelementospares(lista[1:],resp+[lista[0]])
        else:
            return obtenerelementospares(lista[1:],resp)

def confirmarunpar(lista):
    if lista==[]:
        return False
    else:
        if lista[0]%2==0:
            return True
        else:
            return confirmarunpar(lista[1:])

def confirmartodopar(lista):
    if lista==[]:
        return True
    else:
        if lista[0]%2==0:
            return confirmartodopar(lista[1:])
        else:
            return False
        
def separarparimpar(lista,par=[],impar=[]):
    if lista==[]:
        return [par,impar]
    else:
        if lista[0]%2==0:
            return separarparimpar(lista[1:],par+[lista[0]],impar)
        else:
            return separarparimpar(lista[1:],par,impar+[lista[0]])

def aparicion1lista(elem,lista,listan=[],cont=0):
    if lista==[]:
        return listan
    else:
        if lista[0]==elem and cont==0:
            return aparicion1lista(elem,lista[1:],listan,cont+1)
        else:
            return aparicion1lista(elem,lista[1:],listan+[lista[0]],cont)
    
def apariciontodolista(elem,lista,listan=[]):
    if lista==[]:
        return listan
    else:
        if lista[0]==elem:
            return apariciontodolista(elem,lista[1:],listan)
        else:
            return apariciontodolista(elem,lista[1:],listan+[lista[0]])

def mayornum(lista,may=0,cont=0):
    if lista==[]:
        return may
    else:
        if cont==0:
            may=lista[0]
            return mayornum(lista[1:],may,cont+1)
        else:
            if lista[0]>may:
                may=lista[0]
            return mayornum(lista[1:],may,cont)
    
def cambiarpalabra(lista,p1,p2):
    if lista==[]:
        return lista
    else:
        if lista[0]==p1:
            return [p2]+ cambiarpalabra(lista[1:],p1,p2)
        else:
            return [lista[0]] + cambiarpalabra(lista[1:],p1,p2)
    
def eliminarapariciones(lista,pal):
    if lista==[]:
        return lista
    else:
        if lista[0]==pal:
            return []+ eliminarapariciones(lista[1:],pal)
        else:
            return [lista[0]] + eliminarapariciones(lista[1:],pal)
        
def invertirlista(lista,cont=0):
    n=len(lista)//2
    if n-cont==0:
        return lista
    else:
        primelem=lista[0+cont]
        ultimelem=lista[-1-cont]
        lista[0+cont]=ultimelem
        lista[-1-cont]=primelem
        return invertirlista(lista,cont+1)

def eliminarlistaporlista(lista1,lista2,n=0):
    if lista2==[]:
        return lista1
    else:
        return eliminarlistaporlista(eliminarapariciones(lista1,lista2[0]),lista2[1:],n+1)

def fusionlistas(lista1,lista2,nuevalista=[]):
    if lista1==[]:
        return nuevalista
    elif lista2==[]:
        if lista1[0] in nuevalista:
            return fusionlistas(lista1[1:],lista2,nuevalista)
        else:
            return fusionlistas(lista1[1:],lista2,nuevalista+[lista1[0]])
    else:
        if lista2[0] in nuevalista:
            return fusionlistas(lista1,lista2[1:],nuevalista)
        else:
            return fusionlistas(lista1,lista2[1:],nuevalista+[lista2[0]])
        
def xorlistas1(lista1,lista2,nuevalista=[]):
    if lista2==[]:
        return lista1+nuevalista
    else:
        if lista2[0] not in lista1:
            return xorlistas1(lista1,lista2[1:],nuevalista+[lista2[0]])
        else:
            return xorlistas1(lista1,lista2[1:],nuevalista)
        
def xorlistas2(lista1,lista2,nuevalista=[]):
    if lista1==[]:
        return lista2+nuevalista
    else:
        if lista1[0] not in lista2:
            return xorlistas2(lista1[1:],lista2,nuevalista+[lista1[0]])
        else:
            return xorlistas2(lista1[1:],lista2,nuevalista)
        
def andlistas(lista1,lista2,nuevalista=[]):
    if lista2==[]:
        return nuevalista
    else:
        if lista2[0] in lista1:
            return andlistas(lista1,lista2[1:],nuevalista+[lista2[0]])
        else:
            return andlistas(lista1,lista2[1:],nuevalista)

def aparicion1vezlista(elem,lista,listan=[],cont=0):
    if lista==[]:
        return listan
    else:
        if lista[0]==elem and cont==0:
            return lista[1:]
        else:
            return aparicion1lista(elem,lista[1:],listan+[lista[0]],cont)

def removerrepetidas(lista):
    if lista==[]:
        return lista
    else:
        cont=lista.count(lista[0])
        if cont!=1:
            return removerrepetidas(aparicion1vezlista(lista[0],lista))
        else:
            return [lista[0]]+removerrepetidas(lista[1:])

def operacionU(a,u0,b,terminos=[]):
    if 