from Tkinter import *
from tkMessageBox import *
from random import *

palabras= []

#Funcion Rellena Espacios de Sopa
def llenarespaciosAux(m, c, f): 
    while f!=10: 
        if m[c][f]=="": 
            letra=randint(97,122) 
            m[c][f]=chr(letra) 
        else: 
            pass
        c+=1
        if c==10: 
            c=0
            f+=1
    return m

def llenarespacios(matriz):
    return llenarespaciosAux(matriz, 0, 0)

#Funciones Crea Sopa
def cargaMatriz():
    return [[A0.get(),A1.get(),A2.get(),A3.get(),A4.get(),A5.get(),A6.get(),A7.get(),A8.get(),A9.get()],[B0.get(),B1.get(),B2.get(),B3.get(),B4.get(),B5.get(),B6.get(),B7.get(),B8.get(),B9.get()],[C0.get(),C1.get(),C2.get(),C3.get(),C4.get(),C5.get(),C6.get(),C7.get(),C8.get(),C9.get()],[D0.get(),D1.get(),D2.get(),D3.get(),D4.get(),D5.get(),D6.get(),D7.get(),D8.get(),D9.get()],[E0.get(),E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get(),E9.get()],[F0.get(),F1.get(),F2.get(),F3.get(),F4.get(),F5.get(),F6.get(),F7.get(),F8.get(),F9.get()],[G0.get(),G1.get(),G2.get(),G3.get(),G4.get(),G5.get(),G6.get(),G7.get(),G8.get(),G9.get()],[H0.get(),H1.get(),H2.get(),H3.get(),H4.get(),H5.get(),H6.get(),H7.get(),H8.get(),H9.get()],[I0.get(),I1.get(),I2.get(),I3.get(),I4.get(),I5.get(),I6.get(),I7.get(),I8.get(),I9.get()],[J0.get(),J1.get(),J2.get(),J3.get(),J4.get(),J5.get(),J6.get(),J7.get(),J8.get(),J9.get()]]

def primeraLetraAux(matriz, i1, i2):
    while i1<10:
        while i2<10:
            matriz[i1][i2]= matriz[i1][i2][:1]
            i2= i2+1
        return primeraLetraAux(matriz, i1+1, 0)
    return matriz
                 
def primeraLetra():
    matriz= cargaMatriz()
    return llenarespacios(primeraLetraAux(matriz, 0, 0))

def creasopas():
    nombre= soupname.get()
    matriz= primeraLetra()
    palabras= palabras
    print palabras
    f=open("Sopas Guardadas/Sopas Guardadas.txt","a") 
    f.write("\n"+str(nombre)+"\n") 
    c=0
    fo=0
    stringmatriz="" 
    cont=100
    while cont!=0: 
        stringmatriz+=matriz[fo][c] 
        c+=1
        if c==10: 
            c=0
            fo+=1
        cont-=1
    f.write(stringmatriz+"\n") 
    f.write(str(len(palabras))+"\n") 
    while palabras!=[]: 
        f.write(palabras[0]+"\n") 
        palabras=palabras[1:] 
    f.write("-------------------------------------") 
    f.close()
    return showinfo("Saved", "The file "+str(nombre)+" has been saved.")

def noRepetir():
    f=open("Sopas Guardadas/Sopas Guardadas.txt","r") 
    v=f.readlines()
    y= soupname.get() + "\n"
    if y in v:
        return True
    else:
        return False
    
def preview():
    if soupname.get()=="":
        return showinfo("Inválido","Debe ingresar un nombre para la sopa.")
    elif noRepetir()== True:
        return showinfo("Inválido","El nombre ingresado esta repetido.")
        
    else:
        x= armaMatriz()
        opcion= askokcancel("Estas seguro?", "Desea proceder a guardar la sopa? \n"+str(x))
        if opcion == True:
            return creasopas()
        else:
            pass

def creasopas2():
    nombre= soupname.get()
    matriz= primeraLetra()
    palabras= palabras
    c=0
    fo=0
    stringmatriz="" 
    cont=100
    while cont!=0: 
        stringmatriz+=matriz[fo][c] 
        c+=1
        if c==10: 
            c=0
            fo+=1
        cont-=1
    return stringmatriz

