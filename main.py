#!/usr/bin/env python3
 
from math import pi, floor



lista=[23,"dos","perro",23,45]


def isnumber(item): 
    result = type(item) in (int,float)  
    return result 

def main ():
    
    lista2 = [isnumber(val) for val in lista]
    print(lista2)


    
main()





