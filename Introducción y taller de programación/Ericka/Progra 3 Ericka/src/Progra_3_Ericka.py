# -*- coding: cp1252 -*-
from Tkinter import *
from tkMessageBox import *
from time import *
import pickle

#------------------------------------------------------------------------------------
#Instituto Tecológico de Costa Rica
#Carrera de Ingeniería en Computación
#Curso de Taller de Programación
#Profesora: Ericka Solano Fernández
#Tercer Proyecto Programado: Generador de presupuestos
#Estudiante: Pedro Rodríguez de Oliveira
#II semestre
#2013
#------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
#Variables globales
#----------------------------------------------------------------------------------
#Lista de rubros usados en el editor de presupuestos
listarubros=[]
#Lista de presupuestos creados por el usuario
presupuestoshechos=[]
#Lista de rburos a la hora de usar el visualizador de presupuestos
rubrosacargar=[]
#Lista con el nombre de variables
labelsRealVal=["Realval1","Realval2","Realval3","Realval4","Realval5","Realval6","Realval7","Realval8","Realval9","Realval10"]
#Nombre con el que se cargará/guardará presupuestos
nombre=""
#Variables para la edicion de totales en el visualizador de presupuestos
totalingresosestimado=0
totalegresosestimado=0
totalingresosreal=0
totalegresosreal=0
totalingresosdiferencia=0
totalegresosdiferencia=0

#----------------------------------------------------------------------------------
#Clases
#----------------------------------------------------------------------------------
class Rubro:
    def __init__(self,Nombre,Monto,Tipo,Real):
        self.Nombre=Nombre
        self.Monto=Monto
        self.Tipo=Tipo
        self.Real=Real
    
    def getRubro(self):
        return [self.Nombre,self.Monto,self.Tipo,self.Real]

#----------------------------------------------------------------------------------
#Funciones
#----------------------------------------------------------------------------------
#Funciones propias de interfaz
#Abre el creador de presupuestos
def abrircreador():
    global EntryGuardar,EntryNombre,EntrMonto,EntryRubroBorrar,listarubros,EntrTipo
    EntryGuardar.delete(0,END)
    EntryNombre.delete(0,END)
    EntrMonto.set(0)
    EntryRubroBorrar.delete(0,END)
    EntrTipo.set("-Elige el tipo-")
    listarubros=[]
    adicionaralistbox()
    vCarga.withdraw()
    vCreaPresu.deiconify()

#Sale del programa
def salir():
    pregunta=askokcancel("Desea salir?","Desea salir del programa? Todo progreso no salvo se perderá")
    if pregunta:
        v0.destroy()

#Regresa al menu principal
def regresarmenu():
    global EntryCarga
    pregunta=askokcancel("Desea salir?","Desea salir hacia el menú principal? Todo progreso no salvo se perderá")
    if pregunta:
        EntryCarga.delete(0,END)
        cargarpresupuestoshechos()
        vCreaPresu.withdraw()
        vVisual.withdraw()
        vCarga.deiconify()

#Muestra ventana con créditos
def creditos():
    showinfo("Créditos","Hecho por Pedro Rodríguez de Oliveira\nEstudiante del Instituto Tecnológico de Costa Rica\nPara el curso de Taller de Programación\n2013")

#Carga la listbox de presupuestos hechos
def cargarpresupuestoshechos():
    global presupuestoshechos,vCarga,listboxcarga
    presupuestoshechos=[]
    f=open("Archivo de guardado/Titulos creados.txt","r")
    texto=f.readlines()
    for i in texto:
        if i[0]=="*":
            liste=i[1:]
            presupuestoshechos+=[liste]
    listboxcarga.delete(0,END)
    for i in presupuestoshechos:
        listboxcarga.insert(END,i)

#Agrega nuevo rubro a listbox de creador de presupuestos
def adicionaralistbox():
    global listarubros
    listboxcrea.delete(0,END)
    for i in listarubros:
        listboxcrea.insert(END,i.getRubro())

#Elimina rubro de listbox de creador de presupuestos
def eliminardelistbox():
    global listarubros,EntryRubroBorrar
    nombrerubro=EntryRubroBorrar.get()
    cond=False
    for i in listarubros:
        if i.Nombre==nombrerubro:
            cond=True
            x=listarubros.index(i)
            listarubros.remove(i)
            listboxcrea.delete(x)
    if cond==False:
        showerror("Error","Error, lo insertado no está presente en la lista de rubros creados")
    EntryRubroBorrar.delete(0,END)
    
