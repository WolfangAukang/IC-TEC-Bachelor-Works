## -*- coding: cp1252 -*-
import Tkinter as Tk
import ttk as Ttk
from tkMessageBox import *
import time
import threading

#--------------------------------------------
#Variables globales
#--------------------------------------------
global LInstruccion
LInstruccion=[]  #lista global donde queda la carga del archivo..

#--------------------------------------------
#Comandos generales
#--------------------------------------------
#Comando para confirmar selección y salir totalmente del programa
def salir(): 
    salida=askokcancel("Está seguro?", "Deseas salir del programa?")
    if salida==True:
        v0.destroy()
#Comando para mostrar message box con créditos adentros
def creditos(): showinfo("Créditos", "Este programa fue realizado por:\nKevin Alvarado\nDavid Obando\nPedro Rodríguez\n"\
                     "Estudiantes cursantes de Taller de Programación\ndel Instituto Tecnológico de Costa Rica.")

#Comando para mostrar message box con explicación sobre Conjetura de Goldbach
def explicaGoldbach(): showinfo("Explicación sobre la Conjetura de Goldbach","En teoría de números, la conjetura de Goldbach es uno de los problemas abiertos más antiguos en matemáticas.\n"\
                               "A veces se le califica del problema más difícil en la historia de esta ciencia. Su enunciado es el siguiente:\n\n"\
                               "Todo número par mayor que 2 puede escribirse como suma de dos números primos.\n\n"\
                               "Cabe notar que se puede emplear dos veces el mismo número primo.\n\n"\
                               "Por ejemplo= 4=2+2, 6=3+3, 8=3+5, 10=3+7, 12=5+7, 14=7+7...")

#Comando para mostrar message box con explicación sobre los números amigos
def explicaAmigos(): showinfo("Explicación sobre los números amigos", "Se cuenta que en una ocasión le preguntaron a Pitágoras:\n"\
                            "-Para ti qué es un amigo?\nY  respondió:\n-Otro yo\n"
                            "La aplicación de esta forma de concebir la amistad a la Teoría de los  Números, condujo a decir que:\n"\
                            "Dos números son amigos cuando cada uno de ellos es  igual a la suma de los divisores del otro.\n\nPor ejemplo:\n\n"\
                            "Divisores de 284: 1, 2, 4, 71, 142\n\n"\
                            "Divisores de 220: 1 , 2 , 4 , 5 , 10 , 11 , 20 , 22 , 44 , 55 , 110\n\n"\
                            "284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110\n\n"\
                            "220 = 1 + 2 + 4 + 71 + 142\n\n"\
                            "Así, que 220 y 284 son números amigos.")

#Comando para mostrar message box con explicación sobre el Triángulo de Pascal
def explicaPascal(): showinfo("Explicación sobre el Triángulo de Pascal", "Es un árbol invertido o un triángulo "\
                              "donde todos sus bordes son 1 y los valores internos son la suma de los dos valores "\
                              "que se encuentren justo por encima de él.\nLa utilidad de construir un triángulo de Pascal "\
                              "se debe a su directa relación con el cálculo de los números combinatorios y el uso de la fórmula factorial.")

#Comando para mostrar message box con explicación sobre los números triangulares
def explicaTriangular(): showinfo("Explicación sobre los números triangulares", "Es aquel que puede recomponerse en la forma de un "\
                                  "triángulo equilátero (por convención, el primer número triangular es el 1).\nPitágoras y los Pitagóricos "\
                                  "consideraban sagrado el 10 escrito en forma triangular, al cual lo llamaban Tetraktys.")

#Comando para mostrar message box con explicación sobre las curiosidades del 153
def explica153(): showinfo("Explicación sobre el número 153", "1.- Es el número más pequeño que puede ser expresado como la suma de los cubos de sus dígitos:\n"\
                                       "153 = 13 + 53 + 33 = 1 + 125+ 27\n"\
                                       "2.- La suma de sus dígitos es un cuadrado perfecto:\n"\
                                       "1 + 5 + 3 = 9 = 32\n"\
                                       "3.- Puede ser expresado como la suma de todos los números enteros del 1 al 17:\n"\
                                       "153 = 1 + 2 + 3 + 4 +…+ 15 + 16 + 17\n"\
                                       "Esto significa que 153 es el decimoséptimo número triangular. Como su inverso, 351,"\
                                       "también es un número triangular (suma del 1 hasta el 26) podemos decir que 153"\
                                       "es un número triangular invertible.")

