# -*- coding: cp1252 -*-
import Tkinter as Tk
import ttk as Ttk
from tkMessageBox import *
import time
import threading
from math import sqrt

#------------------------------------------------------------------------------------
#Instituto Tecológico de Costa Rica
#Carrera de Ingeniería en Computación
#Curso de Taller de Programación
#Profesora: Ericka Solano Fernández
#Primer Proyecto Programado: Debugger
#Estudiantes: Kevin Alvarado Lamas
#David Obando Paniagua
#Pedro Rodríguez de Oliveira
#II semestre
#2013
#------------------------------------------------------------------------------------

#--------------------------------------------
#Variables
#--------------------------------------------
global LInstruccion
LInstruccion=[]  #Lista global donde se carga el código para los listboxes

#Variable que explica la función de la Conjetura de Goldbach
explicaGoldbach="En teoría de números, la conjetura de Goldbach es uno de los problemas abiertos más antiguos en ma-\ntemáticas."\
                " A veces se califica el problema más di-fícil en la historia de la matemática. Su enuncia-do es el siguiente:\n\n"\
                "Todo número par mayor que 2 puede escribirse como suma de dos números primos.\n\n"\
                "Cabe notar que se puede emplear dos veces el mismonúmero primo.\n\n"\
                "Por ejemplo= 4=2+2, 6=3+3, 8=3+5, 10=3+7, 12=5+7, 14=7+7...\n"\
                "Condiciones para usar la función: Número insertadodebe ser mayor a dos y ser par."

#Variable que explica la función de números amigos
explicaAmigos="En una ocasión le preguntaron a Pitágoras:\n"\
              "Para ti qué es un amigo?. Él respondió:Otro yo\n"\
              "La aplicación de esta forma de concebir la amistada la Teoría de los  Números, condujo a decir que:\n"\
              "Dos números son amigos cuando cada uno de ellos esigual a la suma de los divisores del otro.\nPor ejemplo:\n"\
              "Divisores de 284: 1, 2, 4, 71, 142\n\n"\
              "Divisores de 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110\n\n"\
              "284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110\n\n"\
              "220 = 1 + 2 + 4 + 71 + 142\n\n"\
              "Así, que 220 y 284 son números amigos.\n\n"\
              "Condiciones para usar la función: Ambos números\ndeben ser mayores a uno."

#Variable que explica la función del triángulo de Pascal
explicaPascal="Es un árbol invertido o un triángulo"\
              "donde todos\nsus bordes son 1 y los valores internos son la su-ma de los dos valores "\
              "que se encuentren justo por encima de él.\nLa utilidad de construir un triángulo de Pascal "\
              "sedebe a su directa relación con el cálculo de los  números combinatorios y el uso de la fórmula fac-\ntorial.\n"\
              "Condiciones para usar la función: Número debe ser mayor o igual a cero."
              
#Variable que explica la función de números triangulares
explicaTriangular="Es aquel que puede recomponerse en la forma de un "\
                  "triángulo equilátero (por convención, el primer\nnúmero triangular es el 1).\nPitágoras y los Pitagóricos "\
                  "consideraban sagrado\nel 10 escrito en forma triangular, al cual lo lla-maban Tetraktys.\n"\
                  "Condiciones para usar la función: Número debe ser mayor a 0."

#Variable que explica las curiosidades del 153
explica153="1- Es el número más pequeño que puede ser expresa-do como la suma de los cubos de sus dígitos:\n"\
           "153 =1^3+5^3+3^3= 1 + 125+ 27\n\n"\
           "2- La suma de sus dígitos es un cuadrado perfecto:\n"\
           "1 + 5 + 3 = 9 = 3^2\n\n"\
           "3- Puede ser expresado como la suma de todos los  números enteros del 1 al 17:\n"\
           "153 = 1 + 2 + 3 + 4 +...+ 15 + 16 + 17\n\n"\
           "Esto significa que 153 es el decimoséptimo número triangular. Como su inverso, 351, "\
           "también es un\nnúmero triangular (una suma del 1 hasta 26), pode-mos decir que 153"\
           " es un número triangular inverti-\nble."

#-------------------------------------------------
#Comandos generales de interfaz
#-------------------------------------------------
#Comando para confirmar selección y salir totalmente del programa
def salir(): 
    salida=askokcancel("Está seguro?", "Deseas salir del programa?")
    if salida==True:
        v0.destroy()

#Comando para mostrar message box con créditos adentros
def creditos(): showinfo("Créditos", "Este programa fue realizado por:\nKevin Alvarado\nDavid Obando\nPedro Rodríguez\n"\
                     "Estudiantes cursantes de Taller de Programación\ndel Instituto Tecnológico de Costa Rica.")

#Comando para cerrar la ventana
def mostrar(ventana): return ventana.deiconify

#Comando para abrir la ventana
def ocultar(ventana): return ventana.withdraw()

#Comando para ejecutar ventana después de un cierto tiempo
def ejecutar(f): v0.after(100, f)

#Comando para mostrar la ventana de presentación de la tarea programada
def cerrar_splashscreen():
    ejecutar(ocultar(v1))
    ejecutar(mostrar(v0))

#--------------------------------------------
#Funciones principales (No Debugger)
#--------------------------------------------
'''Conjetura de Goldbach
Entrada: Un número el cual se calculara los primos que al sumarse entre si, dan ese numero
Salida: Una lista con los primos que al sumarse dan el numero insertado
Restriccion: Lo insertado no puede ser menor a 4 ni ser impar, o se retornará mensaje de error'''
#Función que retorna un booleano en caso de que el numero sea primo (True) o no (False).
def primo(n,div=2):
    if div>(n//2):
        return True
    else:
        if n%div==0:
            return False
        else:
            return primo(n, div+1)

#Función que analiza las parejas de numeros primos que, sumados entre ellos, dan el numero insertado por el usuario
def Goldbachaux(num,sumador=2, res=[]):
    if sumador==num:
        return res
    else:
        if primo(sumador) and primo(num-sumador) and sumador!=1 and (num-sumador)!=1:
            return Goldbachaux(num,sumador+1,res+[[sumador, num-sumador]])
        else:
            return Goldbachaux(num,sumador+1,res)

#Comando que convierte el resultado de de la función Goldbachaux en strings
def convertirlistaastring(ResList,cond=False,conteo=0,result=""):
    while not cond:
        if len(ResList)>0:
            if conteo==0:
                result+=str(ResList[0][0])+"+"+str(ResList[0][1])
                conteo+=1
                ResList=ResList[1:]
            else:
                result+=", "+str(ResList[0][0])+"+"+str(ResList[0][1])
        else:
            cond=True
            return result

#Comando que ejecuta la función de Golbachaux sin ejecutar el debugger. Confirma los datos insertados e imprime el resultado en una messagebox
def GoldbachNoDebugger():
    num=EntrGoldbach.get()
    if num<=2 or num%2!=0:
        return showinfo("Error","Error, lo insertado no es par y/o no es mayor a dos")
    else:
        result=convertirlistaastring(Goldbachaux(num))
        return showinfo("Respuesta a la Conjetura de Goldbach"\
                        ,"La(s) suma(s) entre numeros primos que se rezlizan para dar "+str(num)+" son "+ str(result))

    
'''Numeros Amigos
Entrada: Dos números a los cuales se calculara si cumplen con la teoría de los números amigos
Salida: Un cuadro de texto indicando si los numeros son amigos o no. Además, este indica los divisores de ambos numeros
Restriccion: Lo insertado no puede ser menor a 2, o se retornará mensaje de error'''
#AUXILIAR DE LA FUNCION QUE OBTIENE DIVISORES
def divisoresAux(num, numz, hilera): 
    coma=", "
    if numz==1:
        hilera= hilera[0:(len(hilera)-2)]+""
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
def numerosAmigos():
    num1=int(EntrAmigos1.get())
    num2=int(EntrAmigos2.get())
    numx=num1
    numy=num2
    if numx<=1 or numy<=1:
        return showinfo("Error", "Error, lo insertado no es mayor a 1")
    else:
        if num1==amigosAux(num2, numy, 1)and num2==amigosAux(num1,numx,1):
            return showinfo("Respuesta","-Divisores del " +str(num1)+":\n{"+str(divisores(num1))+"}\n-La suma da "+str(num2)+"\n \n -Divisores del " +str(num2)+":\n{"+str(divisores(num2))+"}\n-La suma da "+str(num1)+"\n \nPor lo tanto "+str(num1)+" y "+str(num2)+" SON numeros amigos.")
        else:
            return showinfo("Respuesta", "-Divisores del " +str(num1)+":\n{"+str(divisores(num1))+"}\n-La suma da "+str(sumadivisores(num1))+"\n \n -Divisores del " +str(num2)+":\n{"+str(divisores(num2))+"}\n-La suma da "+str(sumadivisores(num2))+"\n \nPor lo tanto "+str(num1)+" y "+str(num2)+" NO SON numeros amigos.")


'''Triangulo de Pascal
Entrada: Un numero, el cual se le imprimira el escalón correspondiente del triángulo de Pascal.
Salida: Un gráfica mostrando el triángulo de Pascal hasta donde el usuario haya indicado
Restriccion: Lo insertado no puede ser menor a 0, o se retornará mensaje de error'''
#Funcion que calcula el exponente de diez en el cual se encuentra el numero insertado
def factor(num, fac=0):
    if num<10**fac:
        return fac
    else:
        return factor(num,fac+1)

#Funcion que calcula el factorial de lo insertado
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

#Función que calcula la formula de combinaciones de Pascal
def calcPascal(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))