#Combina funciones de crear rubro y actualizar listbox
def guardar_clase_y_actualizar_listbox():
    crearclase()
    adicionaralistbox()

#Combina funciones de eliminar rubro y actualizar listbox
def eliminar_de_lista_y_actualizar_listbox():
    eliminardelistbox()
    adicionaralistbox()

#Confirma si se puede abrir ventana de presupuestos o no
def ventanaguardarpresupuesto():
    global listarubros
    if listarubros==[]:
        showerror ("Error","La lista de rubros está vacía. No se puede guardar este presupuesto")
    elif len(listarubros)>10:
        showerror("Error","Hay demasiados rubros. Intente ser lo más conciso posible.\nSolo se pueden crear 10 rubros en total.")
    else:
        vGuarda.deiconify()

#Guarda presupuesto desde ventana de visualización de presupuestos
def actualizarpresupuesto():
    global nombre,rubrosacargar
    f=open("Archivo de guardado/"+str(nombre)+".txt","wb")
    pickle.dump(rubrosacargar,f)
    f.close()
    showinfo("Exito","Las ediciones en el presupuesto fueron guardadas exitosamente")

#Guarda presupuesto en un txt
def guardarentxt():
    global listarubros,presupuestoshechos,nombre
    nombre=""
    nombre=EntrGuardar.get()
    if nombre!="":
        f=open("Archivo de guardado/"+str(nombre)+".txt","wb")
        pickle.dump(listarubros,f)
        f.close()
        f=open("Archivo de guardado/Titulos creados.txt","r")
        texto=f.readlines()
        nombreb="*"+str(nombre)+"\n"
        if nombreb not in texto:
            f.close()
            f=open("Archivo de guardado/Titulos creados.txt","a")
            f.write("*"+str(nombre)+"\n")
            presupuestoshechos.append(nombre)
            f.close()
            cargarpresupuestoshechos()
        showinfo ("Proceso exitoso","Felicidades, el presupuesto fue guardado.")
        vGuarda.withdraw()
        vCreaPresu.withdraw()
        vCarga.deiconify()
    else:
        showerror("Error","Error, debes insertar un nombre")

#Muestra instrucciones del creador de presupuestos
def instruccionescreapresupuesto():
    showinfo ("Instrucciones","Para usar el creador de presupuestos:\n1)Inserta un rubro que componga tu presupuesto (tal como Escuela, Familia, Trabajo) en la sección Nombre del Rubro\n2)Inserta el monto de dicho rubro en Monto del Rubro (debe ser mayor a 0, porque es un estimado)\n3)Elige en el Tipo de Rubro si es un Ingreso (Entrada) o Egreso (Salida)\n4)Ingresa el rubro dándole clic al boton Ingresar Rubro\n5)Si el rubro ya existe, podrás cambiar los datos al reingresarlo con el mismo nombre, solamente insertando diferentes datos\n6)Si deseas borrar un rubro, pon el nombre del mismo en el cuadro de texto y dale clic al botón de Borrar rubro\n7)Recuerda que sólo puedes crear diez rubros. Trata de ser conciso y específico con los mismos para así evitar redundancias\n8)Para guardar el presupuesto, ve al menú de Opciones/Guardar presupuesto\n9)Listo! Puedes salir clickeando en las opciones de Regresar al menú principal o Salir (todo esto en el menú de Opciones).")

#Muestra instrucciones del visualizador de presupuestos
def instruccionesvisualpresupuesto():
    showinfo ("Instrucciones","Para usar el visualizador de presupuestos:\n1)Puedes editar el monto real de algún rubro con solo insertar el nombre y dándole clic a Modificar valor actual\n2)La columna de DIferencia indica cuanta plata pierdes o ganas de acuerdo al monto real de cada rubro.\n3)Para guardar las modificaciones en el monto real, ve a Opciones/Guardar presupuesto y se guardarán los cambios\n4)Listo! Puedes salir clickeando en las opciones de Regresar al menú principal o Salir (todo esto en el menú de Opciones)")
    
