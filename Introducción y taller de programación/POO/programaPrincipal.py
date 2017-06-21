#programa principal
from Profesor import *
from Curso import *
from Estudiante import *
from Grupo import *

listaC=[] #lista de cursos global
listaP=[] #lista de profesores global
listaE=[] #lista de Estudiantes global

def generarProfes():
    global listaP
    for i in range(1,10,1):
        p=Profesor()
        p.setProfesor(i, "Prof. "+str(i), str(i), "Profe","CA","IC",100)
        listaP.append(p)


def generarCursos():
    global listaC
    for i in range(1,10,1):
        c=Curso()
        c.setCurso("IC-0"+str(i), "Curso-0"+str(i),16,8,i)
        listaC.append(c)

def generarEstudiantes():
    global listaE
    for i in range(1,10,1):
        e=Estudiante()
        e.setEstudiante(i,"Est "+str(i),"CA",i)
        listaE.append(e)

def verProfes():
    global listaP
    for i in listaP:
        print(i.toString()+"\n")

def verEstudiantes():
    global listaE
    for i in listaE:
        print(i.toString()+"\n")

def verCursos():
    global listaC
    for i in listaC:
        print(i.toString()+"\n")

def buscarProfe(cod):
    global listaP
    for i in listaP:
        if i.getCodigo() == cod:
            return i
    return None

def buscarCurso(cod):
    global listaC
    for i in listaC:
        if i.getCodigo()==cod:
            return i
    return None

print("Generando Profesores, Cursos, Estudiantes...")
generarProfes()
generarCursos()
generarEstudiantes()
print("Profesores")
print("=========================")
verProfes()
print("Estudiantes")
print("=========================")
verEstudiantes()
print("Cursos")
print("=========================")
verCursos()

resProfe=buscarProfe(2)
resCurso=buscarCurso("IC-01")
if resProfe != None and resCurso != None:
    g03=Grupo()
    g03.setNumero(3)
    g03.setHorario("K-J 1-3pm")
    g03.setdatosCurso(resCurso)
    g03.setdatosProfe(resProfe)
else:
    print("No se puede crear el grupo porque el profe o el curso no existen")
