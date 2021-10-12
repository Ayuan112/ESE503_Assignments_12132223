# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:59:40 2021

@author: WANG
"""
'''
第n行的第1个数为1，第二个数为1×(n-1)，第三个数为1×(n-1)×（n-2）/2，
第四个数为1×(n-1)×（n-2）/2×（n-3）/3…
几行就有几个数

'''


'''

#方案1:到53还是可行的，后面的数字就有错误了，不清楚哪儿错了。
def Pascal_triangle(k):
    a=1
    b=1
    for i in range(1,k+1):
        if i==1 or i==k :
            print(1)
        elif i<k:
            b=1*(k-i+1)/(i-1)
            a=a*b
            print(int(a))
            #continue
        i+=1        
Pascal_triangle(30)
#Pascal_triangle(200)
'''

#方案2：
def Pascal_triangle(k):
    result=[[1],[1,1]]
    a=[1,1]
    
    for i in range(2,k):
        r=[]
        for j in range(len(a)-1):
            r.append(a[j]+a[j+1])
        a=[1]+r+[1]
        result.append(a)
    #print(result)
    print(result[k-1])
Pascal_triangle(100)
Pascal_triangle(200)