#Edita todos los labels dentro de la pagina de visualizacion
def configurarlabels():
    global Rubro1,Rubro2,Rubro3,Rubro4,Rubro5,Rubro6,Rubro7,Rubro7,Rubro8,Rubro9,Rubro10
    global Estimado1,Estimado2,Estimado3,Estimado4,Estimado5,Estimado6,Estimado7,Estimado7,Estimado8,Estimado9,Estimado10,EstimadoTotal
    global Diferencia1,Diferencia2,Diferencia3,Diferencia4,Diferencia5,Diferencia6,Diferencia7,Diferencia7,Diferencia8,Diferencia9,Diferencia10,DiferenciaTotal
    global Realval1,Realval2,Realval3,Realval4,Realval5,Realval6,Realval7,Realval8,Realval9,Realval10
    global Real1,Real2,Real3,Real4,Real5,Real6,Real7,Real8,Real9,Real10
    global BotonEstado,labelsRealVal,rubrosacargar,totalingresosestimado,totalegresosestimado,totalingresosreal,totalegresosreal,totalingresosdiferencia,totalegresosdiferencia
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10
    for i in [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]:
        i.delete(0,END)
    vCarga.withdraw()
    vVisual.state("zoomed")
    vVisual.deiconify()
    for i in [Rubro1,Rubro2,Rubro3,Rubro4,Rubro5,Rubro6,Rubro7,Rubro7,Rubro8,Rubro9,Rubro10]:
        i.configure(text="")
    for i in [Real1,Real2,Real3,Real4,Real5,Real6,Real7,Real8,Real9,Real10]:
        i.configure(text="Valor Actual=")
    for i in [Realval1,Realval2,Realval3,Realval4,Realval5,Realval6,Realval7,Realval8,Realval9,Realval10]:
        i=0
    w=len(rubrosacargar)
    x=0
    labelsRubro=[Rubro1,Rubro2,Rubro3,Rubro4,Rubro5,Rubro6,Rubro7,Rubro7,Rubro8,Rubro9,Rubro10]
    while w!=0:
        labelsRubro[x].configure(text=rubrosacargar[x].Nombre)
        x+=1
        w-=1
    labelsEstimado=[Estimado1,Estimado2,Estimado3,Estimado4,Estimado5,Estimado6,Estimado7,Estimado7,Estimado8,Estimado9,Estimado10]
    for i in labelsEstimado:
        i.configure(text="")
    w=len(rubrosacargar)
    x=0
    totalingresosestimado=0
    totalegresosestimado=0
    while w!=0:
        if rubrosacargar[x].Tipo=='Egreso (Salida)':
            labelsEstimado[x].configure(text="-"+str(rubrosacargar[x].Monto))
            totalegresosestimado+=rubrosacargar[x].Monto
            x+=1
            w-=1       
        else:
            labelsEstimado[x].configure(text="+"+str(rubrosacargar[x].Monto))
            totalingresosestimado+=rubrosacargar[x].Monto
            x+=1
            w-=1
    EstimadoTotal.configure(text=str(totalingresosestimado-totalegresosestimado))
    labelsReal=[Real1,Real2,Real3,Real4,Real5,Real6,Real7,Real8,Real9,Real10]
    labelsRealval=[Realval1,Realval2,Realval3,Realval4,Realval5,Realval6,Realval7,Realval8,Realval9,Realval10]
    for i in labelsRealval:
        i=""
    w=len(rubrosacargar)
    x=0
    totalegresosreal=0
    totalingresosreal=0
    while w!=0:
        labelsRealVal[x]=rubrosacargar[x].Real
        if rubrosacargar[x].Tipo=='Egreso (Salida)':
            labelsReal[x].configure(text="Valor actual= "+"-"+str(labelsRealVal[x]))
            totalegresosreal+=rubrosacargar[x].Real
        else:
            labelsReal[x].configure(text="Valor actual= "+"+"+str(labelsRealVal[x]))
            totalingresosreal+=rubrosacargar[x].Real
        x+=1
        w-=1
    labelsDiferencia=[Diferencia1,Diferencia2,Diferencia3,Diferencia4,Diferencia5,Diferencia6,Diferencia7,Diferencia7,Diferencia8,Diferencia9,Diferencia10]
    for i in labelsDiferencia:
        i.configure(text="")
    w=len(rubrosacargar)
    x=0
    totalingresosdiferencia=0
    totalegresosdiferencia=0
    while w!=0:
        labelsDiferencia[x].configure(text=str(rubrosacargar[x].Monto-rubrosacargar[x].Real))
        if rubrosacargar[x].Tipo=='Egreso (Salida)':
            labelsDiferencia[x].configure(text=str(rubrosacargar[x].Monto-rubrosacargar[x].Real))
            totalegresosdiferencia+=rubrosacargar[x].Monto-rubrosacargar[x].Real
        else:
            labelsDiferencia[x].configure(text=str(rubrosacargar[x].Real-rubrosacargar[x].Monto))
            totalingresosdiferencia+=rubrosacargar[x].Monto-rubrosacargar[x].Real
        x+=1
        w-=1
    DiferenciaTotal.configure(text=str(totalegresosdiferencia-totalingresosdiferencia))
    if (totalingresosreal-totalegresosreal)>=0:
        BotonEstado.configure(bg="green")
        RealTotal.configure(text=str(totalingresosreal-totalegresosreal),bg="green")
    else:
        BotonEstado.configure(bg="red")
        RealTotal.configure(text=str(totalingresosreal-totalegresosreal),bg="red")
    
