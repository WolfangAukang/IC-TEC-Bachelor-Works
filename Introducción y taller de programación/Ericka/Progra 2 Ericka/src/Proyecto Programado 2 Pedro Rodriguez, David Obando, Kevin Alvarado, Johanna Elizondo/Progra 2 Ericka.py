# -*- coding: utf-8 -*-
#Bibliotecas a importar
from Tkinter import *
from tkMessageBox import *
from random import * 
#-------------------------------------------------------------------------------------------------------
#Instituto Tecológico de Costa Rica
#Carrera de Ingeniería en Computación
#Curso de Taller de Programación
#Profesora: Ericka Solano Fernández
#Segundo Proyecto Programado: Sopa de letras
#Estudiantes: Kevin Alvarado Lamas
#Johanna Elizondo Aguero
#David Obando Paniagua
#Pedro Rodríguez de Oliveira
#II semestre
#2013
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
#Variables globales
#-------------------------------------------------------------------------------------------------------
#Para jugar sopa
#Memoriza la sopa de letras
matriz=[["","","","","","","","","",""],\
        ["","","","","","","","","",""],\
        ["","","","","","","","","",""],\
        ["","","","","","","","","",""],\
        ["","","","","","","","","",""],\
        ["","","","","","","","","",""],\
        ["","","","","","","","","",""],\
        ["","","","","","","","","",""],\
        ["","","","","","","","","",""],\
        ["","","","","","","","","",""]]
#Guarda las palabras
palabras=[]
#Guarda los nombres de las sopas guardadas
sopasguardadastxt=[]
#Para comenzar busqueda en sopa
#Variable que indica si se puede cargar la sopa
puedecargar=False
#Variable que activa modo búsqueda
modobusqueda=False
#Variable para confirmar palabra obtenida
avanzar=True
#Variables que conta las letras de la palabra a buscar 
conteo=0
limiteconteo=0
#Variable para evitar error de trazos
modus=""
#Lista que muestra los botones hecho clic
botonesclicados=[]
#Variable que contiene letras clicadas
palabrahecha=[]
#Variable que analiza posiciones
posicionesbot=[]
#Variable que muestra la palabra que se encuentra buscando actualmente
palabraabuscar=""
#Variables con colores
color="gold"
cambio="red"
letra="white"
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
#Funciones
#-------------------------------------------------------------------------------------------------------
#Interfaz
#Retorna cuadro de confirmacion para cerrar programa
def salir():
    salir=askokcancel("Desea salir?", "Desea salir del programa?\n(Sigue el consejo de Boromir: Uno\nsimplemente no deja de jugar\nsopas de letras)")
    if salir:
        v0.destroy()
        
#Cierra el programa
def salirtotal():
    v0.destroy()

#Carga la ventana que carga la sopa de letras
def ventanacarga():
    v0.withdraw()
    crearlistasopas()
    cargadora.deiconify()

#Carga la ventana creadora de sopas
def ventanacrea():
    global palabras
    v0.withdraw()
    creadorsopas.deiconify()
    palabras=[]

#Cierra la ventana creadora de sopas
def salircrea():
    confirmar=askokcancel("Desea salir?", "Desea salir del programa?")
    if confirmar:
        v0.destroy()

#Retorna al menú principal desde la ventana de crear sopas
def regresarcrea():
    confirmar=askokcancel("Desea salir?", "Desea salir del creador de sopas?")
    if confirmar:
        regresar()

#Retorna al menu principal
def regresar():
    v0.deiconify()
    felicitaciones.update()
    felicitaciones.withdraw()
    juego.update()
    juego.withdraw()
    cargadora.update()
    cargadora.withdraw()
    creadorsopas.update()
    creadorsopas.withdraw()

#Retorna al menu principal desde el juego
def regresardesdejuego():
    confirmar=askokcancel("Desea salir?", "Desea salir del juego?\nTodo el progreso no será guardado")
    if confirmar:
        v0.deiconify()
        felicitaciones.update()
        felicitaciones.withdraw()
        cargadora.update()
        cargadora.withdraw()
        juego.update()
        juego.withdraw()
        creadorsopas.update()
        creadorsopas.withdraw()

#Algoritmos de carga de sopa
def crearlistasopas():
    global sopasguardadastxt
    global listboxcarga
    listboxcarga.delete(0,END)
    sopasguardadastxt=[]
    f=open("Sopas Guardadas/Sopas Guardadas.txt","r")
    texto=f.readlines()
    for i in texto:
        if i[0]=="*":
            liste=i[1:-1]
            sopasguardadastxt+=[liste]
    for i in sopasguardadastxt:
        listboxcarga.insert(END,i)

