# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:02:03 2021

@author: WANG
"""

def Least_moves(a):
    i=0
    while a > 1:
        if a % 2 ==0:
            a=a/2
        else:
            a=a-1
        i+=1
    print(i)
Least_moves(10)