#----------------------------------------------------------------------------------------------------------------------
#Funciones que implican el uso de clases
#Carga el presupuesto para el visualizador
def cargarpresupuesto():
    global rubrosacargar,EntryCarga,vVisual,TituloPresu,nombre
    rubrosacargar=[]
    nombre=EntryCarga.get()
    f=open("Archivo de guardado/Titulos creados.txt","r")
    texto=f.readlines()
    nombreb="*"+str(nombre)+"\n"
    if nombreb not in texto:
        showerror("Error","Error, no existe tal presupuesto")
    else:
        f=open("Archivo de guardado/"+str(nombre)+".txt","rb")
        rubrosacargar=pickle.load(f)
        TituloPresu.configure(text=nombre)
        configurarlabels()
            
#Carga un presupuesto guardado para ser editado en el creador de presupuestos
def editarpresupuesto():
    global listarubros,EntryCarga,vCreaPresu,TituloPresu,nombre,EntrGuardar,EntrMonto,EntryRubroBorrar,EntrTipo,EntryNombre
    listarubros=[]
    nombre=EntryCarga.get()
    f=open("Archivo de guardado/Titulos creados.txt","r")
    texto=f.readlines()
    nombreb="*"+str(nombre)+"\n"
    if nombreb not in texto:
        showerror("Error","Error, no existe tal presupuesto")
    else:
        f=open("Archivo de guardado/"+str(nombre)+".txt","rb")
        listarubros=pickle.load(f)
        EntryNombre.delete(0,END)
        EntrMonto.set(0)
        EntryRubroBorrar.delete(0,END)
        EntrTipo.set("-Elige el tipo-")
        EntrGuardar.set(str(nombre))
        vCarga.withdraw()
        vCreaPresu.deiconify()
        adicionaralistbox()
    
#Crea un nuevo rubro
def crearclase():
    global EntryNombre,EntryMonto,listarubros,EntrTipo
    Nombre=EntryNombre.get()
    Tipo=EntrTipo.get()
    try:
        Monto=int(EntryMonto.get())
        if Nombre=="" or Monto<=0 or Tipo not in ["Ingreso (Entrada)", "Egreso (Salida)"]:
            showerror("Error","Error, algunos de los datos no son correctos. Recuerda:\nDebe haber un nombre.\nMonto debe ser mayor a 0\nDebes cambiar el tipo de rubro a Ingreso o Egreso")
        else:
            Real=Monto
            p=Rubro(Nombre,Monto,Tipo,Real)
            cond=False
            for i in listarubros:
                if i.Nombre==Nombre:
                    pregunta=askokcancel("Cambiar valores del rubro?","Tienes un rubro con el mismo nombre. Desea cambiar sus valores?")
                    cond=True
                    if pregunta:
                        i.Monto=Monto
                        i.Tipo=Tipo
                        i.Real=Monto
                        EntrTipo.set("-Elige el tipo-")
                        EntryNombre.delete(0,END)
                        EntryMonto.delete(0,END)
            if cond==False:
                listarubros.append(p)
                EntrTipo.set("-Elige el tipo-")
                EntryMonto.delete(0,END)
                EntryNombre.delete(0,END)
    except:
        showerror("Error","Error, en el monto no has insertado un número. Favor intentar de nuevo")
            
