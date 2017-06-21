class Persona:
    #zona de declaracion de atributos
    iden=""
    nombre=""
    fechaNac=""

    #zona de declaracion de operaciones

    #Constructor..
    def __init__(self):
        self.iden=""
        self.nombre=""
        self.fechaNac=""

    def setIden(self, i):
        self.iden= i

    def setNombre(self, n):
        self.nombre= n

    def setFechaNac(self, fn):
        self.fechaNac= fn

    def getIden(self):
        return self.iden

    def getNombre(self):
        return self.nombre
    
    def getFechaNac(self):
        return self.fechaNac

    def toString(self):
        h ="Id:" + self.iden
        h+="\nNombre: "+ self.nombre
        h+="\nFN: " + self.fechaNac
        return h

    def setPersona(self, i, n, fn):
        self.iden=i
        self.nombre= n
        self.fechaNac= fn
