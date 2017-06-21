m=[["w","o","k","m","t"],["o","r","r","a","c"],["s","r","e","i","a"],["z","a","l","a","s"],["b","s","o","p","a"],["c","t","s","w","v"]]

def recupereColUpDown(m, numCol):
    col=[]
    for i in range(0,len(m),1):
        col.append(m(i))[numCol]
    return col

def recupereColDownUp(m, numCol):
    col=[]
    for i in range(len(m)-1, -1, -1):
        col.append(m[i][numCol])
    return col

def buscar