#Edita la clase en la ventana de visualizacion
def modificarcalsevisual(valor,pos):
    global rubrosacargar
    global Diferencia1,Diferencia2,Diferencia3,Diferencia4,Diferencia5,Diferencia6,Diferencia7,Diferencia7,Diferencia8,Diferencia9,Diferencia10,DiferenciaTotal
    global Realval1,Realval2,Realval3,Realval4,Realval5,Realval6,Realval7,Realval8,Realval9,Realval10
    global Real1,Real2,Real3,Real4,Real5,Real6,Real7,Real8,Real9,Real10
    global BotonEstado,rubrosacargar,totalingresosreal,totalegresosreal,totalingresosdiferencia,totalegresosdiferencia,labelsRealVal
    if not isinstance(labelsRealVal[pos],int):
        showerror ("Error", "Error, tal rubro no existe")
    else:
        try:
            if int(valor)<0:
                showerror ("Error", "Error, lo insertado es menor a cero, no es válido")
            else:
                rubrosacargar[pos].Real=int(valor)
                configurarlabels()
        except:
            showerror ("Error", "Error, lo insertado no es un número, intente nuevamente")
#----------------------------------------------------------------------------------
#Interfaz
#----------------------------------------------------------------------------------
#Ventana principal
v0=Tk()
v0.withdraw()
v0.geometry("800x680")

#Ventana de carga de presupuesto creado
vCarga=Toplevel()
vCarga.withdraw()
vCarga.geometry("418x451")
vCarga.title("Cargar Presupuesto")
vCarga.resizable(0,0)
Label(vCarga, text="Bienvenido al creador de presupuestos.\nAquí podrás escoger los presupuestos creados por ti.\nSi no tienes uno, dale al botón Crear presupuesto nuevo.", font=("Helvetica",11,"bold")).place(x=5,y=5)
Button(vCarga, text="Crear presupuesto nuevo", command=abrircreador,activebackground="#FF0101").place(x=140, y=67)
Label(vCarga, text="Presupuestos creados:", font=("Helvetica",9)).place(x=2,y=84)
framelistboxcarga=Frame(vCarga, bd=2, relief=SUNKEN, width=120, height=70)
yscrollbar = Scrollbar(framelistboxcarga)
yscrollbar.grid(row=0, column=1, sticky=N+S)
listboxcarga=Listbox(framelistboxcarga, bd=0,bg="white",\
                   yscrollcommand=yscrollbar.set, width=60, height=12)
listboxcarga.grid(row=0, column=0, sticky=N+S+E+W)
yscrollbar.config(command=listboxcarga.yview)
framelistboxcarga.place(x=17,y=107)
Label(vCarga, text="Si has creado algún presupuesto, revisa la lista superior.\nEn el cuadro de texto, inserta el nombre de la lista\ny dale clic a Visualizar presupuesto", font=("Helvetica",11,"bold")).place(x=6,y=310)
Label(vCarga, text="Nota: Clickea el nombre deseado en la lista y lo subrayado indica como este está escrito", font=("Helvetica",7)).place(x=19,y=367)
EntrCarga=StringVar()
EntryCarga=Entry(vCarga,textvariable=EntrCarga,width=65)
EntryCarga.place(x=12,y=390)
Button(vCarga, text="Editar presupuesto",activebackground="#FF0101",command=editarpresupuesto).place(x=80, y=415)
Button(vCarga, text="Visualizar presupuesto",activebackground="#FF0101",command=cargarpresupuesto).place(x=200, y=415)
Button(vCarga, text="Salir",activebackground="#FF0101",command=salir).place(x=370, y=415)

#Ventana de presentación
vPres=Toplevel()
vPres.geometry("678x180")
vPres.config(bg="dark slate grey")
vPres.resizable(0, 0)
vPres.title("Bienvenido!")
imagenPres=PhotoImage(file="Imagenes/Exitoso.gif")
vPres.after(4000,vPres.withdraw)
vPres.after(2000,cargarpresupuestoshechos)
vPres.after(4000,vCarga.deiconify)
Label(vPres, text="Generador de Presupuestos",font=("Impact",28),bg="dark slate grey", fg="white").place(x=58,y=5)
Label(vPres, text="Instituto Tecnológico de Costa Rica\n2013", font=("Helvetica",24),bg="dark slate grey", fg="white").place(x=15,y=64)
Label(vPres, text="Cargando...", font=("SimHei",17),bg="dark slate grey", fg="white").place(x=220,y=150)
Label(vPres, image=imagenPres).place(x=540,y=1)

