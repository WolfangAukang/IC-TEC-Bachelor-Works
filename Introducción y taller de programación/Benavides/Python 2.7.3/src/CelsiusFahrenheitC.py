from __future__ import division
'''
Created on 07/03/2013

@author: Leeecher
'''
def CelFah():
    celsius=input("digite la temperatura en celsius: ")
    fahrenheit=9/5*celsius+32
    return fahrenheit

def FahCel():
    fahrenheit=input("digite la temperatura en fahrenheit: ")
    celsius=5/9*(fahrenheit-32)
    return celsius