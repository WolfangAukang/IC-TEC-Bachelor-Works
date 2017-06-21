#Funcion de primo, utilizada para saber si el sumando es primo o no
def primo(n,div=2):
    if div>n:
        return True
    else:
        if n%div==0:
            return False
        else:
            return primo(n, div+1)
         
#Funcion auxiliar de la conjetura de Golbach, la cual realiza calculos de acuerdo a la formula
def Golbachaux(num,sumador=2, res=[]):
    if sumador==num:
        return res
    else:
        if primo(sumador) and primo(num-sumador) and sumador!=1 and (num-sumador)!=1:
            return Golbachaux(num,sumador+1,res+[[sumador, num-sumador]])
        else:
            return Golbachaux(num,sumador+1,res)
        
#Funcion principal de Golbach, que confirma los datos insertados
def Golbach(num):
    if num%2==0 and num>2:
        return Golbachaux(num)
    else:
        return "Error, lo insertado no es par y/o no es mayor a dos"
