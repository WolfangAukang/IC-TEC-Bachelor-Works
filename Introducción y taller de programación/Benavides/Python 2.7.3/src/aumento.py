'''
Created on 07/03/2013

@author: Leeecher
'''
def aumento():
    salario=input("Favor insertar salario del jugador: ")
    if salario<0:
        print("Salario no valido")
    else:
        if 0<salario<=1000000:
            salario+=salario*0.2
        elif 1000000<salario<=1500000:
            salario+=salario*0.1
        elif 1500000<salario<=2000000:
            salario+=salario*0.05
    return salario
    salario=int(salario)
    print "Salario es igual a", salario