#Actualiza los texts de los botones al cargar una nueva sopa
def letraslabels():
    global b0
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global b10
    global b11
    global b12
    global b13
    global b14
    global b15
    global b16
    global b17
    global b18
    global b19
    global b20
    global b21
    global b22
    global b23
    global b24
    global b25
    global b26
    global b27
    global b28
    global b29
    global b30
    global b31
    global b32
    global b33
    global b34
    global b35
    global b36
    global b37
    global b38
    global b39
    global b40
    global b41
    global b42
    global b43
    global b44
    global b45
    global b46
    global b47
    global b48
    global b49
    global b50
    global b51
    global b52
    global b53
    global b54
    global b55
    global b56
    global b57
    global b58
    global b59
    global b60
    global b61
    global b62
    global b63
    global b64
    global b65
    global b66
    global b67
    global b68
    global b69
    global b70
    global b71
    global b72
    global b73
    global b74
    global b75
    global b76
    global b77
    global b78
    global b79
    global b80
    global b81
    global b82
    global b83
    global b84
    global b85
    global b86
    global b87
    global b88
    global b89
    global b90
    global b91
    global b92
    global b93
    global b94
    global b95
    global b96
    global b97
    global b98
    global b99
    b0.configure(text=matriz[0][0])
    b1.configure(text=matriz[0][1])
    b2.configure(text=matriz[0][2])
    b3.configure(text=matriz[0][3])
    b4.configure(text=matriz[0][4])
    b5.configure(text=matriz[0][5])
    b6.configure(text=matriz[0][6])
    b7.configure(text=matriz[0][7])
    b8.configure(text=matriz[0][8])
    b9.configure(text=matriz[0][9])
    b10.configure(text=matriz[1][0])
    b11.configure(text=matriz[1][1])
    b12.configure(text=matriz[1][2])
    b13.configure(text=matriz[1][3])
    b14.configure(text=matriz[1][4])
    b15.configure(text=matriz[1][5])
    b16.configure(text=matriz[1][6])
    b17.configure(text=matriz[1][7])
    b18.configure(text=matriz[1][8])
    b19.configure(text=matriz[1][9])
    b20.configure(text=matriz[2][0])
    b21.configure(text=matriz[2][1])
    b22.configure(text=matriz[2][2])
    b23.configure(text=matriz[2][3])
    b24.configure(text=matriz[2][4])
    b25.configure(text=matriz[2][5])
    b26.configure(text=matriz[2][6])
    b27.configure(text=matriz[2][7])
    b28.configure(text=matriz[2][8])
    b29.configure(text=matriz[2][9])
    b30.configure(text=matriz[3][0])
    b31.configure(text=matriz[3][1])
    b32.configure(text=matriz[3][2])
    b33.configure(text=matriz[3][3])
    b34.configure(text=matriz[3][4])
    b35.configure(text=matriz[3][5])
    b36.configure(text=matriz[3][6])
    b37.configure(text=matriz[3][7])
    b38.configure(text=matriz[3][8])
    b39.configure(text=matriz[3][9])
    b40.configure(text=matriz[4][0])
    b41.configure(text=matriz[4][1])
    b42.configure(text=matriz[4][2])
    b43.configure(text=matriz[4][3])
    b44.configure(text=matriz[4][4])
    b45.configure(text=matriz[4][5])
    b46.configure(text=matriz[4][6])
    b47.configure(text=matriz[4][7])
    b48.configure(text=matriz[4][8])
    b49.configure(text=matriz[4][9])
    b50.configure(text=matriz[5][0])
    b51.configure(text=matriz[5][1])
    b52.configure(text=matriz[5][2])
    b53.configure(text=matriz[5][3])
    b54.configure(text=matriz[5][4])
    b55.configure(text=matriz[5][5])
    b56.configure(text=matriz[5][6])
    b57.configure(text=matriz[5][7])
    b58.configure(text=matriz[5][8])
    b59.configure(text=matriz[5][9])
    b60.configure(text=matriz[6][0])
    b61.configure(text=matriz[6][1])
    b62.configure(text=matriz[6][2])
    b63.configure(text=matriz[6][3])
    b64.configure(text=matriz[6][4])
    b65.configure(text=matriz[6][5])
    b66.configure(text=matriz[6][6])
    b67.configure(text=matriz[6][7])
    b68.configure(text=matriz[6][8])
    b69.configure(text=matriz[6][9])
    b70.configure(text=matriz[7][0])
    b71.configure(text=matriz[7][1])
    b72.configure(text=matriz[7][2])
    b73.configure(text=matriz[7][3])
    b74.configure(text=matriz[7][4])
    b75.configure(text=matriz[7][5])
    b76.configure(text=matriz[7][6])
    b77.configure(text=matriz[7][7])
    b78.configure(text=matriz[7][8])
    b79.configure(text=matriz[7][9])
    b80.configure(text=matriz[8][0])
    b81.configure(text=matriz[8][1])
    b82.configure(text=matriz[8][2])
    b83.configure(text=matriz[8][3])
    b84.configure(text=matriz[8][4])
    b85.configure(text=matriz[8][5])
    b86.configure(text=matriz[8][6])
    b87.configure(text=matriz[8][7])
    b88.configure(text=matriz[8][8])
    b89.configure(text=matriz[8][9])
    b90.configure(text=matriz[9][0])
    b91.configure(text=matriz[9][1])
    b92.configure(text=matriz[9][2])
    b93.configure(text=matriz[9][3])
    b94.configure(text=matriz[9][4])
    b95.configure(text=matriz[9][5])
    b96.configure(text=matriz[9][6])
    b97.configure(text=matriz[9][7])
    b98.configure(text=matriz[9][8])
    b99.configure(text=matriz[9][9])
        
#Busca sopa y palabras dentro de archivo txt
def buscarsopa():
    global matriz
    global palabras
    global puedecargar
    nombresopa=Entrcargadora.get()
    nombresopa="*"+str(nombresopa)+"\n"
    f=open("Sopas Guardadas/Sopas Guardadas.txt","r")
    texto=f.readlines()
    if nombresopa not in texto:
        showerror("Error","Error, no existe tal sopa")
    else:
        pos=texto.index(nombresopa)
        matrizacrear=list(texto[pos+1])
        can=0
        lineamatriz=[]
        matriz=[]
        for i in range(0,100):
            lineamatriz+=matrizacrear[i]
            can+=1
            if can%10==0 and can!=0:
                matriz+=[lineamatriz]
                lineamatriz=[]
        cantidadpalabras=int(texto[pos+2])
        i=0
        linea=3
        palabras=[]
        while i!=cantidadpalabras:
            agregar=str(texto[pos+linea])
            palabras+=[agregar[:-1]]
            i+=1
            linea+=1
            agregar=""
        puedecargar=True

#Agrega las palabras a la listbox
def agregarpalabraslistbox():
    listbox.delete(0,END)
    for i in palabras:
        listbox.insert(END,i)

#Contiene los procesos que cargan a la sopa y la adaptan al programa
def cargarsopa():
    global puedecargar
    puedecargar=False
    buscarsopa()
    if puedecargar:
        agregarpalabraslistbox()
        letraslabels()
        cargadora.withdraw()
        juego.update()
        juego.deiconify()

