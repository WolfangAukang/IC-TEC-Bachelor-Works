'''
Created on 14/03/2013

@author: Leeecher
'''
def ejemplofor():
    conjunto=[1,2,3]
    for elemento in range(2,0,-1):
        conjunto[elemento]+=conjunto[elemento%3]
    return conjunto