#Ventana de creación de presupuestos
vCreaPresu=Toplevel()
vCreaPresu.withdraw()
vCreaPresu.geometry("468x570")
vCreaPresu.resizable(0, 0)
vCreaPresu.title("Crear presupuesto nuevo")
menubarra = Menu(vCreaPresu)
opcionmenu = Menu(menubarra, tearoff=0)
opcionmenu.add_command(label="Guardar presupuesto",command=ventanaguardarpresupuesto)
opcionmenu.add_command(label="Regresar al menú principal",command=regresarmenu) 
opcionmenu.add_separator()
opcionmenu.add_command(label="Salir del programa",command=salir)
menubarra.add_cascade(label="Opciones", menu=opcionmenu)
instruccionesmenu=Menu(menubarra,tearoff=0)
instruccionesmenu.add_command(label="Instrucciones",command=instruccionescreapresupuesto)
menubarra.add_cascade(label="Instrucciones", menu=instruccionesmenu)
creditosmenu=Menu(menubarra,tearoff=0)
creditosmenu.add_command(label="Hecho por...",command=creditos)
menubarra.add_cascade(label="Créditos", menu=creditosmenu)
imagenCrea=PhotoImage(file="Imagenes/presupuesto_blog-banesco.gif")
Label(vCreaPresu, image=imagenCrea).place(x=0,y=0)
Label(vCreaPresu, text="Crea tu nuevo presupuesto!", font=("Helvetica",28),bg="white").place(x=3,y=10)
Label(vCreaPresu, text="Nombre del rubro", font=("Helvetica",13,"bold"),bg="white").place(x=3,y=79)
EntrNombre=StringVar()
EntryNombre=Entry(vCreaPresu,textvariable=EntrNombre,width=51)
EntryNombre.place(x=147,y=81)
Label(vCreaPresu, text="Monto del rubro", font=("Helvetica",13,"bold"),bg="white").place(x=3,y=120)
EntrMonto=IntVar()
EntryMonto=Entry(vCreaPresu,textvariable=EntrMonto,width=53)
EntryMonto.place(x=137,y=120)
Label(vCreaPresu, text="Tipo de rubro", font=("Helvetica",13,"bold"),bg="white").place(x=3,y=160)
EntrTipo=StringVar()
EntrTipo.set("-Elige el tipo-")
OptionMenu(vCreaPresu, EntrTipo, "Ingreso (Entrada)", "Egreso (Salida)").place(x=123,y=155)
Button(vCreaPresu,text="Ingresar rubro",width=20,command=guardar_clase_y_actualizar_listbox).place(x=160,y=196)
Label(vCreaPresu, text="Inserte nombre del rubro a borrar:", font=("Helvetica",13,"bold"),bg="white").place(x=5,y=247)
EntrRubroBorrar=StringVar()
EntryRubroBorrar=Entry(vCreaPresu,textvariable=EntrRubroBorrar,width=60)
EntryRubroBorrar.place(x=5,y=270)
Button(vCreaPresu,text="Borrar rubro",command=eliminar_de_lista_y_actualizar_listbox).place(x=384,y=265)
listboxcreador=Frame(vCreaPresu, bd=2, relief=SUNKEN, width=150, height=70)
yscrollbar = Scrollbar(listboxcreador)
yscrollbar.grid(row=0, column=1, sticky=N+S)
listboxcrea=Listbox(listboxcreador, bd=0,bg="white",fg="#5858FA",\
                   yscrollcommand=yscrollbar.set, width=68, height=15)
listboxcrea.grid(row=0, column=0, sticky=N+S+E+W)
yscrollbar.config(command=listboxcrea.yview)
listboxcreador.place(x=17,y=302)

#Ventana Guardado
vGuarda=Toplevel()
vGuarda.withdraw()
vGuarda.geometry("370x50")
vGuarda.title("Guardar como...")
Label(vGuarda, text="Favor inserta un nombre para tu presupuesto:",font=("Helvetica",10,"bold")).place(x=10,y=1)
EntrGuardar=StringVar()
EntryGuardar=Entry(vGuarda,textvariable=EntrGuardar,width=48)
EntryGuardar.place(x=12,y=25)
Button(vGuarda,text="Guardar",command=guardarentxt).place(x=310,y=21)