def armaMatrizAux(matriz, cont, cont2, index, dibujo):
    while cont2 < 10:
        while cont < 10:
            dibujo= dibujo + matriz[index] + str("      ")
            index= index+1
            cont= cont+1
        cont2= cont2+1
        cont= 0
        dibujo= dibujo + "\n"
    return dibujo

def armaMatriz():
    x= creasopas2()
    return armaMatrizAux(x, 0, 0, 0, "\n")

#Funcion Add Word
def addwordfunction():
    global palabras
    palabra=Addword.get()
    if palabra != "":
        if len(palabra)<11:
            if palabra not in palabras:
                words.insert(END, palabra)
                palabras.append(palabra)
            else:
                return showerror("Error", "La palabra insertada ya está insertada")
        else:
            return showerror("Error", "La palabra insertada es mayor a 10 letras")
    else:
        return showerror("Error", "La palabra insertada no es válida")

def deletewordfunction():
    global palabras
    palabra=Addword.get()
    if palabra in palabras:
        pos=palabras.index(palabra)
        palabras.remove(palabra)
        words.delete(pos)
    else:
        showerror("Error","Dicha palabra no se encuentra en la lista")
        
#Interfaz-------------------------------------------------------------------------------------------------------------------------------
creadorsopas = Tk() #Ventana Principal
creadorsopas.geometry("1000x650")
creadorsopas.config(bg="black")
creadorsopas.title("Letter Soup Creator ")


filename = PhotoImage(file = "Imagenes/logo.gif")
label = Label( creadorsopas, relief="flat", image=filename, width= 300, height=200, bg="black" )
label.place(x="30", y="0")

#Create your own

COwn= Label(creadorsopas, relief="groove", text="Create your Own ...", font=("COMIC SANS MS", 20), bg="black", fg="#FF9E15", bd=0)
COwn.place(x="540", y="20")

#Soup Name
soupname= StringVar()
SName= Label(creadorsopas, text="Soup Name: ", fg="#FF9E15", font=("COMIC SANS MS", 15), bg="black")
SName.place(x="60", y="200")
Name= Entry(creadorsopas, width=40, textvar= soupname, bg="black", fg="#EB9334")
Name.place(x="60", y="250")

#Frame
frameL= Frame(creadorsopas, bg="black")
frameL.place(x="60", y="330")

#Scrollbar
Scroll= Scrollbar(frameL, bg="#EEE061")
Scroll.pack(side="right", fill="y")


#ListBox
words= Listbox(frameL, height=5, width=33, yscrollcommand = Scroll.set, bg="black", fg="#FF9E15")
words.pack()
#Config. Scroll
Scroll.config(command=words.yview)

#AddWords
Awords= Label(creadorsopas, text="Words: ", font=("COMIC SANS MS", 15), bg="black", fg="#FF9E15")
Awords.place(x="60", y="290")

#Add word Entry
Addword= StringVar()
Add= Entry(creadorsopas, width=20, textvar=Addword, bg="black", fg="#EB9334")
Add.place(x="60", y="430")
AddButton= Button(creadorsopas, text="Add word", command= addwordfunction, bg="#4B43D9", fg="white")
AddButton.place(x="200", y="425")
DeleteButton= Button(creadorsopas, text="Delete", command= deletewordfunction, bg="#E15454", fg="white")
DeleteButton.place(x="270", y="425")

#Boton guardado
CrearSopa= Button(creadorsopas, text="Save your soup", width=17, font=("COMIC SANS MS", 18), fg="black", bg="#FF9E15", bd=3, relief="raised", command= preview)
CrearSopa.place(x="50", y="500")

#String Vars#####
A0=StringVar()
A1=StringVar()
A2=StringVar()
A3=StringVar()
A4=StringVar()
A5=StringVar()
A6=StringVar()
A7=StringVar()
A8=StringVar()
A9=StringVar()

B0=StringVar()
B1=StringVar()
B2=StringVar()
B3=StringVar()
B4=StringVar()
B5=StringVar()
B6=StringVar()
B7=StringVar()
B8=StringVar()
B9=StringVar()

