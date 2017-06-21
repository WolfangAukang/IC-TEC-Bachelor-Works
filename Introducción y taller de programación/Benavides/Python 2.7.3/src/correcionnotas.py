'''
Created on 07/03/2013

@author: Leeecher
'''
def AprobReprob():
    nota=input("Favor inserir nota del estudiante: ")
    if 0<=nota<=100:
        if nota < 70:
            print("Estudiante se encuentra reprobado")
        else:
            print("Estudiante se encuentra aprobado")
    else:
        print("Nota no es valida")
    return "La condicion del estudiante es", (Condicion(nota))
    
def Condicion(nota):
    if 90<=nota<=100:
        return"excelente"
    elif 70<=nota<90:
        return"bueno"
    elif 60<=nota<70:
        return "regular"
    elif 30<=nota<60:
        return"malo"
    else:
        return"pesimo"