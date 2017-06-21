class Curso:
    #zona de declaracion de atributos:
    codigo=""
    nombre=""
    horas=0
    semestre=0
    creditos=0

    #constructor
    def __init__(self):
        self.codigo=""
        self.nombre=""
        self.horas=0
        self.semestre=0
        self.creditos=0

    def setCodigo(self, c):
        self.codigo=c

    def setNombre(self, n):
        self.nombre=n

    def setHoras(self, horas):
        self.horas=horas

    def setSemestre(self, s):
        self.semestre=s

    def setCreditos(self, cre):
        self.creditos=cre

    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getHoras(self):
        return self.horas

    def getSemestre(self):
        return self.semestre

    def getCreditos(self):
        return self.creditos

    def toString(self):
        h="\nNombre del Curso: "+ self.nombre
        h+="Codigo del Curso: " + self.codigo
        h+="\nHoras de curso: " + str(self.horas)
        h+="\nCreditos del curso: "+ str(self.creditos)
        h+="\nSemestre del curso: "+ str(self.semestre)
        return h
    
    def setCurso(self, c, n, horas, cre, s):
        self.codigo=c
        self.nombre=n
        self.horas=horas
        self.creditos=cre
        self.semestre=s