#Cierra la ventana
def mostrar(ventana): return ventana.deiconify

#Abre la ventana
def ocultar(ventana): return ventana.withdraw()

#Ejecutar ventana después de un cierto tiempo
def ejecutar(f): v0.after(100, f)

#Comando para mostrar la ventana de inicio
def cerrar_splashscreen():
    ejecutar(ocultar(v1))
    ejecutar(mostrar(v0))

#--------------------------------------------
#Funciones principales
#--------------------------------------------

#Goldbach
def primo(n,div=2):
    if div>(n//2):
        return True
    else:
        if n%div==0:
            return False
        else:
            return primo(n, div+1)

def Goldbachaux(num,sumador=2, res=[]):
    if sumador==num:
        return res
    else:
        if primo(sumador) and primo(num-sumador) and sumador!=1 and (num-sumador)!=1:
            return Goldbachaux(num,sumador+1,res+[[sumador, num-sumador]])
        else:
            return Goldbachaux(num,sumador+1,res)

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

def GoldbachNoDebugger():
    num=EntrGoldbach.get()
    if num<=2 or num%2!=0:
        return showinfo("Error","Error, lo insertado no es par y/o no es mayor a dos")
    else:
        result=convertirlistaastring(Goldbachaux(num))
        return showinfo("Respuesta a la Conjetura de Goldbach"\
                        ,"La(s) suma(s) entre numeros primos que se rezlizan para dar "+str(num)+" son "+ str(result))
    
#Numeros Amigos
def divisoresAux(num, numz, hilera): #AUXILIAR DE LA FUNCION QUE OBTIENE DIVISORES
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

def divisores(num): #FUNCION PARA OBTENER LOS DIVISORES DE UN NUMERO
    lista=[]
    hilera=""
    numz=num
    return divisoresAux(num, numz, hilera)

def amigosAux(num, num2, cont): #AUXILIAR DE LA FUNCION PRINCIPAL    
    if num2==2:
        return cont
    else:
        if num%(num2-1)==0:
            cont=cont+(num2-1)
            return amigosAux(num, num2-1, cont)
        else:
            return amigosAux(num, num2-1, cont)

def sumadivisores(num): #FUNCION QUE SUMA LOS DIVISORES DE UN NUMERO
    return amigosAux(num, num, 1)

def numerosAmigos(): #FUNCION PRINCIPAL
    num1=int(EntrAmigos1.get())
    num2=int(EntrAmigos2.get())
    numx=num1
    numy=num2
    if num1==amigosAux(num2, numy, 1)and num2==amigosAux(num1,numx,1):
        return showinfo("Respuesta","-Divisores del " +str(num1)+":\n{"+str(divisores(num1))+"}\n-La suma da "+str(num2)+"\n \n -Divisores del " +str(num2)+":\n{"+str(divisores(num2))+"}\n-La suma da "+str(num1)+"\n \nPor lo tanto "+str(num1)+" y "+str(num2)+" SON numeros amigos.")
    else:
        return showinfo("Respuesta", "-Divisores del " +str(num1)+":\n{"+str(divisores(num1))+"}\n-La suma da "+str(sumadivisores(num1))+"\n \n -Divisores del " +str(num2)+":\n{"+str(divisores(num2))+"}\n-La suma da "+str(sumadivisores(num2))+"\n \nPor lo tanto "+str(num1)+" y "+str(num2)+" NO SON numeros amigos.")

#Triangulo de Pascal
def factor(num, fac=0):
    if num<10**fac:
        return fac
    else:
        return factor(num,fac+1)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def calcPascal(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))

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

def trianguloPascalNoDebugger():
    poslleg=int(EntrPascal.get())
    return showinfo("Triangulo de Pascal","Los escalones son:\n"+trianguloPascalAux(0,0,poslleg,0,""))

#Numero Triangular
def numerotriangularAux(n):
    if n==1:
        return 1
    else:
        return n + numerotriangularAux(n-1)

def espacio(n):
    if n==0:
        return ""
    else:
        return " "+espacio(n-1)
    
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

def numerotriangularNoDebugger():
    n=int(EntrTriangular.get())
    if n>0:
        return showinfo("Respuesta","El numero triangular de "+str(n)+" es "+str(numerotriangularAux(n))+".\nEl ejemplo "\
                        "está aquí:\n\n"+demostracion(n)+"\n\nDentro del triángulo hay "+str(numerotriangularAux(n))+\
                        " asteriscos")
    else:
        return showinfo("Error", "Error, datos no validos")

