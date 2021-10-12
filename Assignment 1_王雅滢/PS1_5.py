# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:02:11 2021

@author: WANG
"""

import random
A=random.randint(0,100)
print(A)
a='123456789'
b=['+','-','']
c=['-','']
d=0
T=[]
for i1 in b:
    for i2 in b:
        for i3 in b:
            for i4 in b:
                for i5 in b:
                    for i6 in b:
                        for i7 in b:
                            for i8 in b:
                                for i9 in c:
                                    result=i9+a[0]+i1+a[1]+i2+a[2]+i3+a[3]+i4+a[4]+i5+a[5]+i6+a[6]+i7+a[7]+i8+a[8]
                                    er=eval(result)
                                    if er == A:
                                        d+=1
                                        print(result,'=',er)                                        
                                    if er in range(1,101):
                                        T.append(er)
print(A,"的解决方案有",d,"种")
Total_solutions = []
for i in range(1,101):
    
    Total_solutions.append(T.count(i))
    max_solution=max(Total_solutions)
    min_solution=min(Total_solutions)
    max_num = Total_solutions.index(max_solution)+1
    min_num = Total_solutions.index(min_solution)+1   
print('0-100中：',max_num,'产生的解决方案最多，共有',max(Total_solutions),'种')
print('0-100中：',min_num,'产生的解决方案最少，共有',min(Total_solutions),'种')
