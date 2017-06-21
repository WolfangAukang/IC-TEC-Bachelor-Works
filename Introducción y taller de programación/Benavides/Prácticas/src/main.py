'''
Created on 16/03/2013

@author: Leeecher
'''
import P1
if __name__ == '__main__':
    pass
    b=False
    while b==False:
        a=P1.calc_hotel()
        print a
        b=input("Desea salir? (1 para si, 0 para no): ")
        if b==1:
            b=False
        else:
            b=True