#Curiosidades 153
def primera():
    return showinfo("Primera Curiosidad","153 es igual a la suma de los cubos de sus dígitos:\n1exp(3) + 5exp(3) + 3exp(3)=\n 1 + 125 + 27=\n153")
def segunda():
    return showinfo("Segunda Curiosidad","La suma de sus dígitos es un cuadrado perfecto:\n1 + 5 + 3 = 9\n9 es un número al cuadrado perfecto porque 3exp(2)=9")
def tercera():
    return showinfo("Tercera Curiosidad","La suma de los número del 1 al 17 = 153\nPor lo tanto 153 es el decimo sétimo número triangular \nLa suma de los enteros del 1 al 26 es: 351.\n\nPor es el 153 es un numero triangular invertible")

#--------------------------------------------
#Funciones Debugger
#--------------------------------------------

#Pestaña de Goldbach
#Carga el código del ejercicio en una lista, para imprimirlo en la listbox de la pestaña de Goldbach
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

#Confirma los datos insertados por el usuario
def botonReceiveGoldbach():
    n=EntrGoldbach.get()
    if n%2==0 and n>2:
        resp=threading.Thread(target=lambda:DebuggerGoldbach(LInstruccion,n))
        resp.start()
    else:
        return showinfo("Error","Error, lo insertado no es par y/o no es mayor a dos")

#Realiza el proceso de debug en la pestaña de Goldbach
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

#Numeros amigos



#Triangulo de Pascal
#Carga el código del ejercicio en una lista, para imprimirlo en la listbox de la pestaña de Pascal
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

def botonReceivePascal():
    n=EntrPascal.get()
    if n>=0:
        resp=threading.Thread(target=lambda:DebuggerPascal(LInstruccion,n))
        resp.start()
    else:
        return showinfo("Error","Error, lo insertado no es mayor ni igual a 0")

#Realiza el proceso de debug en la pestaña de Pascal
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
                listbox3var.insert(0,"Num= "+str(num))
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
                listbox3var.insert(2,"Num==0(?) "+str(num==0))
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
                listbox3var.insert(0,"Num= "+str(num))
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
                listbox3var.insert(2,"Num==0(?) "+str(num==0))
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
                listbox3var.insert(0,"Num= "+str(num))
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
                listbox3var.insert(2,"Num==0(?) "+str(num==0))
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
            numact=numact+1
            con=calcPascal(posact,numact)
            resp=factor(con,0)
            impr=impr*10**(resp)+con
            cont+=1
            return DebuggerPascal(LInstruccion,poslleg, numact, posact, impr, res, cont)

#Numero triangular
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

#Confirma los datos insertados por el usuario
def botonReceiveTriangular():
    n=EntrTriangular.get()
    if n>=1:
        resp=threading.Thread(target=lambda:DebuggerTriangular(LInstruccion,n,n))
        resp.start()
    else:
        return showinfo("Error","Error, lo insertado no es mayor ni igual a 1")

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
                            "triangulo hay "+str(res)+" asteriscos")
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


#Curiosidades del 153

#--------------------------------------------
#Interfaz general
#--------------------------------------------
#Ventana principal
v0=Tk.Tk()
ocultar(v0)
v0.config(bg="black")
v0.geometry("790x660")
v0.resizable(0,0)
#v0.protocol("WM_DELETE_WINDOW", "onexit")
v0.title("Curiosidades Matemáticas")

#Ventana inicio
v1=Tk.Toplevel(v0)
v1.geometry("680x162")
v1.config(bg="black")
v1.protocol("WM_DELETE_WINDOW", "onexit")
v1.resizable(0,0)
v1.after(3000,cerrar_splashscreen)
imagenini=Tk.PhotoImage(file="Thelol.gif")

Tk.Label(v1,text="CURIOSIDADES\nMATEMÁTICAS",bg="black",fg="white",font=("Verdana",20,"bold"),\
        justify="center").grid(row=1,column=1)
Tk.Label(v1,text="Instituto Tecnológico de Costa Rica, 2013", bg="black",fg="light green",\
         font=("SimHei",14), justify="center").grid(row=2,column=1,padx=30,sticky=Tk.S)
