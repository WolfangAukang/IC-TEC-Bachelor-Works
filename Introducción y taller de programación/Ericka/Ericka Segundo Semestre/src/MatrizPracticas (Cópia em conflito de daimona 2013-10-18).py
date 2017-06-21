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