#Algoritmos para jugar sopa
#Activa el modo busqueda
def modobusquedafun():
    global avanzar
    global modobusqueda
    global limiteconteo
    global conteo
    global palabras
    global palabraabuscar
    global Botonindicador
    avanzar=True
    palabraabuscar=Entr.get()
    if palabraabuscar in palabras:
        modobusqueda=True
        limiteconteo=len(palabraabuscar)
        Botonindicador.configure(text="Modo búsqueda\nactivado",bg="green")
    else:
        showerror("Error","Error, palabra no disponible para busqueda")

#Confirma si el movimiento hecho por el usuario es valido si el modo busqueda este activado
def posiciones(x,y,boton):
    global avanzar
    global modus
    global modobusqueda
    global matriz
    global conteo
    global limiteconteo
    global botonesclicados
    global palabrahecha
    global posicionesbot
    global Botonindicador
    if modobusqueda:
        boton.configure(bg=cambio)
        conteo+=1
        botonesclicados+=[boton]
        palabrahecha+=[matriz[x][y]]
        if [x,y] not in posicionesbot:
            posicionesbot+=[[x,y]]
            if conteo>=2:
                paradigma1=posicionesbot[-1][0]-posicionesbot[-2][0]
                paradigma2=posicionesbot[-1][1]-posicionesbot[-2][1]
                if (posicionesbot[-1][0])-(posicionesbot[-2][0]) not in [-1,0,1] or (posicionesbot[-1][1])-(posicionesbot[-2][1]) not in [-1,0,1]:
                    error()
                elif modus=="" and conteo==2:
                    if paradigma1==-1 and paradigma2==-1:
                        modus="diar"
                    elif paradigma1==-1 and paradigma2==0:
                        modus="ar"
                    elif paradigma1==-1 and paradigma2==1:
                        modus="ddar"
                    elif paradigma1==0 and paradigma2==-1:
                        modus="i"
                    elif paradigma1==0 and paradigma2==1:
                        modus="d"
                    elif paradigma1==1 and paradigma2==-1:
                        modus="diab"
                    elif paradigma1==1 and paradigma2==0:
                        modus="ab"
                    else:
                        modus="ddab"
                if modus!="" and limiteconteo>=conteo:
                    if modus=="diar":
                        if paradigma1==-1 and paradigma2==-1:
                            pass
                        else:
                            error()
                            avanzar=False
                    elif modus=="ar":
                        if paradigma1==-1 and paradigma2==0:
                            pass
                        else:
                            error()
                            avanzar=False
                    elif modus=="ddar":
                        if paradigma1==-1 and paradigma2==1:
                            pass
                        else:
                            error()
                            avanzar=False
                    elif modus=="i":
                        if paradigma1==0 and paradigma2==-1:
                            pass
                        else:
                            error()
                            avanzar=False
                    elif modus=="d":
                        if paradigma1==0 and paradigma2==1:
                            pass
                        else:
                            error()
                            avanzar=False
                    elif modus=="diab":
                        if paradigma1==1 and paradigma2==-1:
                            pass
                        else:
                            error()
                            avanzar=False
                    elif modus=="ab":
                        if paradigma1==1 and paradigma2==0:
                            pass
                        else:
                            error()
                            avanzar=False
                    else:
                        if paradigma1==1 and paradigma2==1:
                            pass
                        else:
                            error()
                            avanzar=False
                if conteo==limiteconteo and avanzar==True:
                    confirmarpalabra()
                else:
                    pass
        else:
            error()
            
#Borra el contenido de las variables en caso de movimiento erroneo o palabra equivocada. Desactiva modo busqueda
def error():
    global modobusqueda
    global matriz
    global modus
    global conteo
    global limiteconteo
    global botonesclicados
    global palabrahecha
    global posicionesbot
    global Botonindicador
    showerror ("Error","Movimiento no es válido. Tendrás que repetir el proceso")
    modobusqueda=False
    conteo=0
    limiteconteo=0
    for i in botonesclicados:
        i.configure(bg=color)
    botonesclicados=[]
    palabrahecha=[]
    posicionesbot=[]
    modus=""
    Botonindicador.configure(text="Modo búsqueda\ndesactivado",bg="red")
                    
#Revisa la palabra al igualarse el conteo con la cantidad de letras de la palabra y revisa que sea la palabra a buscar
def confirmarpalabra():
    global modus
    global palabrahecha
    global palabraabuscar
    global palabras
    global modobusqueda
    global matriz
    global conteo
    global limiteconteo
    global botonesclicados
    global posicionesbot
    global Botonindicador
    palabraformada="".join(palabrahecha)
    if palabraformada!=palabraabuscar:
        showerror("Error","La palabra no es la correcta")
    else:
        showinfo("Felicidades", "Muy bien, has encontrado la palabra "+str(palabraabuscar))
        pos=palabras.index(palabraabuscar)
        listbox.delete(pos)
        palabras.remove(palabraabuscar)
    modobusqueda=False
    conteo=0
    limiteconteo=0
    for i in botonesclicados:
        i.configure(bg=color)
    botonesclicados=[]
    palabrahecha=[]
    posicionesbot=[]
    modus=""
    Botonindicador.configure(text="Modo búsqueda\ndesactivado",bg="red")
    if palabras==[]:
        juego.withdraw()
        felicitaciones.deiconify()
    
#Algoritmos crear sopas
#Funcion que Rellena Espacios de Sopa
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

#Llena espacios de la matriz
def llenarespacios(matriz):
    return llenarespaciosAux(matriz, 0, 0)

