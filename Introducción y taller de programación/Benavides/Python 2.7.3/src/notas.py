'''
Created on 07/03/2013

@author: Leeecher
'''
'''Entrada: Un numero entero entre 0 y 100, que corresponde a la nota del estudiante.
Salida: La condicion del estudiante, aprobado o reprobado.
Restricciones: El numero no puede ser negativo ni mayor a 100
'''
nota=0
def AprobReprob():
    nota=input("Favor inserir nota del estudiante: ")
    if 0<=nota<=100:
        if nota < 70:
            print("Estudiante se encuentra reprobado")
        else:
            print("Estudiante se encuentra aprobado")
    else:
        print("Nota no es valida")

def Condicion(nota):
    if 90<=nota<=100:
        print("Estudiante es excelente")
    elif 70<=nota<90:
        print("Estudiante es bueno")
    elif 60<=nota<70:
        print("Estudiante es regular")
    elif 30<=nota<60:
        print("Estudiante es malo")
    elif nota<0 or nota>100:
        print("Nota no valida")
    else:
        print("Estudiante es pesimo")