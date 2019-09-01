# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:26:37 2019

@author: Tang
"""

'''
题目描述



请设计一个算法，计算n的阶乘有多少个尾随零。

给定一个int n，请返回n的阶乘的尾零个数。保证n为正整数。

测试样例：
5
返回：1
'''
def getFactorSuffixZero( n):
        # write code here
        s=0
        r=5
        while r<=n:
            s+=n//r
            r*=5
        return s

def solution(a):
     res=0
     m=1
     for i in range(len(a)-1):
         tmp=a[i]
         num=1
         for j in range(i+1,len(a)):
              if abs(a[j]-a[i])==1 or (a[j]-a[i])==0:
                   continue
              else:
                   tmp+=a[j]
                   num+=1
         if tmp>res:
              res=tmp
              m=num
     print(res,m)
solution(a=[1,2,3,1])
from sklearn.cluster.k_means_