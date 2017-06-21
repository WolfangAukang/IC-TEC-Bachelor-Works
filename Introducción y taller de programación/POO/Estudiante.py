class Estudiante:
    #zona de declaracion de atributos
    carnet=0
    nombre=""
    carrera=""
    cedula=0

    #constructor
    def __init___(self):
        self.carnet=0
        self.nombre=""
        self.carrera=""
        self.cedula=0

    def setCarnet(self, carn):
        self.carnet=carn

    def setNombre(self, n):
        self.nombre=n

    def setCarrera(self,carr):
        self.carrera=carr

    def setCedula(self,ce):
        self.cedula=ce

    def getCarnet(self):
        return self.carnet

    def getNombre(self):
        return self.nombre

    def getCarrera(self):
        return self.carrera

    def getCedula(self):
        return self.cedula

    def toString(self):
        h="Carnet del estudiante: " + str(self.carnet)
        h+="\nNombre del estudiante: " + self.nombre
        h+="\nCarrera en la que cursa: " + self.carrera
        h+="\nCedula del estudiante: "+ str(self.cedula)
        return h

    def setEstudiante(self, carn, n, carr, ce):
        self.carnet=carn
        self.nombre=n
        self.carrera=carr
        self.cedula=ce
