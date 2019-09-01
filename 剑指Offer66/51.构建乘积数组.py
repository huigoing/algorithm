# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:42:25 2019

@author: Tang
"""

'''
题目描述


给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素
B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''
def solution(a):
     b=[0 for i in range(len(a))]
     for i in range(len(a)):
          #tmp=1
          res=1
          if i==0:
               tmp=1
          else:
               tmp*=a[i-1]
          for j in range(i+1,len(a)):
               res*=a[j]
          b[i]=tmp*res
     return b
print(solution([1,2,3,4,2]))