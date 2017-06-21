class Profesor:
    #zona de declaracion de variables:
    codigo=0
    nombre=""
    cedula=0
    puesto=""
    depto=""
    jornada=""
    salario=0.0

    #constructor
    def __init__(self):
        self.codigo=0
        self.nombre=""
        self.cedula=0
        self.puesto=""
        self.depto=""
        self.jornada=""
        self.salario=0.0

    def setCodigo(self,co):
        self.codigo=co

    def setNombre(self,n):
        self.nombre=n

    def setCedula(self,ce):
        self.cedula=ce

    def setPuesto(self,p):
        self.puesto=p

    def setDepto(self,d):
        self.depto=d

    def setJornada(self,j):
        self.jornada=j

    def setSalario(self,s):
        self.salario=s

    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getCedula(self):
        return self.cedula

    def getPuesto(self):
        return self.puesto

    def getDepto(self):
        return self.depto

    def getJornada(self):
        return self.jornada

    def getSalario(self):
        return self.salario

    def toString(self):
        h="Nombre del empleado: "+self.nombre
        h+="\nCedula del empleado: "+str(self.cedula)
        h+="\nPuesto del empleado: "+self.puesto
        h+="\nDepartamento del empleado: "+self.depto
        h+="\nCodigo del empleado: "+str(self.codigo)
        h+="\nJornadas en la cual labora el empleado: "+self.jornada
        h+="\nSalario que gana el empleado: "+str(self.salario)
        return h

    def setProfesor(self, co, n, ce, p, d, j, s):
        self.codigo=co
        self.nombre=n
        self.cedula=ce
        self.puesto=p
        self.depto=d
        self.jornada=j
        self.salario=s
