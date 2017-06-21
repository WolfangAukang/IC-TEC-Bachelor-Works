import Tkinter
import tkMessageBox

top=Tkinter.Tk()#Ventana Principal

instruccion= Tkinter.Label(top, text="_Progra_de_calculo_", fg="yellow3", font="SimHei", bg="black")
instruccion.place(x=0, y=0)

texto= Tkinter.Label(top,text="Favor Insertar un numero: ",bg="black",fg="green", relief="raised", font="SimHei",bd=5)
texto.place(x=0, y=75)

instruccion2= Tkinter.Label(top, text="*No debe ser un numeral negativo ni igual a 0", fg="yellow1", font="SimHei", bg="black")
instruccion2.place(x=0, y=125)

entrada= Tkinter.Entry(top, relief="groove", bg="gray8", bd=5, fg="light green", font="SimHei", width=8)
entrada.place(x=219, y=75)
entrada.focus_set()

#Funciones

def salir():
    top.destroy()

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def calculo(n, res=0):
    if n==0:
        res+=1
        return "El resultado es igual a "+str(res)
    else:
        return calculo(n-1, res+(1/factorial(n)))

def introduccion():
    
    n=float(entrada.get())
    if n<=0:
        return tkMessageBox.showinfo("ERROR","Error, datos invalidos")
    else:
        return tkMessageBox.showinfo("Respuesta", calculo(n))



#Botones

boton= Tkinter.Button(top, text="EJECUTAR", command=introduccion, activebackground= "orange", activeforeground="white", bd= 6, width=20, bg="dark orange")
boton.place(x=300, y=75)

boton2= Tkinter.Button(top, text="SALIR", command=salir, activebackground= "orange", activeforeground="white", bd= 6, width=20, bg="dark orange")
boton2.place(x=150, y=150)


top.config(bg="Black")
top.geometry("500x200")
top.mainloop()