Tk.Label(v1,text="Cargando...                  ", bg="black",fg="AntiqueWhite3",\
         font=("SimHei",14), justify="center").grid(row=3,column=1, columnspan=2,padx=25,sticky=Tk.S)
Tk.Label(v1, image=imagenini).grid(row=1, rowspan=3, column=2)


#Menu principal
menubarra = Tk.Menu(v0)
opcionmenu = Tk.Menu(menubarra, tearoff=0)
opcionmenu.add_command(label="Créditos", command=creditos)
opcionmenu.add_separator()
opcionmenu.add_command(label="Salir", command=salir)
menubarra.add_cascade(label="Opciones", menu=opcionmenu)
explicamenu = Tk.Menu(menubarra, tearoff=0)
explicamenu.add_command(label="Conjetura de Goldbach", command=explicaGoldbach)
explicamenu.add_command(label="Números Amigos", command=explicaAmigos)
explicamenu.add_command(label="Triángulo de Pascal", command=explicaPascal)
explicamenu.add_command(label="Número Triangular", command=explicaTriangular)
explicamenu.add_command(label="Curiosidades del 153", command=explica153)
menubarra.add_cascade(label="Acerca de las funciones", menu=explicamenu)


#Titulo
titulogrande = Tk.Label(v0,text="Curiosidades Matemáticas", relief="raised", font=("Helvetica",36,"bold"),\
                    justify="center", bg="white").grid(row=1,column=1,columnspan=6,ipadx=100,sticky=Tk.W)

#Pestañas
pestana=Ttk.Notebook(v0)
tab0=Tk.Frame(pestana)
tab0.config(width="1000", height="400",bg="#2E64FE")
tab1=Tk.Frame(pestana)
tab1.config(width="1000", height="400",bg="#2E64FE")
tab2=Tk.Frame(pestana)
tab2.config(width="1000", height="400",bg="#2E64FE")
tab3=Tk.Frame(pestana)
tab3.config(width="1000", height="400",bg="#2E64FE")
tab4=Tk.Frame(pestana)
tab4.config(width="1000", height="400",bg="#2E64FE")
pestana.add(tab0, text="Conjetura de Goldbach")
pestana.add(tab1, text="Números amigos")
pestana.add(tab2, text="Triángulo de Pascal")
pestana.add(tab3, text="Número triangular")
pestana.add(tab4, text="Curiosidades del 153")
pestana.grid(row=2, column=1, sticky="S")

#Textos de indicación
txtindGoldbach=Tk.Label(tab0,text="Favor insertar un numero par:",bg="#2E64FE").grid(row=1, column=1, pady=25)
txtindAmigos=Tk.Label(tab1,text="Favor insertar dos numeros:",bg="#2E64FE").grid(row=1, column=1, rowspan=2, pady=20, sticky=Tk.S)
txtindPascal=Tk.Label(tab2,text="Favor insertar el escalón\ndeseado del Triangulo de Pascal:"\
                      ,bg="#2E64FE").grid(row=1, column=1, rowspan=2, pady=15, padx=5)
txtindTriangular=Tk.Label(tab3,text="Favor insertar un numero:",bg="#2E64FE").grid(row=1, column=1, pady=25)
txtind153=Tk.Label(tab4,text="Escoja una de las curiosidades",bg="#2E64FE").place(x=2, y=2)

#Métodos de entrada
EntrGoldbach=Tk.IntVar()
EntrAmigos1=Tk.IntVar()
EntrAmigos2=Tk.IntVar()
EntrPascal=Tk.IntVar()
EntrTriangular=Tk.IntVar()

#Entrybox
EntryGoldbach=Tk.Entry(tab0,textvariable=EntrGoldbach, bd=3).grid(row=1, column=2)
EntryAmigos1=Tk.Entry(tab1,textvariable=EntrAmigos1, bd=3).grid(row=1, column=2)
EntryAmigos2=Tk.Entry(tab1,textvariable=EntrAmigos2, bd=3).grid(row=2, column=2, sticky="N")
EntryPascal=Tk.Entry(tab2,textvariable=EntrPascal, bd=3).grid(row=1, rowspan=2, column=2)
EntryTriangular=Tk.Entry(tab3,textvariable=EntrTriangular, bd=3).grid(row=1, column=2)

#Botones
BotonGoldbach=Tk.Button(tab0, text="Calcular", cursor="target",\
                       command=botonReceiveGoldbach).grid(row=1, column=3, padx=3)
