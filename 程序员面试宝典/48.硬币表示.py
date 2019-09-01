# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 18:43:40 2019

@author: Tang
"""

'''
题目描述



有数量不限的硬币，币值为25分、10分、5分和1分，请编写代码计算n分有几种表示法。

给定一个int n，请返回n分有几种表示法。保证n小于等于100000，为了防止溢出，请将答案Mod 1000000007。

测试样例：
6
返回：2
'''
def solution(n):
     if n>100000:
          return None
     res=[0 for i in range(n+1)]
     a=[1,5,10,25]
     res[0]=1
     for i in a:
          for j in range(i,n+1):
              res[j]=res[j]+res[j-i]
     return res[n]%1000000007
print(solution(100))