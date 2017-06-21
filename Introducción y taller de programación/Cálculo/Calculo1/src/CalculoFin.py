from __future__ import division 
import Tkinter  #IMPORTA LA BIBLIOTECA TKINTER

import tkMessageBox # PARA LAS CAJAS DE MENSAJES


import math 
import random

top = Tkinter.Tk()  #VENTANA PRINCIPAL

titulo=Tkinter.Label(top, text="Bienvenido a la calcula limite de x^2-2 cuando x tiende a 3\n Favor insertar numeros mayores a 0 y epsilon debe ser expresado en 0.X (no es\nvalido interpretarlo como 10**x)", width=60, relief= "groove")
titulo.pack(side="top")

L1=Tkinter.Label(top, text="e", width=3, relief= "groove")
L1.pack(side="left")

texto1 = Tkinter.Entry(top, bd=5, width=5)#, textvariable= elepsilon)
texto1.pack(side="left")
texto1.focus_set()

L2=Tkinter.Label(top, text="n", width=3, relief= "groove")
L2.pack(side="left")


texto2 = Tkinter.Entry(top, bd=5, width=5)#, textvariable= numero)
texto2.pack(side="left")
texto2.focus_set()

###################################################
'''Calcula limite de x^2-2 cuando x tiende a 3 
Entrada: Dos numeros: Un numero epsilon (determina distancia entre f(x) y L) y un n que determina la cantidad de resultados en la lista 
Salida: Una lista indicando el resultado 
Restriccion: Numeros de entrada deben ser mayores a 0, sino se retornara mensaje de error '''

##def calculo1():
##    epsilon= int(texto1.get())
##    n= int(texto2.get())
##    return tkMessageBox.showinfo("G", calculo(epsilon, n))


def calculo(): 
    
    epsilon= float(texto1.get())
    n=int(texto2.get())
    try: 
        
        if n<0 or epsilon<0: 
            return tkMessageBox.showinfo("ERROR", "Error, datos no son validos")
        else: 
            izq=-(epsilon/7)+3
            der=(epsilon/7)+3
            resp= calculoaux(izq,der,n,[],0)
            return tkMessageBox.showinfo("RESPUESTA", resp) 

    except: 
        return tkMessageBox.showinfo("ERROR", "Error, datos no son validos")
          
def calculoaux(valizq,valder,n,res,incres): 
    if n==0: 
        return ("La lista de resultado(s) seria: " +str(res)) 
    else: 
        incres=random.uniform(valizq,valder) 
        if incres not in res and incres!=valizq and incres!=valder: 
            return calculoaux(valizq,valder,n-1,res+[incres],0) 
          

###################################################


Boton = Tkinter.Button(top, text="CALCULAR LIMITE", command= calculo, activebackground= "blue", activeforeground="white", bd= 6, width=20) #EL COMMAND ES PARA LLAMAR UNA FUNCION AL TOCAR EL BOTON
Boton.flash()
Boton.pack(side="right", expand=True)



top.mainloop()

calculo()