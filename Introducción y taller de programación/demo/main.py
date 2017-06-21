'''
Created on Mar 7, 2013

@author: rajcbc
'''
import demo

if __name__ == '__main__':
    pass
    a=demo.CelFah(25)
    print a
    a=demo.FahCel(77)
    print a
    a=demo.EcuCuadratica(1, 2, -8)
    print a
    salir=False
    while salir==False:
        demo.imprimecondicion()
        sal=input("desea salir s/n: ")
        if sal=='n':
            salir=False
        else:
            salir=True