#Agarra contenido de entries
def cargaMatriz():
    return [[A0.get(),A1.get(),A2.get(),A3.get(),A4.get(),A5.get(),A6.get(),A7.get(),A8.get(),A9.get()],[B0.get(),B1.get(),B2.get(),B3.get(),B4.get(),B5.get(),B6.get(),B7.get(),B8.get(),B9.get()],[C0.get(),C1.get(),C2.get(),C3.get(),C4.get(),C5.get(),C6.get(),C7.get(),C8.get(),C9.get()],[D0.get(),D1.get(),D2.get(),D3.get(),D4.get(),D5.get(),D6.get(),D7.get(),D8.get(),D9.get()],[E0.get(),E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get(),E9.get()],[F0.get(),F1.get(),F2.get(),F3.get(),F4.get(),F5.get(),F6.get(),F7.get(),F8.get(),F9.get()],[G0.get(),G1.get(),G2.get(),G3.get(),G4.get(),G5.get(),G6.get(),G7.get(),G8.get(),G9.get()],[H0.get(),H1.get(),H2.get(),H3.get(),H4.get(),H5.get(),H6.get(),H7.get(),H8.get(),H9.get()],[I0.get(),I1.get(),I2.get(),I3.get(),I4.get(),I5.get(),I6.get(),I7.get(),I8.get(),I9.get()],[J0.get(),J1.get(),J2.get(),J3.get(),J4.get(),J5.get(),J6.get(),J7.get(),J8.get(),J9.get()]]

#Agarra la primera letra del entry en caso dicho entry tenga mas de dos caracteres
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

#Guarda la sopa en el txt
def creasopas():
    global palabras
    nombre= soupname.get()
    matriz= primeraLetra()
    palabras= palabras
    f=open("Sopas Guardadas/Sopas Guardadas.txt","a") 
    f.write("\n*"+str(nombre)+"\n") 
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
    return showinfo("Guardado", "El archivo "+str(nombre)+" ha sido guardado exitosamente.")

#Verifica que el nombre de la sopa no se encuentre ya guardado
def noRepetir():
    f=open("Sopas Guardadas/Sopas Guardadas.txt","r") 
    v=f.readlines()
    y="*" + soupname.get() + "\n"
    if y in v:
        return True
    else:
        return False

#Lanza previsualizacion de la sopa a crear
def preview():
    global palabras
    if soupname.get()=="":
        return showerror("Inválido","Debe ingresar un nombre para la sopa.")
    elif noRepetir()== True:
        return showerror("Inválido","El nombre ingresado ya existe.")
    elif palabras==[]:
        return showerror("Inválido","La lista de palabras está vacía")
    else:
        x= armaMatriz()
        opcion= askokcancel("Estas seguro?", "Desea proceder a guardar la sopa? \n"+str(x))
        if opcion == True:
            return creasopas()
        else:
            pass

#Convierte la matriz en un string para guardar sopa
def creasopas2():
    global palabras
    nombre= soupname.get()
    matriz= primeraLetra()
    palabras=palabras
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

#Forma la matriz
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

#Funcion que agrega palabras a la listbox y la lista de palabras de la sopa
def addwordfunction():
    global palabras
    palabra=Addword.get()
    if palabra != "":
        if len(palabra)<11:
            if palabra not in palabras:
                words.insert(END, palabra)
                palabras.append(palabra)
            else:
                return showerror("Error", "Esta palabra ya está insertada")
        else:
            return showerror("Error", "La palabra insertada es mayor a 10 letras")
    else:
        return showerror("Error", "La palabra insertada no es válida")
    print palabras

#Elimina palabra de la listbox y lista de palabras de la sopa
def deletewordfunction():
    global palabras
    palabra=Addword.get()
    if palabra in palabras:
        pos=palabras.index(palabra)
        palabras.remove(palabra)
        words.delete(pos)
    else:
        showerror("Error","Dicha palabra no se encuentra en la lista")
    print palabras
        
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
#Interfaz
#-------------------------------------------------------------------------------------------------------    
#Configuracion de la ventana principal
v0=Tk()
v0.config(bg="Black")
v0.geometry("466x380")
v0.resizable(0,0)
v0.title("Sopa de letras")

#Ventana principal
titulo=Label(v0, text="Sopa De Letras", fg="yellow3", font=("SimHei",26), bg="black")
titulo.place(x=110,y=3)
imagenprin=PhotoImage(file="Imagenes/pchlp.gif")
imagen=Label(v0, image=imagenprin)
imagen.place(x=0,y=45)
menutitulo=Label(v0, text="Menú", fg="#00FF40", font=("SimHei",26), bg="black")
menutitulo.place(x=80,y=180)
sopacrear=Button(v0,text="Crear una nueva sopa", activebackground="orange", bd=6, width=25, bg="dark orange",command=ventanacrea)
sopacrear.place(x=245,y=115)
sopajugar=Button(v0,text="Jugar una sopa creada", activebackground="orange", bd=6, width=25, bg="dark orange", command=ventanacarga)
sopajugar.place(x=245,y=175)
sopasalir=Button(v0,text="Salir del juego", command=salir, activebackground="orange", bd=6, width=25, bg="dark orange")
sopasalir.place(x=245,y=235)

#Ventana que crea sopa de letras
creadorsopas = Toplevel()
creadorsopas.resizable(0,0)
creadorsopas.attributes("-fullscreen", 1)
creadorsopas.withdraw()
creadorsopas.geometry("1000x650")
creadorsopas.config(bg="black")
creadorsopas.title("Letter Soup Creator ")
filename = PhotoImage(file = "Imagenes/logo.gif")
label = Label( creadorsopas, relief="flat", image=filename, width= 300, height=200, bg="black" )
label.place(x="30", y="0")

#Create your own
COwn= Label(creadorsopas, relief="groove", text="Crea tu propia sopa!!", font=("COMIC SANS MS", 20), bg="black", fg="#FF9E15", bd=0)
COwn.place(x="540", y="20")

#Soup Name
soupname= StringVar()
SName= Label(creadorsopas, text="Nombre de la sopa: ", fg="#FF9E15", font=("COMIC SANS MS", 15), bg="black")
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
Awords= Label(creadorsopas, text="Palabras insertadas: ", font=("COMIC SANS MS", 15), bg="black", fg="#FF9E15")
Awords.place(x="60", y="290")

