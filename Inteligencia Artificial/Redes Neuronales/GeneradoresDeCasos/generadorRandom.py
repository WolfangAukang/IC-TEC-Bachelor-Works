import numpy as np
from random import randint, shuffle

def luggage():
    hordish = []
    for i in np.random.random_sample((16,)):
        hordish += [int(round(i))]
    return hordish

def countBitso():
    cant = 0
    rangeObt = 0
    lista = luggage()
    for i in lista:
        if i == 1:
            cant+=1
    if cant <= 3:
        rangeObt = [1,0,0,0]
    elif cant <= 7:
        rangeObt = [0,1,0,0]
    elif cant <= 11:
        rangeObt = [0,0,1,0]
    else:
        rangeObt = [0,0,0,1]
    print("{ input: "+ str(lista) +", output: "+str(rangeObt)+" }, cant:"+str(cant))

def countBitson():
    number = randint(0,16)
    if (number == 0):
        lista = str([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        outputLista = str([1,0,0,0])
    elif (number == 1):
        lista = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([1,0,0,0])
    elif (number == 2):
        lista = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([1,0,0,0])
    elif (number == 3):
        lista = [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([1,0,0,0])
    elif (number == 4):
        lista = [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([0,1,0,0])
    elif (number == 5):
        lista = [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([0,1,0,0])
    elif (number == 6):
        lista = [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([0,1,0,0])
    elif (number == 7):
        lista = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([0,1,0,0])
    elif (number == 8):
        lista = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([0,0,1,0])
    elif (number == 9):
        lista = [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([0,0,1,0])
    elif (number == 10):
        lista = [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([0,0,1,0])
    elif (number == 11):
        lista = [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
        shuffle(lista)
        outputLista = str([0,0,1,0])
    elif (number == 12):
        lista = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0]
        shuffle(lista)
        outputLista = str([0,0,0,1])
    elif (number == 13):
        lista = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
        shuffle(lista)
        outputLista = str([0,0,0,1])
    elif (number == 14):
        lista = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
        shuffle(lista)
        outputLista = str([0,0,0,1])
    elif (number == 15):
        lista = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]
        shuffle(lista)
        outputLista = str([0,0,0,1])
    else:
        lista = str([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        outputLista = str([0,0,0,1])
    print("{ input: "+ str(lista) +", output: "+outputLista+" }, cant:"+str(number))


def countBits(listToCount):
    cant = 0
    rangeObt = 0
    for i in listToCount:
        if i == '1':
            cant+=1
    if cant <= 3:
        rangeObt = [1,0,0,0]
    elif cant <= 7:
        rangeObt = [0,1,0,0]
    elif cant <= 11:
        rangeObt = [0,0,1,0]
    else:
        rangeObt = [0,0,0,1]
    print("{ input: "+ str(listToCount) +", output: "+str(rangeObt)+" },")

def genNumber(end, initial = 0):
    for i in range(initial, end):
        generated = str(addZeroes(16 - len(bin(i)[2::]))) + str(bin(i)[2::])
        countBits(list(generated))

def addZeroes(numberOfZeros):
    stringToReturn = ""
    for i in range(numberOfZeros):
        stringToReturn = ''.join(['0',stringToReturn])
    return stringToReturn

for i in range(40):
    countBitson()
#genNumber(initial = 50000, end = 65536)
#65536
