from __future__ import division
import pickle
import random

#Clases
#---------------------------------------------------------------
class Estudiante:
    def __init__(self,Carnet,Nombre):
        self.Carnet=Carnet
        self.Nombre=Nombre
    def getEstudiante(self):
        return [self.Carnet,self.Nombre]

class Urna: 
    def __init__(self,Id,Padron,CantVotan):
        self.Id=Id
        self.Padron=Padron
        self.CantVotan=CantVotan
    def getUrna(self):
        return [self.Id,self.Padron,self.CantVotan]

class Papeleta:
    def __init__(self,Urna,Cand1,Cand2,Cand3):
        self.Urna=Urna
        self.Cand1=Cand1
        self.Cand2=Cand2
        self.Cand3=Cand3
    def getPapeleta(self):
        return [self.Urna,self.Cand1,self.Cand2,self.Cand3]
#---------------------------------------------------------------

#Variables Globales
#---------------------------------------------------------------

Names = ['Pedro','Andres','Raquel','Karina','Ximena','Natasha','Felipe','Montserrat','Daniel','Melisa','Sammy','Ricardo','Pablo','Laura','Jose','Heiner','Salvador','Paula','Gabriel','Noelia','Enrique','Maria Fernanda','Lucia','Raimond','Pier','Jose Ignacio','Ignacio','Esteban','Kevin','Stephanie','Victoria','Jorge','Pamela','Glenn','Julian','Rodolfo','Edgardo','Rolando','Luciano','Edson','Arlin','Lourdes','Jimena','Emilio','Andrea','Justin','Josef','Rocio','Diego','Mariel','Alvaro','Ivan','Monica','Allan','Camila','Michelle','Adrian','Brandon','Eliecer','Giancarlo','Douglas','Loana','Adriana','Warren','Sara','Mariana','Martha','Sebastian','Manuela','Mariela','Fabio','Javier','Fiorella','Nicolas','Nicole','Julia','Mauricio','Larry','Alejandra','Alanna','Gabriela','Sharon','Natalie','Myron','Cristian','Norma','Maria Paula','Andrey','Eduardo','Alonso','Kael','Maripaz','Diana','Joe','Melany','Fabian','Leonardo','Josue']
LastNames = ['Delgado','Campos','Soto','Riggioni','Cordero','Chavarria','Matamoros','Alberty','Rojas','Ramirez','Chavez','Marin','Lopez','Gonzalez','Rodriguez','Solis','Barrantes','Thuel','Arley','Elizondo','Solano','Sanauja','Morales','Obando','Guerrero','Mondragon','Salazar','Perez','Venegas','Cartin','Rivera','Murillo','Fallas','Fuentes','Arce','Arias','Timms','Chacon','De Santa','Vargas','Arroyo','Brenes','Alvarado','Sanchez','Corrales','Jimenez','Pozuelo','Herrera','Gomez','Cortes','Arbenz','Siberon','Tobon','Navarro','Monge','Pereira','Montero','Hernandez','Gutierrez','Madrigal','Calderon','Pacheco','Mora','Abdalla','Carmona','Fonseca','Sandoval','Latham','Koberg','Horton','Piedra','Joachim','Vaca','Chinchilla','Zamora','Fernandez','Zapata','Saenz','Lira','Badilla','Rivera','Salas','Mendez','Arias','Escobar','Borge','Robles','Naranjo','Leiva','Lelchuk','Valverde','Camacho','Leandro','Troyo','Omodeo','Moraga','Beltran','Flores','Benavides','Alfaro','Martinez','Falcon','Adams','Sancho','Carvajal','Mendez','Blanco','Calvo','Villalobos','Montoya','Ochoa','Maynard','Stanka','Vaglio','Picado','Diez','Leon','Acosta','Arrieta','Muntean','Bryant','Trejos','Apu','Madriz','Chen','Villalta','Lascarez','Ramos','Ugalde','Molina','Segura','Scianna','Hansen','Szelagowski','Schmidt','Barboza','Sweeney','Castillo','Suarez','Giordanelli','Garro','Miranda','Zeledon','Alvarez','Cordoba','Forester','Aguilar','Arce','Ruiz','Bermudez']
PapeletasTotal = []
validez = [0,0]
votacionesGlobal=[0,0,0]
estadoGlobal=[0,0,0]
votosValidos=[]
votosContados = [0,0,0]
StudentDataBase = []
BallotBoxDataBase = []
#---------------------------------------------------------------

