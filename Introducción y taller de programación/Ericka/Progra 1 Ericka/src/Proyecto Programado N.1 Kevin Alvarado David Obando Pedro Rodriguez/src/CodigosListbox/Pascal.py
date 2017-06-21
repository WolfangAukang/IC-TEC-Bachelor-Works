def factor(num, fac=0):
    if num<10**fac:
        return fac
    else:
        return factor(num,fac+1)
#----------------------------------------------------------------------------------------
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
#----------------------------------------------------------------------------------------
def calcPascal(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))
#----------------------------------------------------------------------------------------
def trianguloPascalAux(numact, posact, poslleg, impr, res):
    if numact==poslleg:
        res = res + str(impr*10+1)
        return res
    else:
        if numact==posact:
            res= res + str(impr*10+1)+"\n"
            return trianguloPascalAux(0, posact+1, poslleg, 0, res)
        else:
            return trianguloPascalAux(numact+1, posact, poslleg, impr*10**factor(calcPascal(posact,numact),0)+calcPascal(posact,numact), res)