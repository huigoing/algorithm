# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:31:47 2019

@author: Tang
"""

'''
题目描述



对于一个有正有负的整数数组，请找出总和最大的连续数列。

给定一个int数组A和数组大小n，请返回最大的连续数列的和。保证n的大小小于等于3000。

测试样例：
[1,2,3,-6,1]
返回：6
'''
def getMaxSum(self, A, n):
        # write code here
        m=A[0]
        cur=A[0]
        for i in A[1:]:
            if i+m>0:
                m=max(i+m,i)
            else:
                m=i
            cur=max(cur,m)
        return cur
s=input()
a=[]
import math
if s!=' ':
     for i in s.split( ):
          a.append(int(i))
          sum=a[0]
          m=a[-1]
          n=a[0]
     for i in range(1,m):
          n=math.sqrt(n)
          sum+=n
     print('%.2f'%sum)
else:
     print('error')