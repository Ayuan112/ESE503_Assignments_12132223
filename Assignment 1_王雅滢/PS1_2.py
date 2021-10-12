# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 19:42:05 2021

@author: WANG
"""
#from random import randint
#M=random.randint(0,50,(5,10))

import numpy as np

M1=np.random.randint(0,51,size=(5,10))
M2=np.random.randint(0,51,size=(10,5))

print(M1,M2)


result = np.zeros((5,5),int)
for i in range(len(M1)):#01234
    for j in range(len(M2[0])):#01234
       for k in range(len(M2)):#0123456789
           result[i][j] += M1[i][k] * M2[k][j]
           #print(result[i][j])
         
print(result)

   