#Funcion que imprime el triangulo de Pascal
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

#Funcion que ejecuta la funcion de trianguloPascalAux sin llamar al debugger. Además, confirma datos e imprime el resultado en una messagebox
def trianguloPascalNoDebugger():
    poslleg=int(EntrPascal.get())
    return showinfo("Triangulo de Pascal","Los escalones son:\n"+trianguloPascalAux(0,0,poslleg,0,""))


'''Numero Triangular
Entrada: Un numero, el cual se investigará su número triangular correspondiente.
Salida: Un gráfica mostrando el número triangular correspondiente
Restriccion: Lo insertado no puede ser menor a 1, o se retornará mensaje de error'''
#Funcion principal que calcula un numero triangular de acuerdo a n
def numerotriangularAux(n):
    if n==1:
        return 1
    else:
        return n + numerotriangularAux(n-1)

#Funcion que imprime espacios para la demostracion
def espacio(n):
    if n==0:
        return ""
    else:
        return " "+espacio(n-1)
    
#Funcion que imprime una imagen del triangulo formado de acuerdo al número insertado por el usuario
def demostracion(n,posorig=0,norig=1,res=""):
    if n==posorig:
        return res
    else:
        if posorig==0:
            res+=str(espacio(n-norig))
        if norig==posorig:
            return demostracion(n,0,norig+1,res+"\n")
        else:
            return demostracion(n,posorig+1,norig,res+"*")

#Función que compara el numero insertado con los números pertenecientes al grupo de los números triangulares
def igualtriangular(n,t=1):
    if n<numerotriangularAux(t):
        return "lo insertado ("+str(n)+") no es un número triangular."
    else:
        if n==numerotriangularAux(t):
            return "lo insertado ("+str(n)+") es un número triangular."
        else:
            return igualtriangular(n, t+1)

#Funcion que ejecuta la funcion principal de numerotriangularAux sin llamar al debugger. Además, confirma lo insertado y da el resultado en una messagebox
def numerotriangularNoDebugger():
    n=int(EntrTriangular.get())
    if n>0:
        return showinfo("Respuesta","El numero triangular correspondiente a "+str(n)+" es "+str(numerotriangularAux(n))+".\nEl ejemplo "\
                        "está aquí:\n\n"+demostracion(n)+"\n\nDentro del triángulo hay "+str(numerotriangularAux(n))+\
                        " asteriscos.\n\nAdemás, "+str(igualtriangular(n)))
    else:
        return showinfo("Error", "Error, datos no validos")


