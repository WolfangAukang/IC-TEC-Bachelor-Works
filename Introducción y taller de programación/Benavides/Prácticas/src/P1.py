'''
Created on 16/03/2013

@author: Leeecher
'''
'''1. Entrada: Un numero
Salida: El resultado de la division del numero entre 7
Restricciones: Ninguna'''
def foo(op):
    return op/7

'''2. Entrada: Un ano.
Salida: Un booleano indicando True si es un ano bisiesto o False negandolo.
Restriccion: Ninguna.'''
def bisiesto():
    a=input("Inserte ano d.C: ")
    if a%4==0 or a%400==0 and not a%100==0:
        return True
    else:
        return False

'''3. Entrada: Un numero positivo el cual sera desglosado.
Salida: El desglose de este numero, indicando en una tupla, la cantidad de 100's, 50's, 20's, 10's, 5's y 1's.
Restriccion: Que el numero no sea negativo.'''
def desglose():
    num=input('Favor insertar numero: ')
    if num/100>=0:
        a=num/100
        num-=a*100
    else:
        num=num
    if num/50>=0:
        b=num/50
        num-=b*50
    else:
        num=num
    if a/20>=0:
        c=num/20
        num-=c*20
    else:
        num=num
    if a/10>=0:
        d=num/10
        num-=d*10
    else:
        num-num
    if a/5>=0:
        e=num/5
        num-=e*5
    else:
        num=num
    if a/1>=0:
        f=num
        num-=f
    return (a,b,c,d,e,f)

'''4. Entrada: tres argumentos numericos
Salida: EL numero medio de los tres argumentos numericos
Restriccion: Ninguna'''
def mediano(a,b,c):
    d=max(a,b,c)
    e=min(a,b,c)
    if (a==d or a==e) and (b==d or b==e):
        return c
    elif (a==d or a==e) and (c==d or c==e):
        return b
    else:
        return a
    
'''5. Entrada: Tres numeros en una tupla
Salida: La tupla ordenada de mayor a menor
Restriccion: Ninguna'''
def orden(a,b,c):
    d=max(a,b,c)
    e=min(a,b,c)
    if a==d and b==e:
        return (a,c,b)
    elif a==d and c==e:
        return (a,b,c)
    elif b==d and a==e:
        return (b,c,a)
    elif b==d and c==e:
        return (b,a,c)
    elif c==d and a==e:
        return (c,b,a)
    elif c==d and b==e:
        return (c,a,b)
    else:
        print"Error: numeros iguales"
                
'''6. Entrada: Un numero que indique la cantidad de Gigabytes en un disco duro.
Salida: Un numero que indica la cantidad de bytes en el disco duro
Restriccion: Ninguna'''
def disco():
    a=input("Favor insertar el tamano del disco duro: ")
    a*=1073741824
    return a

'''7. Entrada: Se insertan dos numeros.
Salida: La suma de el primer numero insertado elevado a la dos, mas diez
Restricciones:Ninguna'''
def misterio(a,c):
    b=lambda x:a**2
    d=b(c)+10
    return d

'''8. Entrada: Un numero que indica la cantidad de metros a convertir.
Salida: La conversion del numero insertado a centimetros, pulgadas, pies o yardas.
Restricciones: Ninguna'''
def conversionmetros():
    metros=input("Favor insertar la cantidad de metros a convertir: ")
    indicador=input('A que lo deseas convertir? (1 para centimetros, 2 para pulgadas, 3 para pies o 4 para yardas): ')
    if indicador==1:
        metros*=100
        return metros
    elif indicador==2:
        metros*=39.37007874
        return metros
    elif indicador==3:
        metros*=3.280839895
        return metros
    elif indicador==4:
        metros*=1.093613298
        return metros
    else:
        return('Error: Numero no disponible')

'''9. Entrada: Un numero que indica la cantidad de horas del trabajador
Salida: Un numero que indica el salario estimado que se debe pagar al trabajador, de acuerdo a las horas laboradas por el trabajador
Restriccion: ninguna'''
def calc_salario():
    hora=input("Pavor insertar las horas laboradas por el trabajador: ")
    print("Recordar que por cada hora laborada se pagan 30000 colones")
    salario=30000*hora
    if hora>=40:
        salario*=1.5
    else:
        salario*=1
    return salario 

'''10. Entrada: Un numero entero que indica el salario del jugador
Salida: Un numero que indica el salario del jugador incluyendo un aumento.
Restriccion: No insertar un numero negativo'''
def aumento():
    salario=input("Favor insertar salario del jugador: ")
    if salario<0:
        print("Salario no valido")
    else:
        if salario<=1000000:
            salario*=1.2
        elif salario<=1500000:
            salario*=1.1
        elif salario<=2000000:
            salario*=1.05
        else:
            salario=salario
    return "Salario es igual a ", salario
    