#Add word Entry
Addword= StringVar()
Add= Entry(creadorsopas, width=20, textvar=Addword, bg="black", fg="#EB9334")
Add.place(x="60", y="430")
AddButton= Button(creadorsopas, text="Agregar", command= addwordfunction, bg="#4B43D9", fg="white")
AddButton.place(x="200", y="425")
DeleteButton= Button(creadorsopas, text="Borrar", command= deletewordfunction, bg="#E15454", fg="white")
DeleteButton.place(x="270", y="425")

#Labels
imagencrea=PhotoImage(file="Imagenes/6593900.gif")
imagencreav=Label(creadorsopas, image=imagencrea)
imagencreav.place(x=960,y=0)
imagencrea2=PhotoImage(file="Imagenes/6593947.gif")
imagencreav2=Label(creadorsopas, image=imagencrea2)
imagencreav2.place(x=960,y=410)

#Botones
CrearSopa= Button(creadorsopas, text="Guardar la sopa", width=17, font=("COMIC SANS MS", 18), fg="black", bg="#FF9E15", bd=3, relief="raised", command= preview)
CrearSopa.place(x="50", y="500")
botonsalircrea=Button(creadorsopas,text="Salir del programa", activebackground="orange",font=("COMIC SANS MS", 11,"bold"), bd=6, width=40,height=3, bg="dark orange",command=salircrea)
botonsalircrea.place(x=503,y=570)
botonregresomenucrea=Button(creadorsopas,text="Regresar al menú principal", activebackground="orange",font=("COMIC SANS MS", 11,"bold"), bd=6, width=40,height=3, bg="dark orange",command=regresarcrea)
botonregresomenucrea.place(x=503,y=670)

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

#Ventana que carga sopa de letras
cargadora=Toplevel(bg="black")
cargadora.withdraw()
cargadora.geometry("500x409")
cargadora.title("Cargar Sopa")
textocargar=Label(cargadora, text="Favor insertar nombre de la sopa guardada", fg="#00FF40", font=("SimHei",14), bg="black")
textocargar.place(x=2, y=10)
textoindic=Label(cargadora, text="Si no sabes cual sopa escoger, tenemos la sopa Ejemplo,\npara que se entretenga por un momento", fg="dark orange", font=("SimHei",11), bg="black")
textoindic.place(x=8, y=60)
textoindic=Label(cargadora, text="Sopas guardadas:", fg="green", font=("SimHei",11), bg="black")
textoindic.place(x=8, y=95)
Entrcargadora=StringVar()
Entrycargadora=Entry(cargadora,textvariable=Entrcargadora,width=100)
Entrycargadora.place(x=8,y=40)
framelistboxcarga=Frame(cargadora, bd=2, relief=SUNKEN, width=120, height=70)
yscrollbar = Scrollbar(framelistboxcarga)
yscrollbar.grid(row=0, column=1, sticky=N+S)
listboxcarga=Listbox(framelistboxcarga, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=60, height=15)
listboxcarga.grid(row=0, column=0, sticky=N+S+E+W)
yscrollbar.config(command=listboxcarga.yview)
framelistboxcarga.place(x=60,y=117)
botonregreso=Button(cargadora,text="Cancelar", activebackground="orange", bd=6, width=25, bg="dark orange", command=regresar)
botonregreso.place(x=10,y=372)
botonjugar=Button(cargadora,text="Cargar y jugar!", command=cargarsopa,activebackground="orange", bd=6, width=25, bg="dark orange")
botonjugar.place(x=300,y=372)

#Ventana para jugar sopa de letras
juego=Toplevel(bg="black")
juego.withdraw()
juego.geometry("1325x670")
juego.resizable(0,0)
juego.title("Sopa de letras")
juego.attributes("-fullscreen", 1)
framelistbox=Frame(juego, bd=2, relief=SUNKEN, width=120, height=70)
yscrollbar = Scrollbar(framelistbox)
yscrollbar.grid(row=0, column=1, sticky=N+S)
imagencheat=PhotoImage(file="Imagenes/6573353.gif")
imagencheatt=Label(juego,image=imagencheat).place(x=200,y=80)
textocheat=Label(juego, text="Juega honestamente y así\nlo disfrutarás mejor",bg="black", fg="white",font=("Helvetica",20)).place(x=140,y=1)
instruccionestitulo=Label(juego, text="Instrucciones:",fg="dark orange",bg="black",font=("Helvetica",26,"bold"))
instruccionestitulo.place(x=20, y=590)
instrucciones=Label(juego, text="1-Inserte una palabra dentro del espacio, la cual debe encontrarse en la lista en la parte superior\n"\
                    +"2-Dale en el botón de (Comenzar búsqueda)\n3-Dale clic en las letras que forman las palabras",fg="white",bg="black", font=("Helvetica",16,"bold"))
instrucciones.place(x=20, y=640)
listbox=Listbox(framelistbox, bd=0,bg="black",fg="white",\
                   yscrollcommand=yscrollbar.set, width=60, height=15)
listbox.grid(row=0, column=0, sticky=N+S+E+W)
yscrollbar.config(command=listbox.yview)
framelistbox.place(x=60,y=300)
Entr=StringVar()
Entrad=Entry(juego, textvariable=Entr,bd=3,width=40).place(x=60,y=550)
Botonindicador=Button(juego, text="Modo búsqueda\ndesactivado",state="disabled",bd=3,bg="red",command=modobusquedafun)
Botonindicador.place(x=490,y=400)
Botonbusqueda=Button(juego, text="Comenzar búsqueda",activebackground="orange",bd=3,bg="dark orange",command=modobusquedafun).place(x=320,y=548)
Botoncerrar=Button(juego, text="Salir del juego",command=salir,activebackground="orange", bd=6, width=25, bg="dark orange").place(x=1100,y=625)
Botonregresomenupr=Button(juego, text="Regresar al menú principal",command=regresardesdejuego,activebackground="orange", bd=6, width=25, bg="dark orange").place(x=1100,y=675)    

