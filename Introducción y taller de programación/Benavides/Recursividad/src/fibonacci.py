'''
Created on 31/05/2013

@author: Pedro
'''
def fibonacci(num):
    if num==1 or num==2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)