'''
Created on 13/08/2013

@author: Pedro
'''
def name(cual):
    nombre="Tariro"
    numero=56
    if cual==1:
        print "Tu nombre es " + str(nombre) + ". Hola " + str(numero) + "."
    else:
        print "Tu nombre es %s. Hola %d." % (nombre, numero)

def funcionA(x):
    x=x*2
    print("x dentro de la funcion A es %d") % (x)
    return x

def funcionB(a,b):
    global x
    a=a+5
    b=b-1
    x=a+b
    
x=10
print ("en la declaracion x es %d") % (x)
x=funcionA(x)

a=20
b=30
funcionB(a,b)
print ("luego de la funcionB x es %d") % (x)