C0=StringVar()
C1=StringVar()
C2=StringVar()
C3=StringVar()
C4=StringVar()
C5=StringVar()
C6=StringVar()
C7=StringVar()
C8=StringVar()
C9=StringVar()

D0=StringVar()
D1=StringVar()
D2=StringVar()
D3=StringVar()
D4=StringVar()
D5=StringVar()
D6=StringVar()
D7=StringVar()
D8=StringVar()
D9=StringVar()

E0=StringVar()
E1=StringVar()
E2=StringVar()
E3=StringVar()
E4=StringVar()
E5=StringVar()
E6=StringVar()
E7=StringVar()
E8=StringVar()
E9=StringVar()

F0=StringVar()
F1=StringVar()
F2=StringVar()
F3=StringVar()
F4=StringVar()
F5=StringVar()
F6=StringVar()
F7=StringVar()
F8=StringVar()
F9=StringVar()

G0=StringVar()
G1=StringVar()
G2=StringVar()
G3=StringVar()
G4=StringVar()
G5=StringVar()
G6=StringVar()
G7=StringVar()
G8=StringVar()
G9=StringVar()

H0=StringVar()
H1=StringVar()
H2=StringVar()
H3=StringVar()
H4=StringVar()
H5=StringVar()
H6=StringVar()
H7=StringVar()
H8=StringVar()
H9=StringVar()

I0=StringVar()
I1=StringVar()
I2=StringVar()
I3=StringVar()
I4=StringVar()
I5=StringVar()
I6=StringVar()
I7=StringVar()
I8=StringVar()
I9=StringVar()

J0=StringVar()
J1=StringVar()
J2=StringVar()
J3=StringVar()
J4=StringVar()
J5=StringVar()
J6=StringVar()
J7=StringVar()
J8=StringVar()
J9=StringVar()

