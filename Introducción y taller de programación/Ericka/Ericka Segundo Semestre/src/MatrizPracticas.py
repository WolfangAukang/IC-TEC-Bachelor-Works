from __future__ import division
import math

def cuadradomatriz(m,filadese,coldese):
    filatotal=len(m)-1
    coltotal=len(m[0])-1
    if filadese>filatotal or coldese>coltotal:
        return "Error, datos erroneos"
    else:
        if filatotal==1 or coltotal==1:
            if filatotal==1:
                return m[coldese]
            elif coltotal==1:
                return m[filadese][0]
        elif filadese==0 or filadese==filatotal or coldese==0 or coldese==coltotal:
                if coldese==0 and filadese==0:
                    return [[[],m[0][1]],[(m[1][0]),(m[1][1])]]
                elif coldese==0 and filadese==filatotal:
                    return [[(m[filatotal-1][0]),(m[filatotal-1][1])],[[],m[filatotal][1]]]
                elif coldese==coltotal and filadese==0:
                    return [[m[0][coltotal-1],[]],[(m[1][coltotal-1]),(m[1][coltotal])]]
                elif coldese==coltotal and filadese==filatotal:
                    return [[(m[filatotal-1][coltotal-1]),(m[filatotal-1][coltotal])],[m[filatotal][coltotal-1],[]]]
                elif coldese==0:
                    return [[(m[filadese-1][0]),(m[filadese-1][1])],[[],(m[filadese][1])],[(m[filadese+1][0]),(m[filadese+1][1])]]
                elif filadese==0:
                    return [[(m[0][coldese-1]),[],(m[0][coldese+1])],[(m[1][coldese-1]),(m[1][coldese]),(m[1][coldese+1])]]
                elif coldese==coltotal:
                    return [[(m[filadese-1][coltotal-1]),(m[filadese-1][coltotal])],[(m[filadese][coltotal-1]),[]],[(m[filadese+1][coltotal-1]),(m[filadese+1][coltotal])]]
                else:
                    return [[(m[filatotal-1][coldese-1]),(m[filatotal-1][coldese]),(m[filatotal-1][coldese+1])],[(m[filatotal][coldese-1]),[],(m[filatotal][coldese+1])]]
        else:
            return [[(m[filadese-1][coldese-1]),(m[filadese-1][coldese]),(m[filadese-1][coldese+1])],[(m[filadese][coldese-1]),[],(m[filadese][coldese+1])],[(m[filadese+1][coldese-1]),(m[filadese+1][coldese]),(m[filadese+1][coldese+1])]]
        
def bordesmatriz(m):
    resgen=[]
    resfil=[]
    filatotal=len(m)-1
    coltotal=len(m[0])-1
    cont=0
    for i in range(0,coltotal+1):
        resfil.append(m[cont][i])
    resgen.append(resfil)
    cont+=1
    resfil=[]
    while cont!=filatotal:
        resfil.append(m[cont][0])
        contespacios=0
        while contespacios!=coltotal-1:
            resfil.append([])
            contespacios+=1
        resfil.append(m[cont][coltotal])
        cont+=1
        resgen.append(resfil)
        resfil=[]
    for i in range(0,coltotal+1):
        resfil.append(m[filatotal][i])
    resgen.append(resfil)
    return resgen

def sumamitadmatriz(m):
    totalfil=len(m)
    totalcol=len(m[0])
    contador=(totalfil*totalcol)//2
    suma1=0
    suma2=0
    col1=0
    col2=totalcol-1
    fil1=0
    fil2=totalfil-1
    while contador!=0:
        if col1>totalcol-1:
            col1=0
            fil1+=1
        if col2<0:
            col2=totalcol-1
            fil2-=1
        suma1+=m[fil1][col1]
        suma2+=m[fil2][col2]
        col1+=1
        col2-=1
        contador-=1
    if suma1==suma2:
        return True
    else:
        return False

def iterativasubmatriz(m,fil,col):
    totalfil=len(m)
    totalcol=len(m[0])
    nm=[]
    for i in range(fil,totalfil):
        nm+=[m[i][col:]]
    return nm

def invertibles(m1,m2):
    if len(m1[0])!=len(m2):
        return "Error, las matrices no son de igual dimension"
    else:
        matid=[]
        m1nuev=[]
        fil=[]
        n=0
        while n!=len(m1[0]):
            for i in range(0, len(m1)):
                fil+=[m1[i][n]]
            m1nuev+=[fil]
            fil=[]
            n+=1
        m1=m1nuev
        del m1nuev
        fil=[]
        n=0
        c=0
        while n!=len(m2):
            if c==len(m2):
                c=0
                n+=1
                matid+=[fil]
                fil=[]
            multi=0
            try:
                for i in range(0, len(m2[0])):
                    multi+=m1[n][i]*m2[c][i]
                fil+=[multi]
                c+=1
            except:
                pass 
        return matid

def ceros(m):
    resp=[]
    totalfil=len(m)-1
    totalcol=len(m[0])-1
    i=0
    f=0
    while i!=totalcol+1 or f!=totalfil:
        if i>totalcol:
            i=0
            f+=1
        if m[f][i]==0:
            resp+=[[f,i]]
        i+=1
        
    return resp