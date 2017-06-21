def VinieronaVotar():
    import random
    global StudentDataBase, llegan
    l = random.randint(0,len(StudentDataBase)-1)
    x=0
    while x <= l:
        total = len(llegan)
        num = random.randint(0,len(StudentDataBase)-1)
        datosEst = StudentDataBase[num]
        if total == 0:
            llegan.append(datosEst)
        else:
            w=0
            while w <= total:
                for i in range(len(llegan)):
                    if w == total:
                        llegan.append(datosEst)
                        w += 1
                    elif datosEst[0] == llegan[i][0]:
                        w = total + 1
                    else:
                        w += 1
        x += 1
    print llegan


#Original
def VinieronaVotar():
    import random
    global StudentDataBase, llegan
    l = random.randint(0,len(StudentDataBase)-1)
    x=0
    while x <= l:
        total = len(llegan)
        num = random.randint(0,len(StudentDataBase)-1)
        datosEst = StudentDataBase[num]
        for i in range(len(llegan)):
            if total == 0:
                llegan.append(datosEst)
            else:
                while w <= total:
                    if w == total:
                        llegan.append(datosEst)
                        w += 1
                    elif datosEst[0] == llegan[i][0]:
                        w = total + 1
                    else:
                        w += 1
        x += 1
    return llegan