BotonGoldbachNoDebugger=Tk.Button(tab0, text="Calcular (Sin usar debugger)", cursor="target",\
                       command=GoldbachNoDebugger).place(x=180,y=52)
BotonAmigos=Tk.Button(tab1, text="Calcular", cursor="target", command=numerosAmigos).grid(row=1, column=3, rowspan=2, padx=3)
BotonPascal=Tk.Button(tab2, text="Calcular", cursor="target", \
                      command=botonReceivePascal).grid(row=1, rowspan=2, column=3, padx=3)
BotonPascalNoDebugger=Tk.Button(tab2, text="Calcular (Sin usar debugger)", cursor="target",\
                       command=trianguloPascalNoDebugger).place(x=180,y=52)
BotonTriangular=Tk.Button(tab3, text="Calcular", cursor="target",\
                        command=botonReceiveTriangular).grid(row=1, column=3, padx=3)
BotonTriangularNoDebugger=Tk.Button(tab3, text="Calcular (Sin usar debugger)", cursor="target",\
                       command=numerotriangularNoDebugger).place(x=160,y=52)
Boton153=Tk.Button(tab4, text="Primera Curiosidad  ", cursor="target", command= primera).place(x=2, y=25)
SegBoton153=Tk.Button(tab4, text="Segunda Curiosidad", cursor="target", command= segunda).place(x=126, y=25)
TerBoton153=Tk.Button(tab4, text="Tercera Curiosidad  ", cursor="target", command= tercera).place(x=250, y=25)

#Debugger
'''Pestaña Goldbach'''
#Listbox con código
codalgGoldbach=Tk.Label(tab0,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").grid(row=1,column=4,padx=60,sticky=Tk.S)
frame1 = Tk.Frame(tab0, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame1, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame1)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox1 = Tk.Listbox(frame1, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=67, height=13)
listbox1.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox1.xview)
yscrollbar.config(command=listbox1.yview)
frame1.grid(row=4, column=4, columnspan=3)
#Listbox con variables
TituloVariables=Tk.Label(tab0,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=110, y=80)
frame1var = Tk.Frame(tab0, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame1var, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame1var)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox1var= Tk.Listbox(frame1var, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=50, height=10)
listbox1var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox1var.xview)
yscrollbar.config(command=listbox1var.yview)
frame1var.place(x=20, y=120)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab0,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=320, y=320)
frame1res = Tk.Frame(tab0, bd=2, relief=Tk.SUNKEN, width=10, height=20)
xscrollbar = Tk.Scrollbar(frame1res, orient=Tk.HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame1res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result1 = Tk.Text(frame1res, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, height=10, width=91)
Result1.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=Result1.xview)
yscrollbar.config(command=Result1.yview)
frame1res.place(x=20, y=370)          

'''Pestaña Amigos'''
#Listbox con código
codalgAmigos=Tk.Label(tab1,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").grid(row=1,rowspan=2,column=4,padx=60,sticky=Tk.S)
frame2 = Tk.Frame(tab1, bd=2, relief=Tk.SUNKEN, width=100, height=60)
xscrollbar = Tk.Scrollbar(frame2, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame2)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox2 = Tk.Listbox(frame2, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=69, height=15)
listbox2.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox2.xview)
yscrollbar.config(command=listbox2.yview)
frame2.grid(row=4, column=4, columnspan=3)
#Listbox con variables
TituloVariables=Tk.Label(tab1,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=110, y=80)
frame2var = Tk.Frame(tab1, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame2var, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame2var)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox2var= Tk.Listbox(frame2var, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=48, height=11)
listbox2var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox2var.xview)
yscrollbar.config(command=listbox2var.yview)
frame2var.place(x=20, y=120)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab1,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=320, y=330)
frame2res = Tk.Frame(tab1, bd=2, relief=Tk.SUNKEN, width=10, height=20)
xscrollbar = Tk.Scrollbar(frame2res, orient=Tk.HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame2res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result2 = Tk.Text(frame2res, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, height=10, width=91)
Result2.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=Result2.xview)
yscrollbar.config(command=Result2.yview)
frame2res.place(x=20, y=370)          

