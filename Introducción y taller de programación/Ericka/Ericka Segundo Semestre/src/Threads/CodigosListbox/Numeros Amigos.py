#AUXILIAR DE LA FUNCION QUE OBTIENE DIVISORES
def divisoresAux(num, numz, hilera):
    coma=", "
    if numz==1:
        
        hilera= hilera[0:(len(hilera)-2)]+"."      
        return hilera
    elif num%(numz-1)==0:
        cv= str(numz-1)    
        hilera=cv+coma+hilera
        return divisoresAux(num, numz-1, hilera)
    else:
        return divisoresAux(num, numz-1, hilera)
#FUNCION PARA OBTENER LOS DIVISORES DE UN NUMERO
def divisores(num):
    lista=[]
    hilera=""
    numz=num
    return divisoresAux(num, numz, hilera)
#AUXILIAR DE LA FUNCION PRINCIPAL
def amigosAux(num, num2, cont):
    
    if num2==2:
        return cont
    else:
        
        if num%(num2-1)==0:
            cont=cont+(num2-1)
            return amigosAux(num, num2-1, cont)
        else:
            return amigosAux(num, num2-1, cont)
#FUNCION QUE SUMA LOS DIVISORES DE UN NUMERO
def sumadivisores(num):
    return amigosAux(num, num, 1)
#FUNCION PRINCIPAL
def numerosAmigos(num1, num2):
    cont=1
    numx=num1
    numy=num2
    if num1==amigosAux(num2, numy, cont)and num2==amigosAux(num1,numx,cont):
        print("Divisores del " +str(num1)+":")
        print(divisores(num1))
        print("La suma da "+str(num2))
        print("")
        print("Divisores del " +str(num2)+":")
        print(divisores(num2))
        print("La suma da "+str(num1))
        print("")
        return "Por lo tanto "+str(num1)+" y "+str(num2)+" son numeros amigos."
    else:
        print("Divisores del " +str(num1)+":")
        print(divisores(num1))
        print("La suma da "+str(sumadivisores(num1)))
        print("")
        print("Divisores del " +str(num2)+":")
        print(divisores(num2))
        print("La suma da "+str(sumadivisores(num2)))
        print("")
        return "Por lo tanto "+str(num1)+" y "+str(num2)+" no son numeros amigos."