#################
#Primera Fila
eA0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A0)
eA0.place(x="450", y="100")
eA1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A1)
eA1.place(x="500", y="100")
eA2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A2)
eA2.place(x="550", y="100")
eA3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A3)
eA3.place(x="600", y="100")
eA4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A4)
eA4.place(x="650", y="100")
eA5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A5)
eA5.place(x="700", y="100")
eA6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A6)
eA6.place(x="750", y="100")
eA7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A7)
eA7.place(x="800", y="100")
eA8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A8)
eA8.place(x="850", y="100")
eA9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=A9)
eA9.place(x="900", y="100")
#Segunda Fila
eB0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B0)
eB0.place(x="450", y="145")
eB1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B1)
eB1.place(x="500", y="145")
eB2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B2)
eB2.place(x="550", y="145")
eB3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B3)
eB3.place(x="600", y="145")
eB4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B4)
eB4.place(x="650", y="145")
eB5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B5)
eB5.place(x="700", y="145")
eB6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B6)
eB6.place(x="750", y="145")
eB7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B7)
eB7.place(x="800", y="145")
eB8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B8)
eB8.place(x="850", y="145")
eB9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=B9)
eB9.place(x="900", y="145")
#Tercera Fila
eC0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C0)
eC0.place(x="450", y="190")
eC1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C1)
eC1.place(x="500", y="190")
eC2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C2)
eC2.place(x="550", y="190")
eC3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C3)
eC3.place(x="600", y="190")
eC4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C4)
eC4.place(x="650", y="190")
eC5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C5)
eC5.place(x="700", y="190")
eC6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C6)
eC6.place(x="750", y="190")
eC7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C7)
eC7.place(x="800", y="190")
eC8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C8)
eC8.place(x="850", y="190")
eC9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=C9)
eC9.place(x="900", y="190")
#Cuarta Fila
eD0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D0)
eD0.place(x="450", y="235")
eD1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D1)
eD1.place(x="500", y="235")
eD2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D2)
eD2.place(x="550", y="235")
eD3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D3)
eD3.place(x="600", y="235")
eD4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D4)
eD4.place(x="650", y="235")
eD5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D5)
eD5.place(x="700", y="235")
eD6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D6)
eD6.place(x="750", y="235")
eD7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D7)
eD7.place(x="800", y="235")
eD8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D8)
eD8.place(x="850", y="235")
eD9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=D9)
eD9.place(x="900", y="235")
#Quinta Fila
eE0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E0)
eE0.place(x="450", y="280")
eE1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E1)
eE1.place(x="500", y="280")
eE2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E2)
eE2.place(x="550", y="280")
eE3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E3)
eE3.place(x="600", y="280")
eE4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E4)
eE4.place(x="650", y="280")
eE5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E5)
eE5.place(x="700", y="280")
eE6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E6)
eE6.place(x="750", y="280")
eE7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E7)
eE7.place(x="800", y="280")
eE8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E8)
eE8.place(x="850", y="280")
eE9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=E9)
eE9.place(x="900", y="280")
#Sexta Fila
eF0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F0)
eF0.place(x="450", y="325")
eF1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F1)
eF1.place(x="500", y="325")
eF2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F2)
eF2.place(x="550", y="325")
eF3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F3)
eF3.place(x="600", y="325")
eF4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F4)
eF4.place(x="650", y="325")
eF5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F5)
eF5.place(x="700", y="325")
eF6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F6)
eF6.place(x="750", y="325")
eF7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F7)
eF7.place(x="800", y="325")
eF8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F8)
eF8.place(x="850", y="325")
eF9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=F9)
eF9.place(x="900", y="325")
#Septima Fila
eG0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G0)
eG0.place(x="450", y="370")
eG1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G1)
eG1.place(x="500", y="370")
eG2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G2)
eG2.place(x="550", y="370")
eG3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G3)
eG3.place(x="600", y="370")
eG4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G4)
eG4.place(x="650", y="370")
eG5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G5)
eG5.place(x="700", y="370")
eG6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G6)
eG6.place(x="750", y="370")
eG7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G7)
eG7.place(x="800", y="370")
eG8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G8)
eG8.place(x="850", y="370")
eG9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=G9)
eG9.place(x="900", y="370")
#Octava Fila
eH0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H0)
eH0.place(x="450", y="415")
eH1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H1)
eH1.place(x="500", y="415")
eH2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H2)
eH2.place(x="550", y="415")
eH3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H3)
eH3.place(x="600", y="415")
eH4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H4)
eH4.place(x="650", y="415")
eH5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H5)
eH5.place(x="700", y="415")
eH6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H6)
eH6.place(x="750", y="415")
eH7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H7)
eH7.place(x="800", y="415")
eH8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H8)
eH8.place(x="850", y="415")
eH9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=H9)
eH9.place(x="900", y="415")
#Novena Fila
eI0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I0)
eI0.place(x="450", y="460")
eI1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I1)
eI1.place(x="500", y="460")
eI2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I2)
eI2.place(x="550", y="460")
eI3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I3)
eI3.place(x="600", y="460")
eI4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I4)
eI4.place(x="650", y="460")
eI5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I5)
eI5.place(x="700", y="460")
eI6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I6)
eI6.place(x="750", y="460")
eI7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I7)
eI7.place(x="800", y="460")
eI8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I8)
eI8.place(x="850", y="460")
eI9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=I9)
eI9.place(x="900", y="460")
#Decima Fila
eJ0 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J0)
eJ0.place(x="450", y="505")
eJ1 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J1)
eJ1.place(x="500", y="505")
eJ2 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J2)
eJ2.place(x="550", y="505")
eJ3 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J3)
eJ3.place(x="600", y="505")
eJ4 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J4)
eJ4.place(x="650", y="505")
eJ5 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J5)
eJ5.place(x="700", y="505")
eJ6 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J6)
eJ6.place(x="750", y="505")
eJ7 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J7)
eJ7.place(x="800", y="505")
eJ8 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J8)
eJ8.place(x="850", y="505")
eJ9 = Entry(creadorsopas, relief="flat", bg="#151515", bd=0, font=("COMIC SANS MS", 20), fg="#EEE061", width=1, justify="center", textvar=J9)
eJ9.place(x="900", y="505")

creadorsopas.mainloop()