'''11. Entrada: Tres numeros, que indican la hora, los minutos y los segundos, respectivamente.
Salida: Un numero que indica la cantidad de minutos que falta para que sea otro dia
Restriccion: Que alguno de los tres numeros sea negativo'''
def minutos():
    hora=input("Favor insertar la hora: ")
    minuto=input("Favor insertar los minutos: ")
    segundo=input("Favor insertar los segundos: ")
    if 0<=hora<=23 and 0<=minuto<=59 and 0<=segundo<=59:
        hora*=60
        segundo/=60
        faltante=hora+segundo+minuto
        return faltante
    else:
        print "Error: Datos falsos"

'''12. Entrada: Un numero entero de tres digitos.
Salida: Un booleano indicando True si el numero es palindromo y false si el numero no lo es.
Restriccion: El numero no puede ser mayor a 999 ni menor a 100'''
def palindromo():
    num=input("Favor insertar un numero: ")
    if 100<=num<=999:
        a=num/100
        b=num%100
        c=b%10
        if a==c:
            return True
        else:
            return False
    else:
        print "Error: El numero no es de tres digitos"
        
'''13. Entrada: Un numero de tres digitos.
Salida: Un numero que indica el digito mas significativo del numero insertado.
Restriccion: Que no sea de tres digitos.'''
def significativo():
    num=input("Favor insertar numero: ")
    if 100<=num<=999:
        return num/100
    else:
        print "Error en numero de entrada"

'''14. Entrada: Una tupla de dos numeros enteros.
Salida: Un numero equivalente a la adjuncion del segundo numero al primer numero.
Restriccion: Ninguna'''
def adjunto(a,c):
    b=a*10+c
    return b

'''15. Entrada: Una tupla con tres numeros, que indican el dia, mes y ano, respectivamente.
Salida: Un booleano que indica True si a fecha es valida o False si no lo es.
Restriccion: Ninguna'''
def valida(dia,mes,ano):
    if ano%4==0 or ano%400==0 and not ano%100==0:  #Bisiesto
        if mes==2:                                 #Febrero
            if 1<=dia<=29:                         #1 a 29 dias
                a=True
            else:
                a=False
        elif mes==1 or 3 or 5 or 7 or 8 or 10 or 12:   #Enero, Marzo, Mayo, Julio, Agosto, Octubre, Diciembre
            if 1<=dia<=31:                             #1 a 31 dias
                a=True
            else:
                a=False
        elif mes==4 or 6 or 9 or 11:              #Abril, Junio, Septiembre, Noviembre
            if 1<=dia<=30:                        #1 a 30 dias
                a=True
            else:
                a=False
        else:
            a=False
    else:                                          #Ano normal
        if mes==2:                                 #Febrero
            if 1<=dia<=28:                         #1 a 28 dias
                a=True
            else:
                a=False
        elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:   #Enero, Marzo, Mayo, Julio, Agosto, Octubre, Diciembre
            if 1<=dia<=31:                                                           #1 a 31 dias
                a=True
            else:
                a=False
        elif mes==4 or mes==6 or mes==9 or mes==11:               #Abril, Junio, Septiembre, Noviembre
            if 1<=dia<=30:                                        #1 a 30 dias
                a=True
            else:
                a=False
        else:
            a=False
    return a

'''16. Entrada: Una tupla de tres numeros indicando cantidad de mensajes, minutos plenos y minutos reducidos.
Salida: Un numero que indica el monto a pagar.
Restriccion: Ninguna'''
def calcula_monto(a,b,c):
    if a>100:
        d=(a-100)*5
    else:
        d=0
    if b>60:
        e=(b-60)*35
    else:
        e=0
    f=c*20
    monto=(5000+d+e+f)*1.15
    return monto

'''17. Entrada: 4 numeros, que representan la cantidad de personas, cantidad de noches, tipo de habitacion y cantidad de desayunos, ademas de un booleano indicando True o false por la cama adicional.
Salida: Un numero que inidca el monto a cobrarse.
Restriccion: Ninguna'''
def calc_hotel():
    personas=input("Favor insertar la cantidad de personas: ")
    noches=input("Favor insertar la cantidad de noches en estadia: ")
    habitacion=input("Favor insertar el tipo de habitacion a utilizar (Indicar 4 para ejecutiva y 6 para suite): ")
    cama=input("Es necesario una cama extra? (Indicar 1 para si y 0 para no): ")
    desayuno=input("Cuantos desean desayuno?: ")
    dia=noches+1
    a=desayuno*15               #Cantidad de desayunos por 15
    if cama==1:
        b=20
    elif cama==0:
        b=0
    else:
        print "Error"
    if habitacion==4:
        c=personas*40
    elif habitacion==6:
        c=personas*60
    else:
        print "Error"
    factura=noches*(b+c)+dia*a
    return "El precio a pagar seria de: " +str(factura)