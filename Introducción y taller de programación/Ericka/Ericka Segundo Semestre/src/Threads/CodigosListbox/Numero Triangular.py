def numerotriangular(n):
    if n==1:
        return 1
    else:
        return n + numerotriangular(n-1)
