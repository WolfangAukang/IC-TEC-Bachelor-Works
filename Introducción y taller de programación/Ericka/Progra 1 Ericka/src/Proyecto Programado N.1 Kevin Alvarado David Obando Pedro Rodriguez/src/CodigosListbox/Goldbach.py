def Goldbach(num,sumador=2, res=[]):
    if sumador==num:
        return res
    else:
        if primo(sumador) and primo(num-sumador) and sumador!=1 and (num-sumador)!=1:
            return Goldbach(num,sumador+1,res+[[sumador, num-sumador]])
        else:
            return Goldbach(num,sumador+1,res)
#-------------------------------------------------------------------------------------------------------------------
def primo(n,div=2):
    if div>(n//2):
        return True
    else:
        if n%div==0:
            return False
        else:
            return primo(n, div+1)