'''Curiosidades 153
Entrada: Nada. El proceso corresponde a escoger un botón con una curiosidad sobre el número 153
Salida: Una de las curiosidades del 153
Restricción: Ninguna'''
#Funcion que muestra una lista con los digitos del numero 153
def digitosdel153(n=153,digitos153=[]):
    if n<=0:
        return digitos153
    else:
        return digitosdel153(n//10,[n%10] + digitos153)

#Funcion que muestra la primera curiosidad
def cubos153(lista1=digitosdel153(), lista2=[]):
    if lista1==[]:
        return str(sum(lista2))+" es igual a la suma de los cubos de sus dígitos:\n1exp(3) + 5exp(3) + 3exp(3)=\n 1 + 125 + 27="+str(sum(lista2))
    else:    
        return cubos153(lista1[:-1],lista2 + [lista1[-1]**3])
    
#Funcion que muestra la segunda curiosidad
def sumadigitos153(lista1=digitosdel153(),lista2=[]):
    if lista1==[]:
        num=sum(lista2)
        if sqrt(num)==int(sqrt(num)) and isinstance(sqrt(num),float):
            return "La suma de los digitos de 153 es: " +  str(num) + " y el " + str(num) + " es un numero cuadrado perfecto" 
    else:
        return sumadigitos153(lista1[:-1],lista2 + [lista1[-1]])

#Funcion que suma los numeros que hay desde el 1 hasta el 17
def sumaenteros153(n=1):
    if n==17:
        return n 
    else:
        return n + sumaenteros153(n+1)

#Funcion que suma los numeros que hay desde el 1 hasta el 26
def sumaenteros351(n=1):
    if n==26:
        return n
    else:
        return n + sumaenteros351(n+1)

#Funcion que muestra la tercera curiosidad
def numerotriangular153(n=1):    
    if sumaenteros153()==153 and sumaenteros351()==351:
        return "La suma de los enteros del 1 al 17 es: 153 y del 1 al 26 es: 351"
    else:
        pass

#--------------------------------------------
#Funciones Debugger
#--------------------------------------------
'''Pestaña de Goldbach'''
#Funcion que carga el código de la Conjetura de Goldbach en la listbox de Algoritmo
def cargaListaGoldbach(LInstruccion):
    f=open("CodigosListbox/Goldbach.py", mode="r")
    contador = 0
    linea = f.readline()
    while linea != "":
        listbox1.insert(contador, linea)
        LInstruccion.append(linea)
        linea = f.readline()
        contador = contador+1
    f.close()
    return LInstruccion

#Confirma los datos insertados por el usuario para invocar el debugger o lanzar mensaje de error
def botonReceiveGoldbach():
    n=EntrGoldbach.get()
    if n%2==0 and n>2:
        resp=threading.Thread(target=lambda:DebuggerGoldbach(LInstruccion,n))
        resp.start()
    else:
        return showinfo("Error","Error, lo insertado no es par y/o no es mayor a dos")

#Realiza el proceso de debugger en la pestaña de Goldbach
def DebuggerGoldbach(LInstruccion,num,sumador=2,res="",cont=0,contres=0):
    if cont==0:
        listbox1.delete(0, Tk.END)
        listbox1var.delete(0, Tk.END)
        Result1.delete(1.0,Tk.END)
        LInstruccion=cargaListaGoldbach(LInstruccion)
    listbox1var.insert(0, "num= "+str(num))
    listbox1var.insert(1, "sumador= "+str(sumador))
    listbox1var.insert(2, "res= ["+str(res)+"]")
    time.sleep(1)
    listbox1.selection_set(0)
    time.sleep(0.5)
    listbox1.selection_clear(0)
    time.sleep(1)
    listbox1.selection_set(1)
    time.sleep(0.5)
    listbox1.selection_clear(1)
    time.sleep(1)
    listbox1var.insert(3, "num==sumador(?)= "+str(num==sumador))
    if num==sumador:
        time.sleep(1)
        listbox1.selection_set(2)
        time.sleep(0.5)
        listbox1.selection_clear(2)
        Result1.insert(Tk.END, "Los numeros primos que se suman para dar "+str(num)+" son ["+str(res)+"]")
    else:
        time.sleep(1)
        listbox1.selection_set(3)
        time.sleep(0.5)
        listbox1.selection_clear(3)
        time.sleep(1)
        listbox1.selection_set(4) 
        time.sleep(0.5)
        listbox1.selection_clear(4)
        listbox1var.delete(3)
        listbox1var.insert(3, "num-sumador= "+str(num-sumador))
        time.sleep(2)
        con="Hel"
        n=sumador
        div=2
        while con=="Hel":
            listbox1.yview(13)
            listbox1var.delete(0, Tk.END)
            listbox1var.insert(0, "n= "+str(n))
            listbox1var.insert(1, "div= "+str(div))
            time.sleep(1)
            listbox1.selection_set(9)
            time.sleep(0.5)
            listbox1.selection_clear(9)
            time.sleep(1)
            listbox1.selection_set(10) 
            time.sleep(0.5)
            listbox1.selection_clear(10)
            listbox1var.insert(2, "n//2= "+str(n//2))
            time.sleep(0.5)
            listbox1var.insert(3, "div>(n//2)(?)= "+str(div>(n//2)))
            if div>(n//2):
                time.sleep(1)
                listbox1.selection_set(11)
                time.sleep(0.5)
                listbox1.selection_clear(11)
                con=True
                listbox1var.insert(4, "condición= "+str(con))
                listbox1.yview(0)
                time.sleep(2.5)
                listbox1var.delete(0, Tk.END)
            else:
                time.sleep(1)
                listbox1.selection_set(12)
                time.sleep(0.5)
                listbox1.selection_clear(12)
                time.sleep(1)
                listbox1.selection_set(13)
                time.sleep(0.5)
                listbox1.selection_clear(13)
                time.sleep(0.5)
                listbox1var.insert(4, "n%div= "+str(n%div))
                time.sleep(1)
                listbox1var.insert(5, "n%div==0(?)= "+str(n%div==0))
                if n%div==0:
                    time.sleep(1)
                    listbox1.selection_set(14)
                    time.sleep(0.5)
                    listbox1.selection_clear(14)
                    con=False
                    listbox1var.insert(6, "condición= "+str(con))
                    time.sleep(2.5)
                    listbox1var.delete(0, Tk.END)
                else:
                    time.sleep(1)
                    listbox1.selection_set(15)
                    time.sleep(0.5)
                    listbox1.selection_clear(15)
                    time.sleep(1)
                    listbox1.selection_set(16)
                    time.sleep(0.5)
                    listbox1.selection_clear(16)
                    div+=1
        listbox1var.insert(0, "num= "+str(num))
        listbox1var.insert(1, "sumador= "+str(sumador))
        listbox1var.insert(2, "res= ["+str(res)+"]")
        listbox1var.insert(3, "num-sumador= "+str(num-sumador))
        listbox1var.insert(4, "primo(sumador)= "+str(primo(sumador)))
        time.sleep(2)
        con="Hel"
        n=num-sumador
        div=2
        while con=="Hel":
            listbox1.yview(13)
            listbox1var.delete(0, Tk.END)
            listbox1var.insert(0, "n= "+str(n))
            listbox1var.insert(1, "div= "+str(div))
            time.sleep(1)
            listbox1.selection_set(9)
            time.sleep(0.5)
            listbox1.selection_clear(9)
            time.sleep(1)
            listbox1.selection_set(10) 
            time.sleep(0.5)
            listbox1.selection_clear(10)
            listbox1var.insert(2, "n//2= "+str(n//2))
            time.sleep(0.5)
            listbox1var.insert(3, "div>(n//2)(?)= "+str(div>(n//2)))
            if div>(n//2):
                time.sleep(1)
                listbox1.selection_set(11)
                time.sleep(0.5)
                listbox1.selection_clear(11)
                con=True
                listbox1var.insert(4, "condición= "+str(con))
                listbox1.yview(0)
                time.sleep(2.5)
                listbox1var.delete(0, Tk.END)
            else:
                time.sleep(1)
                listbox1.selection_set(12)
                time.sleep(0.5)
                listbox1.selection_clear(12)
                time.sleep(1)
                listbox1.selection_set(13)
                time.sleep(0.5)
                listbox1.selection_clear(13)
                time.sleep(0.5)
                listbox1var.insert(4, "n%div= "+str(n%div))
                time.sleep(1)
                listbox1var.insert(5, "n%div==0(?)= "+str(n%div==0))
                if n%div==0:
                    time.sleep(1)
                    listbox1.selection_set(14)
                    time.sleep(0.5)
                    listbox1.selection_clear(14)
                    con=False
                    listbox1var.insert(6, "condición= "+str(con))
                    time.sleep(2.5)
                    listbox1var.delete(0, Tk.END)
                else:
                    time.sleep(1)
                    listbox1.selection_set(15)
                    time.sleep(0.5)
                    listbox1.selection_clear(15)
                    time.sleep(1)
                    listbox1.selection_set(16)
                    time.sleep(0.5)
                    listbox1.selection_clear(16)
                    div+=1
        listbox1var.insert(0, "num= "+str(num))
        listbox1var.insert(1, "sumador= "+str(sumador))
        listbox1var.insert(2, "res= ["+str(res)+"]")
        listbox1var.insert(3, "num-sumador= "+str(num-sumador))
        listbox1var.insert(4, "primo(sumador)= "+str(primo(sumador)))
        time.sleep(1)
        listbox1var.insert(5, "primo(num-sumador)= "+str(primo(num-sumador)))
        time.sleep(1)
        listbox1var.insert(6, "sumador!=1(?)= "+str(sumador!=1))
        time.sleep(1)
        listbox1var.insert(7, "num-sumador!=1(?)= "+str(num-sumador!=1))
        if primo(sumador) and primo(num-sumador) and sumador!=1 and (num-sumador)!=1:
            time.sleep(1)
            listbox1.selection_set(5) 
            time.sleep(0.5)
            listbox1.selection_clear(5)
            listbox1var.delete(0, Tk.END)
            if contres==0:
                return DebuggerGoldbach(LInstruccion,num,sumador+1,res+str(sumador)+","+str(num-sumador),cont+1,contres+1)
            else:
                return DebuggerGoldbach(LInstruccion,num,sumador+1,res+","+str(sumador)+","+str(num-sumador),cont+1,contres)
        else:
            time.sleep(1)
            listbox1.selection_set(6)
            time.sleep(0.5)
            listbox1.selection_clear(6)
            time.sleep(1)
            listbox1.selection_set(7)
            time.sleep(0.5)
            listbox1.selection_clear(7)
            listbox1var.delete(0, Tk.END)
            return DebuggerGoldbach(LInstruccion,num,sumador+1,res,cont+1,contres)


'''Numeros amigos'''
#Funcion que carga el código de números amigos en la listbox de Algoritmo
def cargaListaAmigos(LInstruccion):
    f=open("CodigosListbox/Numeros Amigos.py", mode="r")
    contador = 0
    linea = f.readline()
    while linea != "":
        listbox2.insert(contador, linea)
        LInstruccion.append(linea)
        linea = f.readline()
        contador = contador+1
    f.close()
    return LInstruccion

#Confirma los datos insertados por el usuario para invocar el debugger o lanzar mensaje de error
def botonReceiveAmigos():
    n1=EntrAmigos1.get()
    n2=EntrAmigos2.get()
    if n1>1 and n2>1:
        resp=threading.Thread(target=lambda:DebuggerNumerosAmigos(LInstruccion,n1,n2,n1,n2))
        resp.start()
    else:
        return showinfo("Error","Error, lo insertado no es mayor a 1")

#Realiza el proceso de debugger en la pestaña de números amigos
def DebuggerNumerosAmigos(LInstruccion,num1,num2,n1,n2,cont=0):
    if cont==0:
        listbox2var.delete(0,Tk.END)
        Result2.delete(1.0,Tk.END)
        listbox2.delete(0,Tk.END)
        LInstruccion = cargaListaAmigos(LInstruccion)
    ti=0.3
    listbox2.yview(5)
    listbox2var.insert(0, "num1= "+str(num1))
    listbox2var.insert(0, "num2= "+str(num2))
    time.sleep(ti)
    listbox2.selection_set(0) #Resalta el def numerosAmigos(num1, num2):
    time.sleep(ti)
    listbox2.selection_clear(0) #Deja de resaltar el def numerosAmigos(num1, num2):
    time.sleep(ti)
    listbox2.selection_set(1) #Resalta if num1==amigosAux(num2, num2, 1):
    time.sleep(ti)
    listbox2.selection_clear(1) 
    time.sleep(ti)
    cont=1
    num=num2
    numy=num2
    numx=num1
    while num2!=2:
        listbox2.selection_set(10) #Resalta def amigosAux(num, num2, cont):
        time.sleep(ti)
        listbox2.selection_clear(10) 
        time.sleep(ti)
        listbox2.selection_set(11) #Resalta if num2==2:
        time.sleep(ti)
        listbox2.selection_clear(11) 
        time.sleep(ti)
        time.sleep(ti)
        listbox2.selection_set(13) #Resalta el else 
        time.sleep(ti)
        listbox2.selection_clear(13) #Deja de resaltar el else
        time.sleep(ti)
        listbox2.selection_set(14) #Resalta el  if num%(num2-1)==0:
        time.sleep(ti)
        listbox2.selection_clear(14) #Deja de resaltar el if num%(num2-1)==0
        if num%(num2-1)==0:
            time.sleep(ti)
            listbox2.selection_set(15) #Resalta el cont=cont+(num2-1)
            time.sleep(ti)
            listbox2.selection_clear(15) #Deja de resaltar el cont=cont+(num2-1)
            cont=cont+(num2-1)
            listbox2var.insert(0, "                                cont= "+str(cont))
            listbox2.selection_set(16) #Resalta el return
            time.sleep(ti)
            listbox2.selection_clear(16) #Deja de resaltar el return
            time.sleep(ti)
            num2= num2-1
            listbox2var.insert(0, "                 amigosAux( "+str(num)+", "+str(num2)+", "+str(cont)+")")
        else:
            time.sleep(ti)
            listbox2.selection_set(17) #Resalta el else 
            time.sleep(ti)
            listbox2.selection_clear(17) #Deja de resaltar el else
            time.sleep(ti)
            listbox2.selection_set(18) #Resalta el return
            time.sleep(ti)
            listbox2.selection_clear(18) #Deja de resaltar el return
            time.sleep(ti)
            num2=num2-1
            listbox2var.insert(0, "               amigosAux( "+str(num)+", "+str(num2)+", "+str(cont)+")")
    time.sleep(ti)
    listbox2.selection_set(12) #Resalta el return 
    time.sleep(ti)
    listbox2.selection_clear(12) #Deja de resaltar el return
    time.sleep(ti)
    listbox2.selection_set(1) #Resalta if num1==amigosAux(num2, num2, 1):
    time.sleep(ti)
    listbox2.selection_clear(1) 
    time.sleep(ti)
    listbox2var.insert(0, "cont= amigosAux(num2, num2, 1)= "+str(cont))
    if numx==cont:
        listbox2var.insert(0, "             num1==amigosAux(num2, num2, 1)= True")
        time.sleep(ti)
        listbox2.selection_set(2) #Resalta el num2==amigosAux(num1,num1,1):
        time.sleep(ti)
        listbox2.selection_clear(2) #Deja de resaltar el num2==amigosAux(num1,num1,1):
        time.sleep(ti)
        cont=1
        num= num1
        while num1!=2:
            listbox2.selection_set(10) #Resalta def amigosAux(num, num2, cont):
            time.sleep(ti)
            listbox2.selection_clear(10) 
            time.sleep(ti)
            listbox2.selection_set(11) #Resalta if num2==2:
            time.sleep(ti)
            listbox2.selection_clear(11) 
            time.sleep(ti)
            listbox2.selection_set(13) #Resalta el else 
            time.sleep(ti)
            listbox2.selection_clear(13) #Deja de resaltar el else
            time.sleep(ti)
            listbox2.selection_set(14) #Resalta el  if num%(num2-1)==0:
            time.sleep(ti)
            listbox2.selection_clear(14) #Deja de resaltar el if num%(num2-1)==0:
            if num%(num1-1)==0:
                time.sleep(ti)
                listbox2.selection_set(15) #Resalta el cont=cont+(num1-1)
                time.sleep(ti)
                listbox2.selection_clear(15) #Deja de resaltar el cont=cont+(num1-1)
                cont=cont+(num1-1)
                listbox2var.insert(0, "                       cont= "+str(cont))
                listbox2.selection_set(16) #Resalta el return
                time.sleep(ti)
                listbox2.selection_clear(16) #Deja de resaltar el return
                time.sleep(ti)
                num1=num1-1
                listbox2var.insert(0, "            amigosAux( "+str(num)+", "+str(num1)+", "+str(cont)+")")
            else:
                time.sleep(ti)
                listbox2.selection_set(17) #Resalta el else 
                time.sleep(ti)
                listbox2.selection_clear(17) #Deja de resaltar el else
                time.sleep(ti)
                listbox2.selection_set(18) #Resalta el return
                time.sleep(ti)
                listbox2.selection_clear(18) #Deja de resaltar el return
                time.sleep(ti)
                num1=num1-1
                listbox2var.insert(0, "            amigosAux( "+str(num)+", "+str(num1)+", "+str(cont)+")")
        time.sleep(ti)
        listbox2.selection_set(12) #Resalta el return 
        time.sleep(ti)
        listbox2.selection_clear(12) #Deja de resaltar el return
        time.sleep(ti)
        listbox2.selection_set(2) #Resalta if num2==amigosAux(num1, num1, 1):
        time.sleep(ti)
        listbox2.selection_clear(2) 
        time.sleep(ti)
        if numy==cont:
            listbox2var.insert(0, "num2==amigosAux(num1, num1, 1)= True")
            time.sleep(ti)
            listbox2.selection_set(3) #Resalta el return
            time.sleep(ti)
            listbox2.selection_clear(3) #Deja de resaltar el return
            Result2.insert(Tk.END,str(n1)+" y "+str(n2)+" son números amigos.\nMás detalles, favor darle clic en el botón de Calcular (Sin usar debugger)")
        else:
            time.sleep(ti)
            listbox2.selection_set(5) #Resalta el return
            time.sleep(ti)
            listbox2.selection_clear(5) #Deja de resaltar el return
            time.sleep(ti)
            Result2.insert(Tk.END,str(n1)+" y "+str(n2)+" NO son números amigos.\nMás detalles, favor darle clic en el botón de Calcular (Sin usar debugger)")
    else:
        listbox2var.insert(0, "num1==amigosAux(num2, num2, 1)= False")
        time.sleep(ti)
        listbox2.selection_set(6) #Resalta el else
        time.sleep(ti)
        listbox2.selection_clear(6) #Deja de resaltar el else
        time.sleep(ti)
        listbox2.selection_set(7) #Resalta el return
        time.sleep(ti)
        listbox2.selection_clear(7) #Deja de resaltar el return
        time.sleep(ti)
        Result2.insert(Tk.END,str(n1)+" y "+str(n2)+" NO son números amigos.\nMás detalles, favor darle clic en el botón de Calcular (Sin usar debugger)")


'''Triangulo de Pascal'''
#Funcion que carga el código del triángulo de Pascal en la listbox de Algoritmo
def cargaListaPascal(LInstruccion):
    f=open("CodigosListbox/Pascal.py", mode="r")
    contador = 0
    linea = f.readline()
    while linea != "":
        listbox3.insert(contador, linea)
        LInstruccion.append(linea)
        linea = f.readline()
        contador = contador+1
    f.close()
    return LInstruccion

#Confirma los datos insertados por el usuario para invocar el debugger o lanzar mensaje de error
def botonReceivePascal():
    n=EntrPascal.get()
    if n>=0:
        resp=threading.Thread(target=lambda:DebuggerPascal(LInstruccion,n))
        resp.start()
    else:
        return showinfo("Error","Error, lo insertado no es mayor ni igual a 0")

#Realiza el proceso de debugger en la pestaña del triángulo de Pascal
def DebuggerPascal(LInstruccion, poslleg, numact=0, posact=0, impr=0, res="",cont=0):
    if cont==0:
        listbox3.delete(0, Tk.END)
        listbox3var.delete(0,Tk.END)
        Result3.delete(1.0,Tk.END)
        LInstruccion=cargaListaPascal(LInstruccion)
    listbox3var.insert(0, "Posición de llegada= "+str(poslleg))
    listbox3var.insert(1, "Número actual= "+str(numact))
    listbox3var.insert(2, "Posición actual= "+str(posact))
    listbox3var.insert(3, "Fila a imprimir= "+str(impr))
    listbox3var.insert(4, "Respuesta= "+res)
    listbox3.yview(15)
    time.sleep(1)
    listbox3.selection_set(15)
    time.sleep(0.5)
    listbox3.selection_clear(15)
    time.sleep(1)
    listbox3.selection_set(16)
    time.sleep(0.5)
    listbox3.selection_clear(16)
    listbox3var.insert(5, "Número actual == Posición llegada(?)= "+str(numact==poslleg))
    if numact==poslleg:
        time.sleep(1)
        listbox3.selection_set(17)
        time.sleep(0.5)
        listbox3.selection_clear(17)
        time.sleep(1)
        listbox3.selection_set(17)
        time.sleep(0.5)
        listbox3.selection_clear(17)
        res+= str(impr*10+1)
        listbox3var.delete(4)
        listbox3var.insert(4, "Respuesta= "+res)
        time.sleep(1)
        listbox3.selection_set(18)
        time.sleep(0.5)
        listbox3.selection_clear(18)
        time.sleep(1)
        Result3.insert(Tk.END,"El escalón correspondiente sería:\n"+res)
    else:
        time.sleep(1)
        listbox3.selection_set(19)
        time.sleep(0.5)
        listbox3.selection_clear(19)
        time.sleep(1)
        listbox3.selection_set(20)
        time.sleep(0.5)
        listbox3.selection_clear(20)
        listbox3var.insert(6, "Número actual == Posición actual(?)= "+str(numact==posact))
        if numact==posact:
            time.sleep(1)
            listbox3.selection_set(21)
            time.sleep(0.5)
            listbox3.selection_clear(21)
            res=res+str(impr*10+1)+"\n"
            listbox3var.delete(4)
            listbox3var.insert(4, "Respuesta= "+res)
            time.sleep(1)
            listbox3.selection_set(22)
            time.sleep(0.5)
            listbox3.selection_clear(22)
            listbox3var.delete(0, Tk.END)
            return DebuggerPascal(LInstruccion, poslleg, 0, posact+1, 0, res, cont+1)
        else:
            time.sleep(1)
            listbox3.selection_set(23)
            time.sleep(0.5)
            listbox3.selection_clear(23)
            time.sleep(1)
            listbox3.selection_set(24)
            time.sleep(0.5)
            listbox3.selection_clear(24)
            n=posact
            k=numact
            listbox3var.insert(7, "N= "+str(n))
            listbox3var.insert(8, "K= "+str(k))
            listbox3.yview(11)
            time.sleep(1)
            listbox3.selection_set(12)
            time.sleep(0.5)
            listbox3.selection_clear(12)
            time.sleep(1)
            listbox3.selection_set(13)
            time.sleep(0.5)
            listbox3.selection_clear(13)
            con=False
            resp=1
            num=n
            while not con:
                listbox3var.delete(0,Tk.END)
                listbox3var.insert(0,"num= "+str(num))
                listbox3var.insert(1,"Respuesta= "+str(resp))
                listbox3.yview(5)
                time.sleep(1)
                listbox3.selection_set(6)
                time.sleep(0.5)
                listbox3.selection_clear(6)
                time.sleep(1)
                listbox3.selection_set(7)
                time.sleep(0.5)
                listbox3.selection_clear(7)
                listbox3var.insert(2,"num==0(?) "+str(num==0))
                if num==0:
                    time.sleep(1)
                    listbox3.selection_set(8)
                    time.sleep(0.5)
                    listbox3.selection_clear(8)
                    con=True
                    listbox3var.delete(1)
                    listbox3var.delete(2)
                    listbox3var.insert(1,"Respuesta= "+str(resp))
                    time.sleep(2)
                    listbox3var.delete(0,Tk.END)
                    time.sleep(1)
                else:
                    time.sleep(1)
                    listbox3.selection_set(9)
                    time.sleep(0.5)
                    listbox3.selection_clear(9)
                    time.sleep(1)
                    listbox3.selection_set(10)
                    time.sleep(0.5)
                    listbox3.selection_clear(10)
                    resp=resp*num
                    num-=1
            listbox3var.insert(0, "Posición de llegada= "+str(poslleg))
            listbox3var.insert(1, "Número actual= "+str(numact))
            listbox3var.insert(2, "Posición actual= "+str(posact))
            listbox3var.insert(3, "Fila a imprimir= "+str(impr))
            listbox3var.insert(4, "Respuesta= "+res)
            listbox3var.insert(5, "N= "+str(n))
            listbox3var.insert(6, "K= "+str(k))
            listbox3var.insert(7, "N-K= "+str(n-k))
            time.sleep(0.5)
            listbox3var.insert(8, "Factorial de N= "+str(factorial(n)))
            time.sleep(0.5)
            con=False
            resp=1
            num=k
            while not con:
                listbox3var.delete(0,Tk.END)
                listbox3var.insert(0,"num= "+str(num))
                listbox3var.insert(1,"Respuesta= "+str(resp))
                listbox3.yview(5)
                time.sleep(1)
                listbox3.selection_set(6)
                time.sleep(0.5)
                listbox3.selection_clear(6)
                time.sleep(1)
                listbox3.selection_set(7)
                time.sleep(0.5)
                listbox3.selection_clear(7)
                listbox3var.insert(2,"num==0(?) "+str(num==0))
                if num==0:
                    time.sleep(1)
                    listbox3.selection_set(8)
                    time.sleep(0.5)
                    listbox3.selection_clear(8)
                    con=True
                    listbox3var.delete(1)
                    listbox3var.delete(2)
                    listbox3var.insert(1,"Respuesta= "+str(resp))
                    time.sleep(2)
                    listbox3var.delete(0,Tk.END)
                    time.sleep(1)
                else:
                    time.sleep(1)
                    listbox3.selection_set(9)
                    time.sleep(0.5)
                    listbox3.selection_clear(9)
                    time.sleep(1)
                    listbox3.selection_set(10)
                    time.sleep(0.5)
                    listbox3.selection_clear(10)
                    resp=resp*num
                    num-=1
            listbox3var.insert(0, "Posición de llegada= "+str(poslleg))
            listbox3var.insert(1, "Número actual= "+str(numact))
            listbox3var.insert(2, "Posición actual= "+str(posact))
            listbox3var.insert(3, "Fila a imprimir= "+str(impr))
            listbox3var.insert(4, "Respuesta= "+res)
            listbox3var.insert(5, "N= "+str(n))
            listbox3var.insert(6, "K= "+str(k))
            listbox3var.insert(7, "N-K= "+str(n-k))
            listbox3var.insert(8, "Factorial de N= "+str(factorial(n)))
            time.sleep(0.5)
            listbox3var.insert(9, "Factorial de K= "+str(factorial(k)))
            time.sleep(0.5)
            con=False
            resp=1
            num=n-k
            while not con:
                listbox3var.delete(0,Tk.END)
                listbox3var.insert(0,"num= "+str(num))
                listbox3var.insert(1,"Respuesta= "+str(resp))
                listbox3.yview(5)
                time.sleep(1)
                listbox3.selection_set(6)
                time.sleep(0.5)
                listbox3.selection_clear(6)
                time.sleep(1)
                listbox3.selection_set(7)
                time.sleep(0.5)
                listbox3.selection_clear(7)
                listbox3var.insert(2,"num==0(?) "+str(num==0))
                if num==0:
                    time.sleep(1)
                    listbox3.selection_set(8)
                    time.sleep(0.5)
                    listbox3.selection_clear(8)
                    con=True
                    listbox3var.delete(1)
                    listbox3var.delete(2)
                    listbox3var.insert(1,"Respuesta= "+str(resp))
                    time.sleep(2)
                    listbox3var.delete(0,Tk.END)
                    time.sleep(1)
                else:
                    time.sleep(1)
                    listbox3.selection_set(9)
                    time.sleep(0.5)
                    listbox3.selection_clear(9)
                    time.sleep(1)
                    listbox3.selection_set(10)
                    time.sleep(0.5)
                    listbox3.selection_clear(10)
                    resp=resp*num
                    num-=1
            listbox3var.insert(0, "Posición de llegada= "+str(poslleg))
            listbox3var.insert(1, "Número actual= "+str(numact))
            listbox3var.insert(2, "Posición actual= "+str(posact))
            listbox3var.insert(3, "Fila a imprimir= "+str(impr))
            listbox3var.insert(4, "Respuesta= "+res)
            listbox3var.insert(5, "N= "+str(n))
            listbox3var.insert(6, "K= "+str(k))
            listbox3var.insert(7, "N-K= "+str(n-k))
            listbox3var.insert(8, "Factorial de N= "+str(factorial(n)))
            listbox3var.insert(9, "Factorial de K= "+str(factorial(k)))
            time.sleep(0.5)
            listbox3var.insert(10, "Factorial de N-K= "+str(factorial(n-k)))
            listbox3.yview(15)
            time.sleep(1)
            listbox3.selection_set(13)
            time.sleep(0.5)
            listbox3.selection_clear(13)
            listbox3var.delete(8,Tk.END)
            listbox3var.insert(8, "Formula de Pascal= "+str(factorial(n)//(factorial(k)*factorial(n-k))))
            time.sleep(1)
            listbox3.selection_set(23)
            time.sleep(0.5)
            listbox3.selection_clear(23)
            cond=False
            num=calcPascal(posact,numact)
            fac=0
            while not cond:
                listbox3var.delete(0,Tk.END)
                listbox3var.insert(0,"Numero= "+str(num))
                listbox3var.insert(1,"Factor= "+str(10**fac))
                listbox3.yview(0)
                time.sleep(1)
                listbox3.selection_set(0)
                time.sleep(0.5)
                listbox3.selection_clear(0)
                time.sleep(1)
                listbox3.selection_set(1)
                time.sleep(0.5)
                listbox3.selection_clear(1)
                listbox3var.insert(2,"Numero<Factor(?)= "+str(num<10**fac))
                time.sleep(0.5)
                if num<10**fac:
                    time.sleep(1)
                    listbox3.selection_set(2)
                    time.sleep(0.5)
                    listbox3.selection_clear(2)
                    listbox3var.delete(0,Tk.END)
                    cond=True
                else:
                    time.sleep(1)
                    listbox3.selection_set(3)
                    time.sleep(0.5)
                    listbox3.selection_clear(3)
                    time.sleep(1)
                    listbox3.selection_set(4)
                    time.sleep(0.5)
                    listbox3.selection_clear(4)
                    fac+=1
            del con
            del k
            del n
            con=calcPascal(posact,numact)
            resp=factor(con,0)
            impr=impr*10**(resp)+con
            cont+=1
            numact=numact+1
            return DebuggerPascal(LInstruccion,poslleg, numact, posact, impr, res, cont)


'''Numero triangular'''
#Funcion que carga el código del número triangular en la listbox de Algoritmo
def cargaListaTriangular(LInstruccion):
    f=open("CodigosListbox/Numero Triangular.py", mode="r")
    contador = 0
    linea = f.readline()
    while linea != "":
        listbox4.insert(contador, linea)
        LInstruccion.append(linea)
        linea = f.readline()
        contador = contador+1
    f.close()
    return LInstruccion

#Confirma los datos insertados por el usuario para invocar el debugger o lanzar mensaje de error
def botonReceiveTriangular():
    n=EntrTriangular.get()
    if n>=1:
        resp=threading.Thread(target=lambda:DebuggerTriangular(LInstruccion,n,n))
        resp.start()
    else:
        return showinfo("Error","Error, lo insertado no es mayor ni igual a 1")

#Realiza el proceso de debugger en la pestaña de número triangular
def DebuggerTriangular(LInstruccion,n,norig,res=0,cont=0):
    if cont==0:
        listbox4.delete(0, Tk.END)
        listbox4var.delete(0, Tk.END)
        Result4.delete(1.0,Tk.END)
        LInstruccion = cargaListaTriangular(LInstruccion)
    listbox4var.insert(0, "n= "+str(n))
    listbox4var.insert(1, "Respuesta= "+str(res))
    time.sleep(1)
    listbox4.selection_set(0) #Resalta el def numerotriangular(n):
    time.sleep(0.5)
    listbox4.selection_clear(0) #Deja de resaltar el def numerotriangular(n):
    time.sleep(1)
    listbox4.selection_set(1) #Resalta el if n==1:
    time.sleep(0.5)
    listbox4.selection_clear(1) #Deja de resaltar el if n==1:
    time.sleep(1)
    listbox4var.insert(2, "n==1(?)= "+str(n==1))
    if n==1:
        time.sleep(1)
        listbox4.selection_set(2) #Resalta el return 1
        time.sleep(0.5)
        listbox4var.delete(1)
        res+=1
        listbox4var.insert(1, "Respuesta= "+str(res))
        time.sleep(3)
        listbox4.selection_clear(2) #Deja de resaltar el return 1
        Result4.insert(Tk.END,"El número triangular correspondiente a "+str(norig)+" es "+str(res)+".\nVéase "\
                            "el siguiente dibujo:\n"+demostracion(norig)+"\n\nComo se puede observar, dentro del "\
                            "triangulo hay "+str(res)+" asteriscos.\n\nAdemás, "+str(igualtriangular(norig)))
    else:
        time.sleep(1)
        listbox4.selection_set(3) #Resalta el else:
        time.sleep(0.5)
        listbox4.selection_clear(3) #Deja de resaltar else
        time.sleep(1)
        listbox4.selection_set(4) #Resalta el return n + numerotriangular(n-1)
        time.sleep(0.5)
        listbox4.selection_clear(4) #Deja de resaltar el return n + numerotriangular(n-1)
        listbox4var.delete(0,Tk.END)
        return DebuggerTriangular(LInstruccion,n-1,norig,res+n,cont+1)


'''Curiosidades del 153'''
#Funcion que carga el código de las curiosidades del 153 en la listbox de Algoritmo
def cargaLista153(LInstruccion):
    f=open("CodigosListbox/Curiosidades153.py", mode="r")
    contador = 1
    linea = f.readline()
    while linea != "":
        listbox5.insert(contador, linea)
        LInstruccion.append(linea)
        linea = f.readline()
        contador = contador+1
    f.close()
    return LInstruccion

#Primera curiosidad
#Invoca el debugger para la primera curiosidad
def botonReceive1531():
    resp=threading.Thread(target=lambda:Debugger1531(LInstruccion))
    resp.start()
    
#Realiza el proceso de debugger de la primera curiosidad
def Debugger1531(LInstruccion,n=153,digitos153=[],cont=0):
    if cont==0:
        listbox5.delete(0,Tk.END)
        listbox5var.delete(0,Tk.END)
        Result5.delete(1.0,Tk.END)
        LInstruccion = cargaLista153(LInstruccion)
    time.sleep(1)
    listbox5.selection_set(2)
    time.sleep(0.5)
    listbox5.selection_clear(2)
    time.sleep(1)
    listbox5var.insert(0,"n= "+str(n))
    listbox5var.insert(1,"Lista de digitos del 153= "+str(digitos153))
    listbox5.selection_set(8)
    time.sleep(0.5)
    listbox5.selection_clear(8)
    con=False
    while not con:
        time.sleep(1)
        listbox5.selection_set(9)
        time.sleep(0.5)
        listbox5.selection_clear(9)
        listbox5var.insert(2,"n<=0(?)= "+str(n<=0))
        if n<=0:
            time.sleep(1)
            listbox5.selection_set(10)
            time.sleep(0.5)
            listbox5.selection_clear(10)
            listbox5var.delete(2)
            con=True
        else:
            time.sleep(1)
            listbox5.selection_set(11)
            time.sleep(0.5)
            listbox5.selection_clear(11)
            time.sleep(1)
            listbox5.selection_set(12)
            time.sleep(0.5)
            listbox5.selection_clear(12)
            listbox5var.delete(0,Tk.END)
            listbox5var.insert(0,"n="+str(n//10))
            listbox5var.insert(1,"Lista de digitos del 153="+str(digitos153+[n%10]))
            time.sleep(1)
            n0=n
            n=n//10
            digitos153=digitos153+[n0%10]
    lista1=[3,5,1]
    lista2=[]
    time.sleep(1)
    listbox5var.delete(0,Tk.END)
    listbox5var.insert(0,"lista1="+str(lista1))
    listbox5var.insert(1,"lista2="+str(lista2))
    listbox5.selection_set(2)
    time.sleep(0.5)
    listbox5.selection_clear(2)
    con=False
    while not con:
        time.sleep(1)
        listbox5.selection_set(2)
        time.sleep(0.5)
        listbox5.selection_clear(2)
        time.sleep(1)
        listbox5.selection_set(3)
        time.sleep(0.5)
        listbox5.selection_clear(3)
        listbox5var.insert(2,"lista1==[](?)= "+str(lista1==[]))
        if lista1==[]:
            time.sleep(1)
            listbox5.selection_set(4)
            time.sleep(0.5)
            listbox5.selection_clear(4)
            listbox5var.delete(0,Tk.END)
            con=True
            Result5.insert(Tk.END,str(sum(lista2))+" es igual a la suma de los cubos de sus dígitos:\n1exp(3) + 5exp(3) + 3exp(3)=\n 1 + 125 + 27 = "+str(sum(lista2)))
        else:
            time.sleep(1)
            listbox5.selection_set(5)
            time.sleep(0.5)
            listbox5.selection_clear(5)
            time.sleep(1)
            listbox5.selection_set(6)
            time.sleep(0.5)
            listbox5.selection_clear(6)
            listbox5var.delete(0,Tk.END)
            listbox5var.insert(0,"lista1="+str(lista1[:-1]))
            listbox5var.insert(1,"lista2="+str(lista2+[lista1[-1]**3]))
            listado=[lista1[-1]**3]
            lista1=lista1[:-1]
            lista2+=listado


#Segunda curiosidad
#Invoca el debugger de la segunda curiosidad 
def botonReceive1532():
    resp=threading.Thread(target=lambda:Debugger1532(LInstruccion))
    resp.start()

#Función que carga el debugger para la segunda curiosidad
def Debugger1532(LInstruccion,n=153,digitos153=[],cont=0):
    if cont==0:
        listbox5.delete(0,Tk.END)
        listbox5var.delete(0,Tk.END)
        Result5.delete(1.0,Tk.END)
        LInstruccion = cargaLista153(LInstruccion)
    time.sleep(1)
    listbox5.yview(8)
    listbox5.selection_set(14)
    time.sleep(0.5)
    listbox5.selection_clear(14)
    time.sleep(1)
    listbox5var.insert(0,"n= "+str(n))
    listbox5var.insert(1,"Lista de digitos del 153= "+str(digitos153))
    listbox5.selection_set(8)
    time.sleep(0.5)
    listbox5.selection_clear(8)
    con=False
    while not con:
        time.sleep(1)
        listbox5.selection_set(9)
        time.sleep(0.5)
        listbox5.selection_clear(9)
        listbox5var.insert(2,"n<=0(?)= "+str(n<=0))
        if n<=0:
            time.sleep(1)
            listbox5.selection_set(10)
            time.sleep(0.5)
            listbox5.selection_clear(10)
            listbox5var.delete(2)
            con=True
        else:
            time.sleep(1)
            listbox5.selection_set(11)
            time.sleep(0.5)
            listbox5.selection_clear(11)
            time.sleep(1)
            listbox5.selection_set(12)
            time.sleep(0.5)
            listbox5.selection_clear(12)
            listbox5var.delete(0,Tk.END)
            listbox5var.insert(0,"n="+str(n//10))
            listbox5var.insert(1,"Lista de digitos del 153="+str(digitos153+[n%10]))
            time.sleep(1)
            n0=n
            n=n//10
            digitos153=digitos153+[n0%10]
    lista1=[3,5,1]
    lista2=[]
    time.sleep(1)
    listbox5var.delete(0,Tk.END)
    listbox5var.insert(0,"lista1="+str(lista1))
    listbox5var.insert(1,"lista2="+str(lista2))
    time.sleep(0.5)
    con=False
    while not con:
        time.sleep(1)
        listbox5.selection_set(14)
        time.sleep(0.5)
        listbox5.selection_clear(14)
        time.sleep(1)
        listbox5.selection_set(15)
        time.sleep(0.5)
        listbox5.selection_clear(15)
        listbox5var.insert(2,"lista1==[](?)= "+str(lista1==[]))
        if lista1==[]:
            time.sleep(1)
            listbox5.selection_set(16)
            time.sleep(0.5)
            listbox5.selection_clear(16)
            time.sleep(1)
            listbox5var.delete(2)
            listbox5var.insert(2,"num= "+str(sum(lista2)))
            num=sum(lista2)
            listbox5.selection_set(17)
            time.sleep(0.5)
            listbox5.selection_clear(17)
            listbox5var.insert(3,"sqrt(num)==int(sqrt(num))(?)= "+str(sqrt(num)==int(sqrt(num))))
            con=True
            time.sleep(1)
            listbox5.selection_set(17)
            time.sleep(0.5)
            listbox5.selection_clear(17)
            Result5.insert(Tk.END,"La suma de los digitos de 153 es: " +  str(num) + " y el " + str(num) + " es un numero cuadrado perfecto")
        else:
            time.sleep(1)
            listbox5.selection_set(19)
            time.sleep(0.5)
            listbox5.selection_clear(19)
            time.sleep(1)
            listbox5.selection_set(20)
            time.sleep(0.5)
            listbox5.selection_clear(20)
            listbox5var.delete(0,Tk.END)
            listbox5var.insert(0,"lista1="+str(lista1[:-1]))
            listbox5var.insert(1,"lista2="+str(lista2+[lista1[-1]]))
            listado=[lista1[-1]]
            lista1=lista1[:-1]
            lista2+=listado


#Tercera curiosidad
##Invoca el debugger de la tercera curiosidad 
def botonReceive1533():
    resp=threading.Thread(target=lambda:Debugger1533(LInstruccion))
    resp.start()

#Funcion que carga el debugger para la tercera curiosidad
def Debugger1533(LInstruccion,n=1,cont=0):
    if cont==0:
        listbox5.delete(0,Tk.END)
        listbox5var.delete(0,Tk.END)
        Result5.delete(1.0,Tk.END)
        LInstruccion = cargaLista153(LInstruccion)
    listbox5.yview(35)
    time.sleep(1)
    listbox5.selection_set(34)
    time.sleep(0.5)
    listbox5.selection_clear(34)
    time.sleep(1)
    listbox5.selection_set(35)
    time.sleep(0.5)
    listbox5.selection_clear(35)
    con=False
    resp=0
    n=1
    while not con:
        listbox5.yview(22)
        listbox5var.delete(0,Tk.END)
        listbox5var.insert(0,"n= "+str(n))
        listbox5var.insert(1,"respuesta= "+str(resp))
        time.sleep(1)
        listbox5.selection_set(22)
        time.sleep(0.5)
        listbox5.selection_clear(22)
        time.sleep(1)
        listbox5.selection_set(23)
        time.sleep(0.5)
        listbox5.selection_clear(23)
        listbox5var.insert(2,"n==17(?)= "+str(n==17))
        if n==17:
            time.sleep(1)
            listbox5.selection_set(24)
            time.sleep(0.5)
            listbox5.selection_clear(24)
            listbox5var.delete(0,Tk.END)
            listbox5var.insert(0,"n= "+str(n))
            listbox5var.insert(1,"respuesta= "+str(resp+n))
            time.sleep(1.5)
            listbox5var.delete(2)
            con=True
        else:
            time.sleep(1)
            listbox5.selection_set(25)
            time.sleep(0.5)
            listbox5.selection_clear(25)
            time.sleep(1)
            listbox5.selection_set(26)
            time.sleep(0.5)
            listbox5.selection_clear(26)
            listbox5var.delete(0,Tk.END)
            listbox5var.insert(0,"n="+str(n+1))
            listbox5var.insert(1,"respuesta="+str(resp+n))
            resp+=n
            n+=1
    time.sleep(1)
    listbox5.yview(35)
    listbox5var.delete(0,Tk.END)
    listbox5var.insert(0,"sumaenteros153()="+str(153))
    listbox5.selection_set(35)
    time.sleep(1)
    listbox5.selection_clear(35)
    con=False
    n=1
    resp=0
    while not con:
        listbox5.yview(22)
        listbox5var.delete(0,Tk.END)
        listbox5var.insert(0,"n= "+str(n))
        listbox5var.insert(1,"respuesta= "+str(resp))
        time.sleep(1)
        listbox5.selection_set(28)
        time.sleep(0.5)
        listbox5.selection_clear(28)
        time.sleep(1)
        listbox5.selection_set(29)
        time.sleep(0.5)
        listbox5.selection_clear(29)
        listbox5var.insert(2,"n==26(?)= "+str(n==26))
        if n==26:
            time.sleep(1)
            listbox5.selection_set(30)
            time.sleep(0.5)
            listbox5.selection_clear(30)
            listbox5var.delete(0,Tk.END)
            listbox5var.insert(0,"n= "+str(n))
            listbox5var.insert(1,"respuesta= "+str(resp+n))
            time.sleep(1.5)
            con=True
        else:
            time.sleep(1)
            listbox5.selection_set(31)
            time.sleep(0.5)
            listbox5.selection_clear(31)
            time.sleep(1)
            listbox5.selection_set(32)
            time.sleep(0.5)
            listbox5.selection_clear(32)
            listbox5var.delete(0,Tk.END)
            listbox5var.insert(0,"n="+str(n+1))
            listbox5var.insert(1,"respuesta="+str(resp+n))
            resp+=n
            n+=1
    listbox5.yview(35)
    time.sleep(0.5)
    listbox5.selection_set(35)
    time.sleep(1)
    listbox5.selection_clear(35)
    listbox5var.delete(0,Tk.END)
    listbox5var.insert(0,"sumaenteros153()="+str(153))
    listbox5var.insert(1,"sumaenteros351()="+str(351))
    time.sleep(1)
    listbox5var.insert(2,"sumaenteros153()==153(?)= "+str(True))
    time.sleep(0.5)
    listbox5var.insert(3,"sumaenteros153()==351(?)= "+str(True))
    time.sleep(1)
    listbox5.selection_set(36)
    time.sleep(0.5)
    Result5.insert(Tk.END,"La suma de los enteros del 1 al 17 es: 153 y del 1 al 26 es: 351")
    listbox5.selection_clear(36)
        

#--------------------------------------------
#Interfaz general
#--------------------------------------------
#Ventana principal
v0=Tk.Tk() #Crea ventana principal
ocultar(v0) #Ejecuta función de ocultar ventana principal
v0.config(bg="black") #Color de fondo de la ventana principal
v0.geometry("1230x650") #Tamaño de la ventana principal
v0.resizable(0,0) #Ventana principal no es maximizable ni minimizable
v0.title("Curiosidades Matemáticas") #Título de la ventana principal

#Ventana inicio
v1=Tk.Toplevel(v0) #Crea ventana de presentación
v1.geometry("680x162") #Tamaño de ventana de presentación
v1.config(bg="black") #Color de fondo de la ventana de presentación
v1.protocol("WM_DELETE_WINDOW", "onexit") #Prohibe que el botón de cerrar tenga efecto
v1.resizable(0,0) #Ventana de presentación no es maximizable ni minimizable
v1.after(3000,cerrar_splashscreen) #Después de tres segundos, cerrar ventana de presentación
imagenini=Tk.PhotoImage(file="Thelol.gif") #Carga imagen para ventana de presentación
Tk.Label(v1,text="CURIOSIDADES\nMATEMÁTICAS",bg="black",fg="white",font=("Verdana",20,"bold"),\
        justify="center").grid(row=1,column=1) #Crea el título de la ventana de presentación
#Labels insertados en ventana de presentacion para agregar informacion extra
Tk.Label(v1,text="Instituto Tecnológico de Costa Rica, 2013", bg="black",fg="light green",\
         font=("SimHei",14), justify="center").grid(row=2,column=1,padx=30,sticky=Tk.S)
Tk.Label(v1,text="Cargando...                  ", bg="black",fg="AntiqueWhite3",\
         font=("SimHei",14), justify="center").grid(row=3,column=1, columnspan=2,padx=25,sticky=Tk.S)
#Label para invocar imagen dentro de ventana principal
Tk.Label(v1, image=imagenini).grid(row=1, rowspan=3, column=2)

#Menu principal
menubarra = Tk.Menu(v0) #Crea la barra de menú
opcionmenu = Tk.Menu(menubarra, tearoff=0) #Crea una secion llamada Opcionmenu
opcionmenu.add_command(label="Créditos", command=creditos) #Adiciona a Opcionmenu una opcion llamada Creditos 
opcionmenu.add_separator() #Agrega un separador
opcionmenu.add_command(label="Salir", command=salir) #Adiciona a Opcionmenu una opcion llamada Salir
menubarra.add_cascade(label="Opciones", menu=opcionmenu)#Crea menu de cascada para Opcionmenu

#Titulo
titulogrande = Tk.Label(v0,text="Curiosidades Matemáticas", relief="sunken", font=("Helvetica",36,"bold"),\
                    justify="center", bg="#2B5484", bd=8, width=20, fg="white").grid(row=1,column=1,columnspan=6,ipadx=309,sticky=Tk.W) #Crea titulo para ventana principal

#Pestañas
pestana=Ttk.Notebook(v0) #Crea pestañas para ventana principal
#Crea diferentes cuadros para cada funcion
tab0=Tk.Frame(pestana)
tab0.config(width="2000", height="800",bg="#5BA3D0")
tab1=Tk.Frame(pestana)
tab1.config(width="2000", height="800",bg="#5BA3D0")
tab2=Tk.Frame(pestana)
tab2.config(width="2000", height="800",bg="#5BA3D0")
tab3=Tk.Frame(pestana)
tab3.config(width="2000", height="800",bg="#5BA3D0")
tab4=Tk.Frame(pestana)
tab4.config(width="2000", height="800",bg="#5BA3D0")
#Agrega nombre a cada pestaña, donde cada una se relaciona con un cuadro creado
pestana.add(tab0, text="Conjetura de Goldbach")
pestana.add(tab1, text="Números amigos")
pestana.add(tab2, text="Triángulo de Pascal")
pestana.add(tab3, text="Número triangular")
pestana.add(tab4, text="Curiosidades del 153")
pestana.grid(row=2, column=1, sticky="S")

#Textos de indicación
#Agrega un texto indicando que hacer, parra cada cuadro
txtindGoldbach=Tk.Label(tab0,text="Favor insertar un numero par:",bg="#5BA3D0").grid(row=1, column=1, pady=25)
txtindAmigos=Tk.Label(tab1,text="Favor insertar dos numeros:",bg="#5BA3D0").grid(row=1, column=1, rowspan=2, pady=20, sticky=Tk.S)
txtindPascal=Tk.Label(tab2,text="Favor insertar el escalón\ndeseado del Triangulo de Pascal:"\
                      ,bg="#5BA3D0").grid(row=1, column=1, rowspan=2, pady=15, padx=5)
txtindTriangular=Tk.Label(tab3,text="Favor insertar un numero:",bg="#5BA3D0").grid(row=1, column=1, pady=25)
txtind153=Tk.Label(tab4,text="Escoja una de las curiosidades:",bg="#5BA3D0").place(x=100, y=2)

#Métodos de entrada
#Crea los métodos de entrada para las Entryboxes
EntrGoldbach=Tk.IntVar()
EntrAmigos1=Tk.IntVar()
EntrAmigos2=Tk.IntVar()
EntrPascal=Tk.IntVar()
EntrTriangular=Tk.IntVar()

#Entrybox
#Crea una Entrybox para recibir datos por parte del usuario
EntryGoldbach=Tk.Entry(tab0,textvariable=EntrGoldbach, bd=3).grid(row=1, column=2)
EntryAmigos1=Tk.Entry(tab1,textvariable=EntrAmigos1, bd=3).grid(row=1, column=2)
EntryAmigos2=Tk.Entry(tab1,textvariable=EntrAmigos2, bd=3).grid(row=2, column=2, sticky="N")
EntryPascal=Tk.Entry(tab2,textvariable=EntrPascal, bd=3).grid(row=1, rowspan=2, column=2)
EntryTriangular=Tk.Entry(tab3,textvariable=EntrTriangular, bd=3).grid(row=1, column=2)

#Botones
#Crea botones para ejecutar las funciones principales del proyecto programado
BotonGoldbach=Tk.Button(tab0, text="Calcular", cursor="target",\
                       command=botonReceiveGoldbach).grid(row=1, column=3, padx=3)
BotonGoldbachNoDebugger=Tk.Button(tab0, text="Calcular (Sin usar debugger)", cursor="target",\
                       command=GoldbachNoDebugger).place(x=180,y=52)
BotonAmigos=Tk.Button(tab1, text="Calcular", cursor="target", command=botonReceiveAmigos).grid(row=1, column=3, rowspan=2, padx=3)
BotonAmigosNoDebugger=Tk.Button(tab1, text="Calcular (Sin usar debugger)", cursor="target", command=numerosAmigos).place(x=150,y=57)
BotonPascal=Tk.Button(tab2, text="Calcular", cursor="target", \
                      command=botonReceivePascal).grid(row=1, rowspan=2, column=3, padx=3)
BotonPascalNoDebugger=Tk.Button(tab2, text="Calcular (Sin usar debugger)", cursor="target",\
                       command=trianguloPascalNoDebugger).place(x=180,y=52)
BotonTriangular=Tk.Button(tab3, text="Calcular", cursor="target",\
                        command=botonReceiveTriangular).grid(row=1, column=3, padx=3)
BotonTriangularNoDebugger=Tk.Button(tab3, text="Calcular (Sin usar debugger)", cursor="target",\
                       command=numerotriangularNoDebugger).place(x=160,y=52)
Boton153=Tk.Button(tab4, text="Primera Curiosidad  ", cursor="target", command= botonReceive1531).place(x=2, y=25)
SegBoton153=Tk.Button(tab4, text="Segunda Curiosidad", cursor="target", command= botonReceive1532).place(x=126, y=25)
TerBoton153=Tk.Button(tab4, text="Tercera Curiosidad  ", cursor="target", command= botonReceive1533).place(x=250, y=25)

#Debugger
#Componentes de la interfaz de Debugger
'''Pestaña Goldbach'''
#Listbox con código
codalgGoldbach=Tk.Label(tab0,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").grid(row=1,column=4,padx=60,sticky=Tk.S)
frame1 = Tk.Frame(tab0, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame1)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox1 = Tk.Listbox(frame1, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=67, height=13)
listbox1.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox1.yview)
frame1.grid(row=4, column=4, columnspan=3)
#Listbox con variables
TituloVariables=Tk.Label(tab0,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=110, y=80)
frame1var = Tk.Frame(tab0, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame1var)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox1var= Tk.Listbox(frame1var, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=50, height=10)
listbox1var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox1var.yview)
frame1var.place(x=20, y=120)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab0,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=320, y=320)
frame1res = Tk.Frame(tab0, bd=2, relief=Tk.SUNKEN, width=10, height=20)
yscrollbar = Tk.Scrollbar(frame1res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result1 = Tk.Text(frame1res, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, height=10, width=91)
Result1.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=Result1.yview)
frame1res.place(x=20, y=370)          
#Textbox con información
TituloExplicacion=Tk.Label(tab0,text="Explicación", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=800, y=32)
frame1exp = Tk.Frame(tab0, bd=2, relief=Tk.SUNKEN, width=10, height=20)
Exp1 = Tk.Text(frame1exp, bd=0,bg="black",fg="white", height=25, width=50)
Exp1.insert(Tk.END,explicaGoldbach)
Exp1.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
frame1exp.place(x=800, y=70)         


'''Pestaña Amigos'''
#Listbox con código
codalgAmigos=Tk.Label(tab1,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").grid(row=1,rowspan=2,column=4,padx=60,sticky=Tk.S)
frame2 = Tk.Frame(tab1, bd=2, relief=Tk.SUNKEN, width=100, height=60)
yscrollbar = Tk.Scrollbar(frame2)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox2 = Tk.Listbox(frame2, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=69, height=15)
listbox2.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox2.yview)
frame2.grid(row=4, column=4, columnspan=3)
#Listbox con variables
TituloVariables=Tk.Label(tab1,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=110, y=85)
frame2var = Tk.Frame(tab1, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame2var)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox2var= Tk.Listbox(frame2var, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=48, height=11)
listbox2var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox2var.yview)
frame2var.place(x=20, y=120)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab1,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=320, y=330)
frame2res = Tk.Frame(tab1, bd=2, relief=Tk.SUNKEN, width=10, height=20)
yscrollbar = Tk.Scrollbar(frame2res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result2 = Tk.Text(frame2res, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, height=10, width=91)
Result2.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=Result2.yview)
frame2res.place(x=20, y=370)          
#Textbox con información
TituloExplicacion=Tk.Label(tab1,text="Explicación", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=800, y=32)
frame2exp = Tk.Frame(tab1, bd=2, relief=Tk.SUNKEN, width=10, height=20)
Exp2 = Tk.Text(frame2exp, bd=0,bg="black",fg="white", height=25, width=50)
Exp2.insert(Tk.END,explicaAmigos)
Exp2.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
frame2exp.place(x=800, y=70)         


'''Pestaña Pascal'''
#Listbox con código
codalgPascal=Tk.Label(tab2,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").grid(row=1,rowspan=2,column=4,padx=50,sticky=Tk.S)
frame3 = Tk.Frame(tab2, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame3)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox3 = Tk.Listbox(frame3, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=65, height=14)
listbox3.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox3.yview)
frame3.place(x=370, y=70)
#Listbox con variables
TituloVariables=Tk.Label(tab2,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=110, y=80)
frame3var = Tk.Frame(tab2, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame3var)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox3var= Tk.Listbox(frame3var, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=53, height=11)
listbox3var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox3var.yview)
frame3var.place(x=17, y=118)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab2,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=320, y=330)
frame3res = Tk.Frame(tab2, bd=2, relief=Tk.SUNKEN, width=10, height=20)
yscrollbar = Tk.Scrollbar(frame3res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result3 = Tk.Text(frame3res, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, height=10, width=91)
Result3.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=Result3.yview)
frame3res.place(x=20, y=370)
#Textbox con información
TituloExplicacion=Tk.Label(tab2,text="Explicación", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=800, y=32)
frame3exp = Tk.Frame(tab2, bd=2, relief=Tk.SUNKEN, width=10, height=20)
Exp3 = Tk.Text(frame3exp, bd=0,bg="black",fg="white", height=25, width=50)
Exp3.insert(Tk.END,explicaPascal)
Exp3.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
frame3exp.place(x=800, y=70) 

          
'''Pestaña Triangular'''
#Listbox con código
codalgTriangular=Tk.Label(tab3,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").grid(row=1,column=4,padx=70,sticky=Tk.S)
frame4res = Tk.Frame(tab3, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame4res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox4 = Tk.Listbox(frame4res, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=70, height=14)
listbox4.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox4.yview)
frame4res.grid(row=4, column=4, columnspan=3)
#Listbox con variables
TituloVariables=Tk.Label(tab3,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=110, y=80)
frame4resvar = Tk.Frame(tab3, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame4resvar)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox4var= Tk.Listbox(frame4resvar, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=47, height=11)
listbox4var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox4var.yview)
frame4resvar.place(x=17, y=118)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab3,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").grid(row=5,column=1,columnspan=4,pady=8,padx=60,sticky=Tk.S)
frame4res = Tk.Frame(tab3, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame4res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result4= Tk.Text(frame4res, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=90, height=11)
Result4.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox4var.yview)
frame4res.grid(row=6, column=1, columnspan=4)
#Textbox con información
TituloExplicacion=Tk.Label(tab3,text="Explicación", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=800, y=32)
frame4exp = Tk.Frame(tab3, bd=2, relief=Tk.SUNKEN, width=10, height=20)
Exp4 = Tk.Text(frame4exp, bd=0,bg="black",fg="white", height=25, width=50)
Exp4.insert(Tk.END,explicaTriangular)
Exp4.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
frame4exp.place(x=800, y=70) 


'''Pestaña 153'''
#Listbox con código
codalg153=Tk.Label(tab4,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=410,y=36)
frame5res = Tk.Frame(tab4, bd=2, relief=Tk.SUNKEN, width=10, height=50,bg="white")
yscrollbar = Tk.Scrollbar(frame5res, cursor="tcross")
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox5 = Tk.Listbox(frame5res, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=66, height=13)
listbox5.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox5.yview)
frame5res.place(x=360, y=77)
#Listbox con variables
TituloVariables=Tk.Label(tab4,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=108,y=80)
frame5var = Tk.Frame(tab4, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame5var, cursor="tcross")
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox5var= Tk.Listbox(frame5var, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=50, height=10)
listbox5var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox5var.yview)
frame5var.place(x=20, y=120)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab4,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=325, y=330)
frame5res = Tk.Frame(tab4, bd=2, relief=Tk.SUNKEN, width=100, height=50)
yscrollbar = Tk.Scrollbar(frame5res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result5= Tk.Text(frame5res, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=92, height=10)
Result5.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
yscrollbar.config(command=listbox5var.yview)
frame5res.place(x=20, y=375)
#Textbox con información
TituloExplicacion=Tk.Label(tab4,text="Explicación", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#5BA3D0", fg="#163562").place(x=800, y=32)
frame5exp = Tk.Frame(tab4, bd=2, relief=Tk.SUNKEN, width=10, height=20)
Exp5 = Tk.Text(frame5exp, bd=0,bg="black",fg="white", height=25, width=50)
Exp5.insert(Tk.END,explica153)
Exp5.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
frame5exp.place(x=800, y=70) 


#Invocadores de todo el código, a la hora de correr el mismo          
v0.config(menu=menubarra)
v0.mainloop()
