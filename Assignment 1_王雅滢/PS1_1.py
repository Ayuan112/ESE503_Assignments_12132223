# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 14:33:02 2021

@author: WANG
"""
import random
a=random.randint(0,100)
b=random.randint(0,100)
c=random.randint(0,100)
print(a,b,c)
def value():  
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b>c:
            if a>c:
                print(b,a,c)
            else:
                print(b,c,a)
        else:
            print(c,b,a)
value()
     
        
    
        
        
    
    
    
  