class Fecha:
    #zona de declaracion de atributos
    dia=0
    mes=0
    anno=0
    ddls=""

    #Constructor
    def __init__(self):
        self.dia=0
        self.mes=0
        self.anno=0
        self.ddls=""

    def setdia(self,d):
        self.dia=d

    def setmes(self,m):
        self.mes=m

    def setanno(self,a):
        self.anno=a

    def setddls(self,dd):
        self.ddls=dd

    def getdia():
        return self.dia

    def getmes():
        return self.mes

    def getanno():
        return self.anno

    def getddls():
        return self.ddls

    def toInt(self):
        h=str(self.dia)+"/"+str(self.mes)+"/"+str(self.anno)+"\n"
        return h

    def toString(self):
        x="\nDia de la semana: "+str(self.ddls)
        return x

    def setFecha(self,d,m,a,dd):
        self.dia=d
        self.mes=m
        self.anno=a
        self.ddls=dd
