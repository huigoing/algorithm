# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:53:46 2019

@author: Tang
"""

'''
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
def fugai(n):
     if n<=0:
          return 0
     if n==1:
          return 1
     if n==2:
          return 2
     a=[0 for i in range(n)]
     a[0]=1
     a[1]=2
     for i in range(2,n):
          a[i]=a[i-1]+a[i-2]
     
     return a[n-1]
print(fugai(2))
     