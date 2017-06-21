'''
Created on 16/05/2013

@author: Pedro
'''
def imp_vector(vector):
    for v in range(0, len(vector)):
        print vector[v]
    
def imp_matriz(matriz):
    for i in range(0, len(matriz)):
        for k in range(0, len(matriz[i])):
            print matriz[i][k],
        print