'''Matriz de botones'''
framematriz=Frame(juego, bd=2, bg="dark orange",relief=SUNKEN, width=602, height=572).place(x=618,y=31)
b0=Button(juego,relief=RAISED,command=lambda:posiciones(0,0,b0), width=7,height=3,bg=color)
b0.place(x=620, y=33)
b1=Button(juego,relief=RAISED,command=lambda:posiciones(0,1,b1), width=7,height=3,bg=color)
b1.place(x=680, y=33)
b2=Button(juego,relief=RAISED,command=lambda:posiciones(0,2,b2), width=7,height=3,bg=color)
b2.place(x=740, y=33)
b3=Button(juego,relief=RAISED,command=lambda:posiciones(0,3,b3), width=7,height=3,bg=color)
b3.place(x=800, y=33)
b4=Button(juego,relief=RAISED,command=lambda:posiciones(0,4,b4), width=7,height=3,bg=color)
b4.place(x=860, y=33)
b5=Button(juego,relief=RAISED,command=lambda:posiciones(0,5,b5), width=7,height=3,bg=color)
b5.place(x=920, y=33)
b6=Button(juego,relief=RAISED,command=lambda:posiciones(0,6,b6), width=7,height=3,bg=color)
b6.place(x=980, y=33)
b7=Button(juego,relief=RAISED,command=lambda:posiciones(0,7,b7), width=7,height=3,bg=color)
b7.place(x=1040, y=33)
b8=Button(juego,relief=RAISED,command=lambda:posiciones(0,8,b8), width=7,height=3,bg=color)
b8.place(x=1100, y=33)
b9=Button(juego,relief=RAISED,command=lambda:posiciones(0,9,b9), width=7,height=3,bg=color)
b9.place(x=1160, y=33)
b10=Button(juego,relief=RAISED,command=lambda:posiciones(1,0,b10), width=7,height=3,bg=color)
b10.place(x=620, y=90)
b11=Button(juego,relief=RAISED,command=lambda:posiciones(1,1,b11), width=7,height=3,bg=color)
b11.place(x=680, y=90)
b12=Button(juego,relief=RAISED,command=lambda:posiciones(1,2,b12), width=7,height=3,bg=color)
b12.place(x=740, y=90)
b13=Button(juego,relief=RAISED,command=lambda:posiciones(1,3,b13), width=7,height=3,bg=color)
b13.place(x=800, y=90)
b14=Button(juego,relief=RAISED,command=lambda:posiciones(1,4,b14), width=7,height=3,bg=color)
b14.place(x=860, y=90)
b15=Button(juego,relief=RAISED,command=lambda:posiciones(1,5,b15), width=7,height=3,bg=color)
b15.place(x=920, y=90)
b16=Button(juego,relief=RAISED,command=lambda:posiciones(1,6,b16), width=7,height=3,bg=color)
b16.place(x=980, y=90)
b17=Button(juego,relief=RAISED,command=lambda:posiciones(1,7,b17), width=7,height=3,bg=color)
b17.place(x=1040, y=90)
b18=Button(juego,relief=RAISED,command=lambda:posiciones(1,8,b18), width=7,height=3,bg=color)
b18.place(x=1100, y=90)
b19=Button(juego,relief=RAISED,command=lambda:posiciones(1,9,b19), width=7,height=3,bg=color)
b19.place(x=1160, y=90)
b20=Button(juego,relief=RAISED,command=lambda:posiciones(2,0,b20), width=7,height=3,bg=color)
b20.place(x=620, y=147)
b21=Button(juego,relief=RAISED,command=lambda:posiciones(2,1,b21), width=7,height=3,bg=color)
b21.place(x=680, y=147)
b22=Button(juego,relief=RAISED,command=lambda:posiciones(2,2,b22), width=7,height=3,bg=color)
b22.place(x=740, y=147)
b23=Button(juego,relief=RAISED,command=lambda:posiciones(2,3,b23), width=7,height=3,bg=color)
b23.place(x=800, y=147)
b24=Button(juego,relief=RAISED,command=lambda:posiciones(2,4,b24), width=7,height=3,bg=color)
b24.place(x=860, y=147)
b25=Button(juego,relief=RAISED,command=lambda:posiciones(2,5,b25), width=7,height=3,bg=color)
b25.place(x=920, y=147)
b26=Button(juego,relief=RAISED,command=lambda:posiciones(2,6,b26), width=7,height=3,bg=color)
b26.place(x=980, y=147)
b27=Button(juego,relief=RAISED,command=lambda:posiciones(2,7,b27), width=7,height=3,bg=color)
b27.place(x=1040, y=147)
b28=Button(juego,relief=RAISED,command=lambda:posiciones(2,8,b28), width=7,height=3,bg=color)
b28.place(x=1100, y=147)
b29=Button(juego,relief=RAISED,command=lambda:posiciones(2,9,b29), width=7,height=3,bg=color)
b29.place(x=1160, y=147)
b30=Button(juego,relief=RAISED,command=lambda:posiciones(3,0,b30), width=7,height=3,bg=color)
b30.place(x=620, y=204)
b31=Button(juego,relief=RAISED,command=lambda:posiciones(3,1,b31), width=7,height=3,bg=color)
b31.place(x=680, y=204)
b32=Button(juego,relief=RAISED,command=lambda:posiciones(3,2,b32), width=7,height=3,bg=color)
b32.place(x=740, y=204)
b33=Button(juego,relief=RAISED,command=lambda:posiciones(3,3,b33), width=7,height=3,bg=color)
b33.place(x=800, y=204)
b34=Button(juego,relief=RAISED,command=lambda:posiciones(3,4,b34), width=7,height=3,bg=color)
b34.place(x=860, y=204)
b35=Button(juego,relief=RAISED,command=lambda:posiciones(3,5,b35), width=7,height=3,bg=color)
b35.place(x=920, y=204)
b36=Button(juego,relief=RAISED,command=lambda:posiciones(3,6,b36), width=7,height=3,bg=color)
b36.place(x=980, y=204)
b37=Button(juego,relief=RAISED,command=lambda:posiciones(3,7,b37), width=7,height=3,bg=color)
b37.place(x=1040, y=204)
b38=Button(juego,relief=RAISED,command=lambda:posiciones(3,8,b38), width=7,height=3,bg=color)
b38.place(x=1100, y=204)
b39=Button(juego,relief=RAISED,command=lambda:posiciones(3,9,b39), width=7,height=3,bg=color)
b39.place(x=1160, y=204)
b40=Button(juego,relief=RAISED,command=lambda:posiciones(4,0,b40), width=7,height=3,bg=color)
b40.place(x=620, y=261)
b41=Button(juego,relief=RAISED,command=lambda:posiciones(4,1,b41), width=7,height=3,bg=color)
b41.place(x=680, y=261)
b42=Button(juego,relief=RAISED,command=lambda:posiciones(4,2,b42), width=7,height=3,bg=color)
b42.place(x=740, y=261)
b43=Button(juego,relief=RAISED,command=lambda:posiciones(4,3,b43), width=7,height=3,bg=color)
b43.place(x=800, y=261)
b44=Button(juego,relief=RAISED,command=lambda:posiciones(4,4,b44), width=7,height=3,bg=color)
b44.place(x=860, y=261)
b45=Button(juego,relief=RAISED,command=lambda:posiciones(4,5,b45), width=7,height=3,bg=color)
b45.place(x=920, y=261)
b46=Button(juego,relief=RAISED,command=lambda:posiciones(4,6,b46), width=7,height=3,bg=color)
b46.place(x=980, y=261)
b47=Button(juego,relief=RAISED,command=lambda:posiciones(4,7,b47), width=7,height=3,bg=color)
b47.place(x=1040, y=261)
b48=Button(juego,relief=RAISED,command=lambda:posiciones(4,8,b48), width=7,height=3,bg=color)
b48.place(x=1100, y=261)
b49=Button(juego,relief=RAISED,command=lambda:posiciones(4,9,b49), width=7,height=3,bg=color)
b49.place(x=1160, y=261)
b50=Button(juego,relief=RAISED,command=lambda:posiciones(5,0,b50), width=7,height=3,bg=color)
b50.place(x=620, y=318)
b51=Button(juego,relief=RAISED,command=lambda:posiciones(5,1,b51), width=7,height=3,bg=color)
b51.place(x=680, y=318)
b52=Button(juego,relief=RAISED,command=lambda:posiciones(5,2,b52), width=7,height=3,bg=color)
b52.place(x=740, y=318)
b53=Button(juego,relief=RAISED,command=lambda:posiciones(5,3,b53), width=7,height=3,bg=color)
b53.place(x=800, y=318)
b54=Button(juego,relief=RAISED,command=lambda:posiciones(5,4,b54), width=7,height=3,bg=color)
b54.place(x=860, y=318)
b55=Button(juego,relief=RAISED,command=lambda:posiciones(5,5,b55), width=7,height=3,bg=color)
b55.place(x=920, y=318)
b56=Button(juego,relief=RAISED,command=lambda:posiciones(5,6,b56), width=7,height=3,bg=color)
b56.place(x=980, y=318)
b57=Button(juego,relief=RAISED,command=lambda:posiciones(5,7,b57), width=7,height=3,bg=color)
b57.place(x=1040, y=318)
b58=Button(juego,relief=RAISED,command=lambda:posiciones(5,8,b58), width=7,height=3,bg=color)
b58.place(x=1100, y=318)
b59=Button(juego,relief=RAISED,command=lambda:posiciones(5,9,b59), width=7,height=3,bg=color)
b59.place(x=1160, y=318)
b60=Button(juego,relief=RAISED,command=lambda:posiciones(6,0,b60), width=7,height=3,bg=color)
b60.place(x=620, y=375)
b61=Button(juego,relief=RAISED,command=lambda:posiciones(6,1,b61), width=7,height=3,bg=color)
b61.place(x=680, y=375)
b62=Button(juego,relief=RAISED,command=lambda:posiciones(6,2,b62), width=7,height=3,bg=color)
b62.place(x=740, y=375)
b63=Button(juego,relief=RAISED,command=lambda:posiciones(6,3,b63), width=7,height=3,bg=color)
b63.place(x=800, y=375)
b64=Button(juego,relief=RAISED,command=lambda:posiciones(6,4,b64), width=7,height=3,bg=color)
b64.place(x=860, y=375)
b65=Button(juego,relief=RAISED,command=lambda:posiciones(6,5,b65), width=7,height=3,bg=color)
b65.place(x=920, y=375)
b66=Button(juego,relief=RAISED,command=lambda:posiciones(6,6,b66), width=7,height=3,bg=color)
b66.place(x=980, y=375)
b67=Button(juego,relief=RAISED,command=lambda:posiciones(6,7,b67), width=7,height=3,bg=color)
b67.place(x=1040, y=375)
b68=Button(juego,relief=RAISED,command=lambda:posiciones(6,8,b68), width=7,height=3,bg=color)
b68.place(x=1100, y=375)
b69=Button(juego,relief=RAISED,command=lambda:posiciones(6,9,b69), width=7,height=3,bg=color)
b69.place(x=1160, y=375)
b70=Button(juego,relief=RAISED,command=lambda:posiciones(7,0,b70), width=7,height=3,bg=color)
b70.place(x=620, y=432)
b71=Button(juego,relief=RAISED,command=lambda:posiciones(7,1,b71), width=7,height=3,bg=color)
b71.place(x=680, y=432)
b72=Button(juego,relief=RAISED,command=lambda:posiciones(7,2,b72), width=7,height=3,bg=color)
b72.place(x=740, y=432)
b73=Button(juego,relief=RAISED,command=lambda:posiciones(7,3,b73), width=7,height=3,bg=color)
b73.place(x=800, y=432)
b74=Button(juego,relief=RAISED,command=lambda:posiciones(7,4,b74), width=7,height=3,bg=color)
b74.place(x=860, y=432)
b75=Button(juego,relief=RAISED,command=lambda:posiciones(7,5,b75), width=7,height=3,bg=color)
b75.place(x=920, y=432)
b76=Button(juego,relief=RAISED,command=lambda:posiciones(7,6,b76), width=7,height=3,bg=color)
b76.place(x=980, y=432)
b77=Button(juego,relief=RAISED,command=lambda:posiciones(7,7,b77), width=7,height=3,bg=color)
b77.place(x=1040, y=432)
b78=Button(juego,relief=RAISED,command=lambda:posiciones(7,8,b78), width=7,height=3,bg=color)
b78.place(x=1100, y=432)
b79=Button(juego,relief=RAISED,command=lambda:posiciones(7,9,b79), width=7,height=3,bg=color)
b79.place(x=1160, y=432)
b80=Button(juego,relief=RAISED,command=lambda:posiciones(8,0,b80), width=7,height=3,bg=color)
b80.place(x=620, y=489)
b81=Button(juego,relief=RAISED,command=lambda:posiciones(8,1,b81), width=7,height=3,bg=color)
b81.place(x=680, y=489)
b82=Button(juego,relief=RAISED,command=lambda:posiciones(8,2,b82), width=7,height=3,bg=color)
b82.place(x=740, y=489)
b83=Button(juego,relief=RAISED,command=lambda:posiciones(8,3,b83), width=7,height=3,bg=color)
b83.place(x=800, y=489)
b84=Button(juego,relief=RAISED,command=lambda:posiciones(8,4,b84), width=7,height=3,bg=color)
b84.place(x=860, y=489)
b85=Button(juego,relief=RAISED,command=lambda:posiciones(8,5,b85), width=7,height=3,bg=color)
b85.place(x=920, y=489)
b86=Button(juego,relief=RAISED,command=lambda:posiciones(8,6,b86), width=7,height=3,bg=color)
b86.place(x=980, y=489)
b87=Button(juego,relief=RAISED,command=lambda:posiciones(8,7,b87), width=7,height=3,bg=color)
b87.place(x=1040, y=489)
b88=Button(juego,relief=RAISED,command=lambda:posiciones(8,8,b88), width=7,height=3,bg=color)
b88.place(x=1100, y=489)
b89=Button(juego,relief=RAISED,command=lambda:posiciones(8,9,b89), width=7,height=3,bg=color)
b89.place(x=1160, y=489)
b90=Button(juego,relief=RAISED,command=lambda:posiciones(9,0,b90), width=7,height=3,bg=color)
b90.place(x=620, y=546)
b91=Button(juego,relief=RAISED,command=lambda:posiciones(9,1,b91), width=7,height=3,bg=color)
b91.place(x=680, y=546)
b92=Button(juego,relief=RAISED,command=lambda:posiciones(9,2,b92), width=7,height=3,bg=color)
b92.place(x=740, y=546)
b93=Button(juego,relief=RAISED,command=lambda:posiciones(9,3,b93), width=7,height=3,bg=color)
b93.place(x=800, y=546)
b94=Button(juego,relief=RAISED,command=lambda:posiciones(9,4,b94), width=7,height=3,bg=color)
b94.place(x=860, y=546)
b95=Button(juego,relief=RAISED,command=lambda:posiciones(9,5,b95), width=7,height=3,bg=color)
b95.place(x=920, y=546)
b96=Button(juego,relief=RAISED,command=lambda:posiciones(9,6,b96), width=7,height=3,bg=color)
b96.place(x=980, y=546)
b97=Button(juego,relief=RAISED,command=lambda:posiciones(9,7,b97), width=7,height=3,bg=color)
b97.place(x=1040, y=546)
b98=Button(juego,relief=RAISED,command=lambda:posiciones(9,8,b98), width=7,height=3,bg=color)
b98.place(x=1100, y=546)
b99=Button(juego,relief=RAISED,command=lambda:posiciones(9,9,b99), width=7,height=3,bg=color)
b99.place(x=1160, y=546)

