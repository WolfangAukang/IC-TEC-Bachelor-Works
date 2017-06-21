from Curso import *
from Profesor import *

class Grupo:
    #zona de declaracion de atributos
    numero=0
    horario=""
    aula=""
    cantEst=0
    datosCurso=Curso()
    datosProfe=Profesor()
    listaEstudiantes=[]

    #constructor
    def __init__(self):
        self.numero=0
        self.horario=""
        self.aula=""
        self.cantEst=0
        self.datosCurso=Curso()
        self.datosProfe=Profesor()
        listaEstudiantes=[]

    def setNumero(self,n):
        self.numero=n

    def setHorario(self,h):
        self.horario=h

    def setAula(self,a):
        self.aula=a

    def setcantEst(self,ce):
        self.cantEst=ce

    def setdatosCurso(self,dc):
        self.datosCruso=dc

    def setdatosProfe(self,dp):
        self.datosProfe=dp

    def setlistaEstudiantes(self, le):
        self.listaEstudiantes=le

    def getNumero(self):
        return self.numero

    def getHorario(self):
        return self.horario

    def getAula(self):
        return self.aula

    def getcantEst(self):
        return self.cantEst

    def getdatosCurso(self):
        return self.datosCurso

    def getlistaEstudiantes(self):
        return self.listaEstudiantes

    def toString(self):
        z ="Numero:" + str(self.numero)
        z+="\nHorario: "+ self.horario
        z+="\nAula: " + self.aula
        z+="\nCantidad Estudiantes: " + str(self.cantEst)
        z+="\nDatos Curso: " + self.datosCurso.toString()
        z+="\nDatos Profesor: " + self.datosProfe.toString()
        z+="\nLista Estudiantes: " + str(self.listaEstudiantes)
        return z

    def setGrupo(self, n, h, a, ce, dc, dp, le):
        self.numero= n
        self.horario= h
        self.aula= a
        self.cantest= ce
        self.datoscurso= dc
        self.datosprofe= dp
        self.listaestudiantes= le