#Ventana visualización
vVisual=Toplevel()
vVisual.withdraw()
vVisual.geometry("1366x738")
vVisual.title("Visualizando presupuesto")
tex2="Nuevo valor del rubro:"
tex3="Modificar valor actual"
colorrojo="#FE2E2E"
coloramarillo="yellow"
menubarra2 = Menu(vVisual)
opcionmenu2 = Menu(menubarra2, tearoff=0)
opcionmenu2.add_command(label="Guardar presupuesto",command=actualizarpresupuesto)
opcionmenu2.add_command(label="Regresar al menú principal",command=regresarmenu) 
opcionmenu2.add_separator()
opcionmenu2.add_command(label="Salir del programa",command=salir)
menubarra2.add_cascade(label="Opciones", menu=opcionmenu2)
instruccionesmenu2=Menu(menubarra,tearoff=0)
instruccionesmenu2.add_command(label="Instrucciones",command=instruccionesvisualpresupuesto)
menubarra2.add_cascade(label="Instrucciones", menu=instruccionesmenu2)
creditosmenu2=Menu(menubarra2,tearoff=0)
creditosmenu2.add_command(label="Hecho por...",command=creditos)
menubarra2.add_cascade(label="Créditos", menu=creditosmenu2)
imagenVisua=PhotoImage(file="Imagenes/ideaplantilla.gif")
Label(vVisual,image=imagenVisua).place(x=0,y=0)
TituloPresu=Label(vVisual,text="---------------------",font=("Helvetica",37),bg="white")
TituloPresu.place(x=565,y=3)
BotonEstado=Button(vVisual, state="disabled",width=47,height=4,bg="white")
BotonEstado.place(x=688,y=610)
#Fila 1---------------------------------------------------------------------------------------
Realval1=""
Real1=Label(vVisual,text="Valor actual="+str(Realval1),bg=colorrojo)
Real1.place(x=688,y=158)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=179)
Rubro1=Label(vVisual,bg="white",font=10)
Rubro1.place(x=3,y=162)
Estimado1=Label(vVisual,bg="#ACFA58",font=10)
Estimado1.place(x=430,y=162)
Diferencia1=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia1.place(x=1130,y=162)
E1=IntVar()
e1=Entry(vVisual,textvariable=E1,width=10)
e1.place(x=825,y=179)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e1.get(),0)).place(x=895,y=173)
#Fila 2---------------------------------------------------------------------------------------
Realval2=""
Real2=Label(vVisual,text="Valor actual="+str(Realval2),bg=colorrojo)
Real2.place(x=688,y=202)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=223)
Rubro2=Label(vVisual,bg="white",font=10)
Rubro2.place(x=3,y=206)
Estimado2=Label(vVisual,bg="#ACFA58",font=10)
Estimado2.place(x=430,y=206)
Diferencia2=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia2.place(x=1130,y=206)
E2=IntVar()
e2=Entry(vVisual,textvariable=E2,width=10)
e2.place(x=825,y=223)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e2.get(),1)).place(x=895,y=217)
#Fila 3---------------------------------------------------------------------------------------
Realval3=""
Real3=Label(vVisual,text="Valor actual="+str(Realval3),bg=colorrojo)
Real3.place(x=688,y=246)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=267)
Rubro3=Label(vVisual,bg="white",font=10)
Rubro3.place(x=3,y=250)
Estimado3=Label(vVisual,bg="#ACFA58",font=10)
Estimado3.place(x=430,y=250)
Diferencia3=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia3.place(x=1130,y=250)
E3=IntVar()
e3=Entry(vVisual,textvariable=E3,width=10)
e3.place(x=825,y=267)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e3.get(),2)).place(x=895,y=261)
#Fila 4---------------------------------------------------------------------------------------
Realval4=""
Real4=Label(vVisual,text="Valor actual="+str(Realval4),bg=colorrojo)
Real4.place(x=688,y=290)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=311)
Rubro4=Label(vVisual,bg="white",font=10)
Rubro4.place(x=3,y=294)
Estimado4=Label(vVisual,bg="#ACFA58",font=10)
Estimado4.place(x=430,y=294)
Diferencia4=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia4.place(x=1130,y=294)
E4=IntVar()
e4=Entry(vVisual,textvariable=E4,width=10)
e4.place(x=825,y=311)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e4.get(),3)).place(x=895,y=305)
#Fila 5---------------------------------------------------------------------------------------
Realval5=""
Real5=Label(vVisual,text="Valor actual="+str(Realval5),bg=colorrojo)
Real5.place(x=688,y=334)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=355)
Rubro5=Label(vVisual,bg="white",font=10)
Rubro5.place(x=3,y=338)
Estimado5=Label(vVisual,bg="#ACFA58",font=10)
Estimado5.place(x=430,y=338)
Diferencia5=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia5.place(x=1130,y=338)
E5=IntVar()
e5=Entry(vVisual,textvariable=E5,width=10)
e5.place(x=825,y=355)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e5.get(),4)).place(x=895,y=349)
#Fila 6---------------------------------------------------------------------------------------
Realval6=""
Real6=Label(vVisual,text="Valor actual="+str(Realval6),bg=colorrojo)
Real6.place(x=688,y=378)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=399)
Rubro6=Label(vVisual,bg="white",font=10)
Rubro6.place(x=3,y=382)
Estimado6=Label(vVisual,bg="#ACFA58",font=10)
Estimado6.place(x=430,y=382)
Diferencia6=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia6.place(x=1130,y=382)
E6=IntVar()
e6=Entry(vVisual,textvariable=E6,width=10)
e6.place(x=825,y=399)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e6.get(),5)).place(x=895,y=393)
#Fila 7---------------------------------------------------------------------------------------
Realval7=""
Real7=Label(vVisual,text="Valor actual="+str(Realval7),bg=colorrojo)
Real7.place(x=688,y=422)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=443)
Rubro7=Label(vVisual,bg="white",font=10)
Rubro7.place(x=3,y=426)
Estimado7=Label(vVisual,bg="#ACFA58",font=10)
Estimado7.place(x=430,y=426)
Diferencia7=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia7.place(x=1130,y=426)
E7=IntVar()
e7=Entry(vVisual,textvariable=E7,width=10)
e7.place(x=825,y=443)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e7.get(),6)).place(x=895,y=437)
#Fila 8---------------------------------------------------------------------------------------
Realval8=""
Real8=Label(vVisual,text="Valor actual="+str(Realval8),bg=colorrojo)
Real8.place(x=688,y=466)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=487)
Rubro8=Label(vVisual,bg="white",font=10)
Rubro8.place(x=3,y=470)
Estimado8=Label(vVisual,bg="#ACFA58",font=10)
Estimado8.place(x=430,y=470)
Diferencia8=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia8.place(x=1130,y=470)
E8=IntVar()
e8=Entry(vVisual,textvariable=E8,width=10)
e8.place(x=825,y=487)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e8.get(),7)).place(x=895,y=481)
#Fila 9---------------------------------------------------------------------------------------
Realval9=""
Real9=Label(vVisual,text="Valor actual="+str(Realval9),bg=colorrojo)
Real9.place(x=688,y=510)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=531)
Rubro9=Label(vVisual,bg="white",font=10)
Rubro9.place(x=3,y=514)
Estimado9=Label(vVisual,bg="#ACFA58",font=10)
Estimado9.place(x=430,y=514)
Diferencia9=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia9.place(x=1130,y=514)
E9=IntVar()
e9=Entry(vVisual,textvariable=E9,width=10)
e9.place(x=825,y=531)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e9.get(),6)).place(x=895,y=525)
#Fila 10--------------------------------------------------------------------------------------
Realval10=""
Real10=Label(vVisual,text="Valor actual="+str(Realval10),bg=colorrojo)
Real10.place(x=688,y=554)
Label(vVisual,text=tex2,bg=colorrojo).place(x=688,y=575)
Rubro10=Label(vVisual,bg="white",font=10)
Rubro10.place(x=3,y=558)
Estimado10=Label(vVisual,bg="#ACFA58",font=10)
Estimado10.place(x=430,y=558)
Diferencia10=Label(vVisual,bg="#FE9A2E",font=10)
Diferencia10.place(x=1130,y=558)
E10=IntVar()
e10=Entry(vVisual,textvariable=E10,width=10)
e10.place(x=825,y=575)
Button(vVisual,text=tex3,bg=colorrojo,activebackground=coloramarillo,command=lambda:modificarcalsevisual(e10.get(),9)).place(x=895,y=569)
#Fila Total---------------------------------------------------------------------------------------
EstimadoTotal=Label(vVisual,bg="white",font=("Impact",18))
EstimadoTotal.place(x=435,y=630)
RealTotal=Label(vVisual,bg="white",font=("Impact",18))
RealTotal.place(x=785,y=630)
DiferenciaTotal=Label(vVisual,bg="white",font=("Impact",18))
DiferenciaTotal.place(x=1135,y=630)

#Muestran menús en las ventanas de creador y visualizador de presupuestos
vVisual.config(menu=menubarra2)
vCreaPresu.config(menu=menubarra)
#Ejecuta ventana principal
v0.mainloop()