#Funciones
#---------------------------------------------------------------
def addStudent(nombre,carnet):
    e = Estudiante(nombre,carnet)
    StudentDataBase.append(e)
    with open('StudentDataBase.dat', 'wb') as f:
        pickle.dump(StudentDataBase, f)
        
def VerEstudiantes():
    for x in StudentDataBase:
        print(x.getEstudiante())

def crearUrnas():
    global BallotBoxDataBase, StudentDataBase
    totalpadron=len(StudentDataBase)
    listaTemp=StudentDataBase
    if totalpadron%25==0:
        totalUrnas=(totalpadron//25)
    else:
        totalUrnas=(totalpadron//25)+1
    i=0
    while i!=totalUrnas:
        Id=100+i
        ListaPadron=[]
        for x in range(0,25):
            try:
                agregar=listaTemp[x]
                agregar=agregar.getEstudiante()
                ListaPadron.append(agregar)
            except:
                break
        i+=1
        cantVot=random.randint(0,len(ListaPadron))
        listaTemp=listaTemp[25:]
        u= Urna(Id, ListaPadron,cantVot)
        BallotBoxDataBase.append(u)
            
def VerUrnas():
    for x in BallotBoxDataBase:
        print(x.getUrna())

def situacionUrna(Id):
    global BallotBoxDataBase,votacionesGlobal
    totalUrnas=len(BallotBoxDataBase)
    for i in BallotBoxDataBase:
        urnaInfo=i.getUrna()
        urnaId=urnaInfo[0]
        if Id==urnaId:
            print "Situacion en Urna No."+str(Id)+":"
            padronUrna=urnaInfo[1]
            votacionesGlobal[0]+=len(padronUrna)
            asistentes=urnaInfo[2]
            votacionesGlobal[1]+=asistentes
            votacionesGlobal[2]+=len(padronUrna)-asistentes
            print "El padrón está compuesto por "+str(len(padronUrna))+" estudiantes"
            print "Han venido a votar "+str(asistentes)+" estudiantes"
            print "Entonces no han venido a votar "+str(len(padronUrna)-asistentes)+" estudiantes\n"
        else:
            pass
    
    return None

def situacionGlobal():
    global votacionesGlobal
    print "En total, el padrón está compuesto por "+str(votacionesGlobal[0])+" estudiantes"
    print "Han venido a votar, en total, "+str(votacionesGlobal[1])+" estudiantes"
    print "Entonces no han venido a votar "+str(votacionesGlobal[2])+" estudiantes, en total.\n"
    return None

def votaciones():
    global BallotBoxDataBase,validez,PapeletasTotal
    for x in BallotBoxDataBase:
        votantesDisp=x.getUrna()
        Urna=votantesDisp[0]
        votantesDisp=votantesDisp[2]
        z=0
        while z!=votantesDisp:
            num = random.randint(1,1000)
            if num%2==0: #Voto valido
                validez[0] += 1
                candidatos=[1,2,3]
                voto=random.choice(candidatos)
                if voto==1:
                    Cand1=True
                    Cand2=False
                    Cand3=False
                elif voto==2:
                    Cand1=False
                    Cand2=True
                    Cand3=False
                else:
                    Cand1=False
                    Cand2=False
                    Cand3=True
                p=Papeleta(Urna,Cand1,Cand2,Cand3)
                PapeletasTotal.append(p)
                votosValidos.append(p)
            else:   #Voto invalido
                validez[1] += 1
                formadevoto=[0,2,3]
                voto=random.choice(formadevoto)
                Cand1=False
                Cand2=False
                Cand3=False
                i=0
                while i!=voto:
                    avotar=[1,2,3]
                    votar=random.choice(avotar)
                    if votar==1:
                        Cand1=True
                    elif votar==2:
                        Cand2=True
                    else:
                        Cand3=True
                    avotar.remove(votar)
                    votar=random.choice(avotar)
                    if votar==1:
                        Cand1=True
                    elif votar==2:
                        Cand2=True
                    else:
                        Cand3=True
                    i+=1
                p=Papeleta(Urna,Cand1,Cand2,Cand3)
                PapeletasTotal.append(p)
            z+=1
    return None
        

def papeletasEnEstado(UrnaId,Situacion):
    global PapeletasTotal, estadoGlobal
    votosVNV=[0,0,0]
    for i in PapeletasTotal:
        papeleta=i.getPapeleta()
        sacarId=papeleta[0]
        if sacarId==UrnaId:
            cond="Blanco"
            for i in [1,2,3]:
                if papeleta[i]==True:
                    if cond=="Blanco":
                        cond="Valido"
                    elif cond=="Valido":
                        cond="Excess"
                    else:
                        pass
            if cond=="Blanco":
                votosVNV[2]+=1
                estadoGlobal[2]+=1
            elif cond=="Valido":
                votosVNV[0]+=1
                estadoGlobal[0]+=1
            else:
                votosVNV[1]+=1
                estadoGlobal[1]+=1
    if Situacion=="V":
        return "Se contabilizaron "+str(votosVNV[0])+" votos validos"
    elif Situacion=="N":
        return "Se contabilizaron "+str(votosVNV[1])+" votos nulos"
    else:
        return "Se contabilizaron "+str(votosVNV[2])+" votos en blanco"
    
def Contabilidadfinal():
    global estadoGlobal
    print "He aquí el conteo total de votos validos y no validos:"
    print "Se contabilizaron "+str(estadoGlobal[0]//3)+" votos validos"
    print "Se contabilizaron "+str(estadoGlobal[1]//3)+" votos nulos"
    print "Se contabilizaron "+str(estadoGlobal[2]//3)+" votos en blanco"

#Hacerlo por urna
def ganador():
    global votosContados
    global votosContados,votosValidos
    for i in votosValidos:
        papeleta=i.getPapeleta()
        Cand1voto=papeleta[1]
        if Cand1voto:
            votosContados[0]+=1
        else:
            Cand2voto=papeleta[2]
            if Cand2voto:
                votosContados[1]+=1
            else:
                votosContados[2]+=1
    i=1
    while i!=4:
        print "Candidato "+str(i)+" ha obtenido "+str(votosContados[i-1])+" votos"
        i+=1
    votosganador=max(votosContados)
    if votosContados.count(votosganador)>1:
        return "Hubo un empate entre dos candidatos"
    else:
        if votosContados[0]==votosganador:
            return "El ganador de esta elecciones es el Candidato 1"
        elif votosContados[1]==votosganador:
            return "El ganador de esta elecciones es el Candidato 2"
        else:
            return "El ganador de esta elecciones es el Candidato 3"
#---------------------------------------------------------------

#Ejecución del código
#---------------------------------------------------------------
cantidadpadron=random.randint(50,200)
i=1
print ("====================================================================")
print ("                        Elecciones ASODEC 2013                      ")
print ("====================================================================")
while i<=cantidadpadron:
    nombre=Names[random.randint(0,len(Names)-1)]
    apellido=LastNames[random.randint(0,len(LastNames)-1)]
    carnet=20130000+i
    addStudent(str(nombre)+" "+str(apellido),carnet)
    i+=1
print ("====================================================================")
print ("                         Padrón Electoral                           ")
print ("====================================================================")
VerEstudiantes()
print ("====================================================================")
print ("                   VOTACIONES EN PROGRESO!                          ")
print ("====================================================================")
print ("................................................!")
print ("====================================================================")
print ("                   VOTACIONES FINALIZADAS!                          ")
print ("====================================================================")
print ("====================================================================")
print ("                         Urnas de votación                          ")
print ("====================================================================")
crearUrnas()
for i in BallotBoxDataBase:
    urnaId=i.getUrna()
    urnaId=urnaId[0]
    situacionUrna(urnaId)
situacionGlobal()
votaciones()
print ("====================================================================")
print ("                    Estadística de votos                            ")
print ("====================================================================")
UrnasIds=[]
for i in BallotBoxDataBase:
    urna=i.getUrna()
    urna=urna[0]
    UrnasIds.append(urna)
for i in UrnasIds:
    print ("Situacion en urna No."+str(i))
    print papeletasEnEstado(i,"V")
    print papeletasEnEstado(i,"N")
    print papeletasEnEstado(i,"B")+"\n"
    for i in estadoGlobal:
        i=i/3
Contabilidadfinal()
print ("====================================================================")
print ("                          Resultado                                 ")
print ("====================================================================")
print ganador()