'''Pestaña Pascal'''
#Listbox con código
codalgPascal=Tk.Label(tab2,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").grid(row=1,rowspan=2,column=4,padx=50,sticky=Tk.S)
frame3 = Tk.Frame(tab2, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame3, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame3)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox3 = Tk.Listbox(frame3, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=65, height=14)
listbox3.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox3.xview)
yscrollbar.config(command=listbox3.yview)
frame3.place(x=370, y=70)
#Listbox con variables
TituloVariables=Tk.Label(tab2,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=110, y=80)
frame3var = Tk.Frame(tab2, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame3var, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame3var)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox3var= Tk.Listbox(frame3var, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=53, height=11)
listbox3var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox3var.xview)
yscrollbar.config(command=listbox3var.yview)
frame3var.place(x=17, y=118)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab2,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=320, y=330)
frame3res = Tk.Frame(tab2, bd=2, relief=Tk.SUNKEN, width=10, height=20)
xscrollbar = Tk.Scrollbar(frame3res, orient=Tk.HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame3res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result3 = Tk.Text(frame3res, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, height=10, width=91)
Result3.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=Result3.xview)
yscrollbar.config(command=Result3.yview)
frame3res.place(x=20, y=370)
          
'''Pestaña Triangular'''
#Listbox con código
codalgTriangular=Tk.Label(tab3,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").grid(row=1,column=4,padx=70,sticky=Tk.S)
frame4res = Tk.Frame(tab3, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame4res, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame4res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox4 = Tk.Listbox(frame4res, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=70, height=14)
listbox4.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox4.xview)
yscrollbar.config(command=listbox4.yview)
frame4res.grid(row=4, column=4, columnspan=3)
#Listbox con variables
TituloVariables=Tk.Label(tab3,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=110, y=80)
frame4resvar = Tk.Frame(tab3, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame4resvar, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame4resvar)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox4var= Tk.Listbox(frame4resvar, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=47, height=11)
listbox4var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox4var.xview)
yscrollbar.config(command=listbox4var.yview)
frame4resvar.place(x=17, y=118)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab3,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").grid(row=5,column=1,columnspan=4,pady=8,padx=60,sticky=Tk.S)
frame4res = Tk.Frame(tab3, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame4res, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame4res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result4= Tk.Text(frame4res, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=90, height=11)
Result4.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox4var.xview)
yscrollbar.config(command=listbox4var.yview)
frame4res.grid(row=6, column=1, columnspan=4)

'''Pestaña 153'''
#Listbox con código
codalg153=Tk.Label(tab4,text="Algoritmo de resolución", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=410,y=36)
frame5res = Tk.Frame(tab4, bd=2, relief=Tk.SUNKEN, width=10, height=50,bg="white")
xscrollbar = Tk.Scrollbar(frame5res, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame5res, cursor="tcross")
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox5 = Tk.Listbox(frame5res, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=66, height=13)
listbox5.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox5.xview)
yscrollbar.config(command=listbox5.yview)
frame5res.place(x=360, y=77)
#Listbox con variables
TituloVariables=Tk.Label(tab4,text="Variables", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=108,y=80)
frame5var = Tk.Frame(tab4, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame5var, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame5var, cursor="tcross")
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
listbox5var= Tk.Listbox(frame5var, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=50, height=10)
listbox5var.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox5var.xview)
yscrollbar.config(command=listbox5var.yview)
frame5var.place(x=20, y=120)
#Textbox con respuesta
TituloRespuesta=Tk.Label(tab4,text="Resultado", font=("Verdana",20),\
                       justify=Tk.CENTER,bg="#2E64FE").place(x=325, y=330)
frame5res = Tk.Frame(tab4, bd=2, relief=Tk.SUNKEN, width=100, height=50)
xscrollbar = Tk.Scrollbar(frame5res, orient=Tk.HORIZONTAL, cursor="tcross")
xscrollbar.grid(row=1, column=0, sticky=Tk.E+Tk.W)
yscrollbar = Tk.Scrollbar(frame5res)
yscrollbar.grid(row=0, column=1, sticky=Tk.N+Tk.S)
Result5= Tk.Text(frame5res, bd=0,bg="black",fg="white",\
                   xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, width=92, height=10)
Result5.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)
xscrollbar.config(command=listbox5var.xview)
yscrollbar.config(command=listbox5var.yview)
frame5res.place(x=20, y=375)
                       
v0.config(menu=menubarra)
v0.mainloop()