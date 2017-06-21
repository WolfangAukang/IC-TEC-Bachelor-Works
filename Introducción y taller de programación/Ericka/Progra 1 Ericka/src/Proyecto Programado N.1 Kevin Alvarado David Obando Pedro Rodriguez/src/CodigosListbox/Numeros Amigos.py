def numerosAmigos(num1, num2): 
    if num1==amigosAux(num2, num2, 1):
        if num2==amigosAux(num1,num1,1):
            return (" SON numeros amigos")
        else:
            return (" NO SON numeros amigos")
    else:
        return (" NO SON numeros amigos")

#-------------------------------------------------------
def amigosAux(num, num2, cont): 
    if num2==2:
        return cont
    else:   
        if num%(num2-1)==0:
            cont=cont+(num2-1)
            return amigosAux(num, num2-1, cont)
        else:
            return amigosAux(num, num2-1, cont)