'''Ventana de felicitaciones'''
felicitaciones=Toplevel()
felicitaciones.withdraw()
felicitaciones.geometry("550x390")
felicitaciones.config(bg="black")
textofel=Label(felicitaciones,text="Enhorabuena! Habéis\nhecho la sopa!",font=("Verdana",24),fg="#00FF40",bg="black")
textofel.place(x=100,y=10)
textofel2=Label(felicitaciones, text="Pero como dijo Boromir: Uno simplemente no deja de\n jugar sopa de letras ;)",font=("Verdana",14),fg="dark orange",bg="black")
textofel2.place(x=5,y=90)
textofel3=Label(felicitaciones, text="Hasta la próxima :D",font=("Verdana",14),fg="#0B40CF",bg="black")
textofel3.place(x=179,y=145)
imagenfin=PhotoImage(file="Imagenes/6582776.gif")
imagenfinn=Label(felicitaciones,image=imagenfin).place(x=35,y=180)
botonsalir=Button(felicitaciones,text="Salir", activebackground="orange", bd=6, width=21, bg="dark orange",command=salirtotal)
botonsalir.place(x=343,y=250)
botonregresomenu=Button(felicitaciones,text="Regresar al menú principal", activebackground="orange", bd=6, width=21, bg="dark orange",command=regresar)
botonregresomenu.place(x=343,y=290)

vK=Toplevel()
imagenVisua=PhotoImage(file="Imagenes/ideaplantilla.gif")
Label(vK,image=imagenVisua).place(x=0,y=0)
#-------------------------------------------------------------------------------------------------------

#Comando de ejecución de interfaz
v0.mainloop()
